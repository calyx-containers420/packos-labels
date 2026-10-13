# PackOS Labels for Claude

Official quotes for custom printed roll labels from [PackOS](https://packos.ai), inside Claude. Describe a
label or share its artwork (a PDF), and Claude asks only what PackOS needs, then returns the price PackOS's
estimating engine gives: price per label, total, the price-break table, one-time tooling and lead time. Save
the quote to your PackOS account, start an order on packos.ai, or hand a label that cannot be priced online
(foil, oversize, special effects) to a PackOS specialist.

## What it installs

- **The `packos` connector** — PackOS's remote MCP server at `https://mcp.packos.ai/mcp` (streamable HTTP).
- **The `quote-labels` skill** — how to use the connector well: read artwork first, ask only what PackOS asks,
  never recompute a price, and how to handle a label PackOS will not price online. It carries a label-buying
  guide (material, finish, white ink, storage, copy position, effects) so Claude can advise someone who has never
  specified a label, within the options PackOS really offers.
- **Slash skills**: `/quote`, `/quote-artwork` (in Claude Code it finds the PDF in your
  workspace and uploads it) and `/compare-labels` (Claude Code names them `/packos-labels:…`).

The connector also offers ready-made starters wherever MCP prompts show (the "+" menu in claude.ai, `/mcp__packos__…`
in Claude Code): Quote a label, Quote my label artwork, Compare price breaks, Quote several labels, Check a PackOS quote.

## What it sends, and to whom

Every request goes to PackOS (`mcp.packos.ai`, operated by Calyx Containers). Quoting needs no account: the
label details you describe, or the artwork file you share, are sent to PackOS to be read and priced. Artwork
is kept as an upload in PackOS so the quote can be reopened with its file. Saving a quote, starting an order
and asking a specialist require signing in to PackOS (OAuth); the specialist hand-off shares your account's
email with PackOS Sales so they can reply. The plugin runs nothing on your computer.

## Install

From the Claude plugin directory, or in Claude Code from this folder:

```
claude --plugin-dir ./packos-labels
```

On claude.ai or Claude Desktop, the connector can also be added on its own under Customize › Connectors with the
URL `https://mcp.packos.ai/mcp`.

Prices are ex-works, in US dollars, with freight and tax not included, valid for 30 days. The assistant never
places an order or takes payment: orders are checked and paid for by you on packos.ai.

## Privacy and support

- Privacy policy: https://packos.ai/privacy
- Terms: https://packos.ai/terms
- Support: https://packos.ai/contact

## License

The plugin's files are licensed under the Apache License 2.0 (see `LICENSE`). "PackOS" and its logo are
trademarks of Calyx Containers and are not licensed (see `NOTICE`). The PackOS service the connector reaches
is not part of this repository.
