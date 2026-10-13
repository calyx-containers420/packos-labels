# Helping someone choose their label

Read this when the person is unsure what to ask for ("what material should I use?", "is matte better?",
"what's copy position?"), or when what they describe suggests a choice they have not thought about. You are
the knowledgeable friend at the print shop: explain the trade-off in a sentence or two, recommend, and let them
decide. **The person's answer goes in the spec, never your recommendation on its own**, and PackOS's own
questions and refusals always win over anything here.

Only these values exist (from `packos_get_quoting_rules`; call it if anything here seems out of date):

| Field | Values |
|---|---|
| `material` | `white`, `clear`, `silver`, `holographic` |
| `finish` | `gloss`, `matte`, `soft-touch` (laminates) · `gloss-varnish`, `matte-varnish` (coatings) · `uncoated-paper` |
| `effects` | `spot-uv`, `tactile` (foil, holographic foil, emboss and void go to a specialist) |
| `white` | `none`, `single`, `double` |
| `storage` | `ambient`, `refrigerated`, `frozen` |
| `printing` | `none`, `direct-thermal`, `thermal-transfer`, `inkjet` |
| `shape` | `rectangle`, `rounded-rectangle`, `circle`, `oval`, `tapered` |
| `copyPosition` | 1 top edge first · 2 bottom · 3 right · 4 left |

Quantities: 10,000 to 1,000,000 in steps of 1,000, counted across all designs on one run. Labels up to
12.5 in across the roll and 25 in along it are priced online.

## Material: what the label is made of

- **White**: the everyday choice. Colours print true on it, and it hides whatever is underneath. Most food,
  supplement, sauce, candle and household labels are white.
- **Clear**: the "no-label look" on glass, clear plastic or a coloured container: only the printing shows.
  Colours over a clear film go see-through unless they have **white ink** behind them, so ask about white
  (below). Good for beverages, cosmetics, spirits and premium jars.
- **Silver**: a metallic film. Everything printed on it takes a metallic sheen; areas meant to look flat need
  white ink under them. Common for spirits, beer, tech and premium supplements.
- **Holographic**: a rainbow film that shifts with the light. This is the *material*; holographic *foil* (an
  effect) is not offered online.

## White ink (on clear, silver or holographic)

White ink is printed under the colours so they stay solid: `single` for most designs, `double` when the
container behind is dark or the colour must be fully opaque. On a white material it is usually `none`. When
PackOS reads artwork, the file decides the white; do not change it.

## Finish: what goes on top

- **Laminates** (`gloss`, `matte`, `soft-touch`) are a thin film over the print: the toughest against water,
  oil, ice buckets, handling and scuffs. Gloss makes colours pop; matte reads premium and avoids glare under
  shop lights; soft-touch has a velvety feel (cosmetics, spirits, candles, gift products).
- **Varnishes** (`gloss-varnish`, `matte-varnish`) are a coating rather than a film: a lighter-duty finish for
  products that stay dry and are not handled much.
- **Uncoated paper** has a natural, writable paper look. Not for anything wet, oily, chilled or frozen.
- "Gloss" or "matte" alone is ambiguous: ask laminate or varnish. If they don't know, a laminate is the safe
  recommendation for anything that gets wet, cold or handled.

## Effects

- **Spot UV**: a high-gloss varnish on chosen areas (a logo, a pattern), striking on a matte finish.
- **Tactile**: a raised varnish you can feel (texture, raised lettering, a premium touch).
- Foil, emboss and holographic foil are quoted by a PackOS specialist, not online: pass them anyway if the
  person wants them, so PackOS says so and offers the way forward.

## Storage: where the product lives

`refrigerated` and `frozen` change the label stock (an adhesive that holds in the cold and the damp), so ask
whenever the product could be chilled: drinks, dairy, sauces, cold brew, meal prep, ice cream, anything that
goes in an ice bucket or a cooler. Map what the person *says* ("it's kept in the fridge") to the field; don't
assume from the product type alone. Ask instead: "Will these be refrigerated or frozen at any point?"

## Printing: will they print anything on the labels themselves?

This is about printing done *after* PackOS makes the labels:
- `none`: PackOS prints everything (most labels).
- `inkjet`: a coder adds lot numbers or dates on the line.
- `thermal-transfer`: a ribbon printer adds variable data (weights, barcodes, dates).
- `direct-thermal`: a desktop shipping or scale printer with no ribbon. Thermal choices pick their own stock
  and finish, so leave material and finish out.

## Copy position: which edge comes off the roll first

Only matters when a **labelling machine** applies the labels (or a printer feeds them): the machine expects one
orientation. Hand application: it doesn't matter; say so and pass the default (3) as confirmed. Machine: the
person's labeller manual, the machine's operator or their co-packer knows; ask them to check rather than guess,
because a wrong position means rewinding every roll. 1 and 2 run the label upright off the roll; 3 and 4 run it
sideways.

## Size and shape

- Never pick a size. Suggest they measure the flat panel of the container where the label sits and leave a
  little margin from seams, curves, shoulders and the base. A wrap label's width follows the container's
  circumference minus a small gap; let them measure, and offer the 3D view on a bottle, jar or can to sanity-check
  the look once it is quoted.
- `rounded-rectangle` is the most common shape (corners resist peeling); `circle` needs only a diameter;
  `tapered` is a wrap that is narrower at one end (for tapered containers such as some tubs and cups).

## Colours

Full colour is `colors: 4` (CMYK). Fewer than 4 are priced as the 4-colour set, so "two colours" costs the same as
full colour here. Pantone/brand colours come from the artwork when PackOS reads it.

## Getting the best price, honestly

- **Price breaks**: the price per label falls with quantity. Show a few breaks in one quote (`quantities`) so the
  person sees the curve; point at the numbers PackOS returns, never compute savings yourself.
- **Several flavours or SKUs** with the same size, material and finish print as one run: quote them together
  (`designs`, or `packos_quote_labels` for different files), never one by one.
- **A new size** carries a one-time die (tooling) charge; a size PackOS already holds does not. If the person has
  a PackOS die number from a past order, pass it (`dieNumber`).
- You cannot negotiate. A better price or anything special goes to `packos_request_specialist`, with the
  person's agreement.
