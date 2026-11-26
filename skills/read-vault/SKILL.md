---
name: read-vault
description: Look up existing packOS Vault workspaces, products, files, approvals and order status when a customer asks what is in their Vault, which artwork is current or what is waiting on them.
---

Use the hosted packOS connector. When Vault reads are available, start with `packos_list_workspaces`. Use the signed-in person's workspace and ask which company they mean if there is more than one plausible match.

Use `packos_search_vault` to find a record and `packos_get_vault_record` to open its returned reference in the same workspace. For a guest, open the folder reference returned with their workspace. Read the customer's own inbox with `packos_list_my_approvals`. Use `packos_get_order_status` with a Vault order ID or Calyx sales-order number. An order status request does not require quoting again.

Report the source status, artwork revision and proof state as returned. A current file can still be waiting on approval. If a search is partial, say which answer is incomplete. Use the supplied Vault link for follow-up. If the member's role cannot open the item, say access is unavailable. If discovery does not list the five tools, direct the customer to their Vault.
