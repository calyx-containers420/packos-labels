---
name: quote-labels
description: Get official PackOS quotes for custom printed roll labels (product labels, stickers on a roll), from a description or from the label artwork (PDF), help the person choose material, finish and effects, and save or order it on packos.ai. Use when someone asks what labels or roll stickers cost, wants a label quote, price breaks or lead time, compares label options, shares label artwork to be priced, or mentions a PackOS quote id (pq_…).
---

# Quoting roll labels with PackOS

PackOS prices custom printed labels on rolls. Every price comes from the PackOS estimating engine through the
`packos` connector. **Never estimate, round, convert or recompute a price** — repeat the summary sentence a
quote returns, word for word, and show the numbers it returns as they are.

## Be the expert in the room

Most people buying labels have never specified one. Lead them: one short message at a time, in plain words,
with a recommendation when they are unsure and the reason in a sentence. **When the person is unsure what to
choose (material, finish, white, storage, copy position, effects, size), read
[references/label-guide.md](references/label-guide.md)** and advise from it. Advice is yours; the spec carries
only what the person agreed to, and every price is PackOS's.

Keep the conversation moving toward a price: as soon as PackOS has enough, quote, then refine. A quote on
PackOS's assumptions, clearly listed, beats a questionnaire.

## The tools

| Tool | Use it to |
|---|---|
| `packos_get_quoting_rules` | Learn what is quoted online: sizes, materials, finishes, effects, quantity rules, lead time, terms. Call it first if unsure. |
| `packos_get_artwork_upload_link` | A one-file link to send the person's label PDF to PackOS (you cannot attach a file to a tool call). |
| `packos_read_label_artwork` | Read the person's label PDF: size, shape, colours, white, effects, what was assumed, the questions to ask, and a picture. Returns an `analysis_id`. |
| `packos_check_label_spec` | Check a described label before quoting: what PackOS still needs, what it assumed, what is not offered. |
| `packos_quote_label` | The official quote — from `spec` (a described label) **or** `analysis_id` (a label read from its artwork), never both. |
| `packos_quote_labels` | Several labels on one order (flavours, SKUs, sizes): PackOS groups the ones that print together and returns each run's quote and the order total. |
| `packos_view_label_3d` | Show a quoted label in 3D (on its roll, flat, or on a bottle, jar or can), from a quote id or an artwork analysis id. |
| `packos_get_quote` | Read a quote back by its id (`pq_…`), including whether it has expired. |
| `packos_save_quote` | Keep the quote in the person's PackOS account (My quotes on packos.ai). Needs sign-in. |
| `packos_start_order` | The link where the person orders on packos.ai. Needs sign-in. |
| `packos_request_specialist` | Hand a label quoting cannot price to a PackOS specialist, with the person's note. Needs sign-in. |

## How to quote

1. **If the person has the artwork, read it first** (`packos_read_label_artwork`). The file decides the size,
   the shape, the colours, the white and the effects; quoting from the file is more accurate than any
   description of it. Show the picture and say what was read.
   - **Getting the file to PackOS.** As soon as the person mentions their artwork, call
     `packos_get_artwork_upload_link`; do not ask them to attach it to the chat first: a file attached to the
     conversation never reaches a tool. Never paste a PDF as base64: a label file is megabytes. Then:
     - if you can run shell commands (Cowork, Claude Code), look for the file yourself first: a path the person
       gave, or label-looking PDFs / `.ai` files in the workspace (`find . -maxdepth 3 -iname '*.pdf' -o -iname '*.ai'`).
       One clear match: run the `curl` command the link returns with that path. Several: ask which (list them).
       None: ask for the path;
     - otherwise, or if that command cannot reach packos.ai, give the person the page link exactly as returned (the
       card shows it as a button, with "It's uploaded" for when they are done) and end your turn until they say the
       file is uploaded.
     Then call `packos_read_label_artwork` with `file: { upload_id }` (it waits a few seconds for a file still on
     its way). If it says the file has not arrived, tell the person once and end your turn; do not call it again
     until they say it is uploaded. Never invent a link or read the file yourself instead.
   - Do not quote from your own reading of the artwork, even when you can open it: only PackOS's read sees the
     plates, the white and the effects the press prints. Do not state a size, colours or anything else about the
     file before PackOS has read it; say only that you are sending it to PackOS.
2. **Ask only what PackOS asks.** `packos_quote_label` returns its own questions ("Ask the person: …"), so a
   separate `packos_check_label_spec` is optional. Ask those questions in plain words, **all in one message**,
   and offer the options they list (with your recommendation when the person seems unsure). Where the quote card
   shows them as buttons, a one-line nudge is enough. Do not guess an answer and do not fill a field the person
   did not state; leave it out and PackOS asks.
   - **Use what the person already said.** A plain statement is an answer: "it's kept in the fridge" →
     `storage: refrigerated`; "we put them on by hand" → `copyPosition` does not matter (pass 3, confirmed);
     "full colour" → `colors: 4`; "on clear bottles, no-label look" → `material: clear`. A product type alone
     ("cold brew", "candles") is a reason to ask, not an answer.
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
   person is most likely to order. **Show the curve unasked:** when the person names one quantity, pass it as
   `quantity` and in `quantities` with two larger steps (e.g. 10,000 → `[10000, 25000, 50000]`; 50,000 →
   `[50000, 100000, 250000]`), so they see where the price per label drops without asking again. When they gave
   no quantity, quote `[10000, 25000, 50000]` with `quantity: 10000` and say these are starting points. The breaks come back in the summary, but only `quantity` gets a quote id: to
   save or order a break, quote that quantity on its own first.
4. **Repeat the summary exactly, in your reply.** Even when a PackOS card shows the quote, write the summary
   sentence yourself: the card can be collapsed or not shown at all, and "the quote is above" leaves the person
   with no price. The summary states the unit price, the total, tooling, lead time, the price breaks
   asked for, and that prices are ex-works with freight and tax not included. The total is the price; the unit
   price is rounded to four places, so never multiply it back out or "correct" a total.
4b. **Several labels (multi-SKU): one `packos_quote_labels` call**, a line per artwork with its own quantity
   (2–12 lines). PackOS groups the lines that print together (same size, material and finish) into one run, the
   way packos.ai prices a basket: never quote flavours one by one (separate runs cost more, and a flavour under
   10,000 would be refused on its own when it is fine with its siblings). Repeat the summary it returns; it
   already carries the order total.
4c. **Comparing options** ("gloss or matte?", "white or clear?"): one quote per option PackOS can price, then
   PackOS's numbers side by side in a short table with a one-line take on each trade-off (from the label guide).
   Point at the numbers; never compute the difference.
5. **Offer to show it in 3D** once it is quoted (`packos_view_label_3d` with the quote id, or the analysis id for
   artwork): PackOS draws the label on its roll, and the person can switch to flat, bottle, jar or can and turn it.
   Say what is shown (artwork, or stock and finish only for a label quoted from words); never describe colours or
   finishes the card has not been given.
6. **Give the "Open in PackOS" link exactly as returned**, as a link (e.g. `[Open in PackOS](…)`). Never shorten,
   rewrite or summarise it: one changed character breaks it.
7. **End with the next step, in one line**: the assumptions to confirm (if any), then what they can do now:
   change something and re-quote, see it in 3D, save it, or order it on packos.ai. One question, not a menu of
   five.

**A returning person** who gives a quote id (`pq_…`): `packos_get_quote` first. If it has expired, say so and
offer to quote the same label again (same spec or artwork, same quantity); prices can change.

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
