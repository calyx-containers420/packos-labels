---
name: manufacturer-setup
description: Connect a manufacturer's own LabelTraxx shop to PackOS, prepare its estimating-engine margins, and rehearse a test label quote through a reviewed ticket.
---

Use the PackOS connector's manufacturer tools for this workflow. Start with packos_open_manufacturer_setup. If the manufacturer tools are absent, report that the connected gateway has not enabled this feature.

1. Confirm the manufacturer's Vault workspace. In the authorized browser, open the returned Connections link, help fill the shop and reserved-range fields, and hand the private credential entry and shop confirmation to the administrator. Never ask for a credential in chat. Use the Customers link to map an existing customer, ship-to and LT product.
2. Call packos_manufacturer_state and packos_manufacturer_mappings. Use only this shop's returned identifiers. Check the sync date and current draft. Ask which margin schedule the plant authorizes. Show the change, then use packos_save_manufacturer_pricing_draft. Publishing is a separate owner/admin action on the Pricing page.
3. Select a mapped reorder SKU. Confirm the actual label dimensions, material, finish, colour count, quantity and ship-by date. Call packos_test_manufacturer_ticket with the chosen connection, customer, schedule and a stable reference. Use the engine's returned price and ticket draft. Missing rates, mappings and exhausted ranges must be resolved in PackOS before retrying.
4. Open the returned review link in the manufacturer's own session. The authorized plant reviewer checks the exact shop, goods, tooling, quantity and ticket, and decides whether to submit. Even a marked TEST ticket can reach a live shop. Hand control to the reviewer for the final decision. On a host without browser control, provide the same link.
5. Call packos_manufacturer_ticket_receipt with the original workspace, customer and reference. Report the actual writer state and external ID. A queued or shadowed run is still unverified. An ambiguous response calls for checking the same run before any retry.
