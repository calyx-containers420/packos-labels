---
name: quote-labels
description: Get official PackOS quotes for custom printed roll labels, from a description or from the label artwork (PDF), and help the person save it or order it on packos.ai. Use when someone asks what labels cost, wants a label quote, price breaks or lead time, or shares label artwork to be priced.
---

# Quoting roll labels with PackOS

PackOS prices custom printed labels on rolls. Every price comes from the PackOS estimating engine through the
`packos` connector. **Never estimate, round, convert or recompute a price** — repeat the summary sentence a
quote returns, word for word, and show the numbers it returns as they are.

## The tools

| Tool | Use it to |
|---|---|
| `packos_get_quoting_rules` | Learn what is quoted online: sizes, materials, finishes, effects, quantity rules, lead time, terms. Call it first if unsure. |
| `packos_read_label_artwork` | Read the person's label PDF: size, shape, colours, white, effects, what was assumed, the questions to ask, and a picture. Returns an `analysis_id`. |
| `packos_check_label_spec` | Check a described label before quoting: what PackOS still needs, what it assumed, what is not offered. |
| `packos_quote_label` | The official quote — from `spec` (a described label) **or** `analysis_id` (a label read from its artwork), never both. |
| `packos_get_quote` | Read a quote back by its id (`pq_…`), including whether it has expired. |
| `packos_save_quote` | Keep the quote in the person's PackOS account (My quotes on packos.ai). Needs sign-in. |
| `packos_start_order` | The link where the person orders on packos.ai. Needs sign-in. |
| `packos_request_specialist` | Hand a label quoting cannot price to a PackOS specialist, with the person's note. Needs sign-in. |

## How to quote

1. **If the person has the artwork, read it first** (`packos_read_label_artwork`). The file decides the size,
   the shape, the colours, the white and the effects; quoting from the file is more accurate than any
   description of it. Show the picture and say what was read.
2. **Ask only what PackOS asks.** `packos_quote_label` returns its own questions ("Ask the person: …"), so a
   separate `packos_check_label_spec` is optional. Ask those questions in plain words and offer the options they
   list. Do not guess an answer and do not fill a field the person did not state; leave it out and PackOS asks.
   - **Never guess a size.** "A 13-inch-wide label" has no height: ask for it. Only a round label (shape
     `circle`) has one dimension. A size given as W × H goes in as given; the copy position (which edge leaves
     the roll first) is among the assumptions to confirm.
   - **Thermal labels:** "thermal paper" is a *printing* answer, not a material: `direct-thermal` (no ribbon,
     e.g. desktop shipping printers) or `thermal-transfer` (with a ribbon). That choice picks the stock and its
     finish, so ask it first and leave material and finish out.
   - **"Gloss" or "matte" alone:** `gloss`, `matte` and `soft-touch` are laminates (a protective film);
     `gloss-varnish` and `matte-varnish` are coatings. Ask which, if the person did not say.
   - **Effects:** pass every effect the person asked for, including foil or emboss. PackOS answers those with a
     refusal; never drop one to get a price.
   - What PackOS *assumed* comes back as "Assumed, because the person did not say (confirm before they order)".
     Tell the person, and confirm before they order.
3. **Quote.** For artwork: `packos_quote_label { analysis_id, quantity, confirmations }`, where
   `confirmations` holds the person's answers (printing, material, finish, storage, copy position, roll size)
   and any correction to the size (only the side the person corrected) or the design count. Storage can change the
   stock (e.g. a beverage or cold-storage white): that is expected, do not change the material back.
   An artwork quote is often priced straight away on what PackOS assumed (material, finish, printing, storage,
   copy position): relay those and confirm them with the person before they order. Pass a confirmed value even
   when it equals the assumption (e.g. `copyPosition` when labels go on by hand, where it does not matter), so the
   quote stops listing it. Each re-quote is a new quote id that replaces the earlier one: save or order the latest. Colours, white, effects and shape come from the file; to
   change those, quote by `spec` instead. For a description: `packos_quote_label { spec, quantity }`.
   Quantities are 10,000 to 1,000,000 in steps of 1,000 (for a quantity between steps, quote the steps either
   side and say why); pass `quantities` (up to 6) for price breaks in one call, with `quantity` the one the
   person is most likely to order. The breaks come back in the summary, but only `quantity` gets a quote id: to
   save or order a break, quote that quantity on its own first.
4. **Repeat the summary exactly.** It states the unit price, the total, tooling, lead time, the price breaks
   asked for, and that prices are ex-works with freight and tax not included. The total is the price; the unit
   price is rounded to four places, so never multiply it back out or "correct" a total.
4b. **Several labels (multi-SKU).** Flavours or SKUs on the same size, material and finish are ONE quote: `designs`
   = how many artworks and `quantity` = the TOTAL across them (3 flavours × 10,000 = `designs: 3`, `quantity:
   30,000`). They print as one run; quoting them one by one prices separate runs and costs the person more. A
   label with a different size, material or finish is its own quote. Show each quote's summary; if you give an
   order total, say it is the sum of the quotes' totals.
5. **Give the "Open in PackOS" link exactly as returned**, as a link (e.g. `[Open in PackOS](…)`). Never shorten,
   rewrite or summarise it: one changed character breaks it.

**Numbers:** you may point at numbers PackOS returned ("the 50,000 break has the lowest price per label"). Never
calculate new ones: no savings, percentages, discounts, conversions or totals of your own.

## When PackOS will not price it online

A refusal is an answer, not an error: say why in PackOS's words (foil, a size wider than the press, an effect
priced by hand…). Offer two ways forward: change what was refused and quote again, or
`packos_request_specialist` with the person's own note and the `spec` as described (a refused label has no quote
id) — a specialist replies to the email on their account.

**Discounts and special requests:** you cannot change a price. If the person wants a better price or anything
quoting does not offer, offer `packos_request_specialist` with their note, without promising an outcome.
It sends a message to PackOS on the person's behalf: call it only after they say yes.

## Saving and ordering

Saving, ordering and the specialist hand-off ask the person to sign in to PackOS (the connector will prompt;
if a call says the person must sign in, ask them to, then try again). A new account must verify its email
address before a specialist request; if PackOS says so, tell the person to open the link PackOS emailed them.
An agent never places an order: `packos_start_order` returns the link where the person checks the quote and
the shipping address, accepts the terms and receives the payment link on packos.ai. Quotes are valid for 30
days; an expired quote must be quoted again.

If PackOS says it is busy, tell the person and try once more after the time it gives; never loop.

## What not to do

- Do not compare PackOS's price with other suppliers' or invent a discount.
- Do not promise a delivery date: lead time is in business days after proof approval, plus freight.
- Do not upload anything but the person's own label artwork.
- Labels only, on rolls. Pouches, cartons and sheets are not quoted online yet; say so and point to packos.ai.
