---
name: read-vault
description: Upload artwork revisions, file them in folders, request artwork reviews, and organize packOS Vault folders and look up production specifications, folder activity, approvals and order status when a customer asks what is in their Vault, which artwork is current or what is waiting on them.
---

Use the hosted packOS connector. When Vault reads are available, start with `packos_list_workspaces`. Use the signed-in person's workspace and ask which company they mean if there is more than one plausible match.

Use `packos_search_vault` to find a record and `packos_get_vault_record` to open its returned reference in the same workspace. For a guest, open the folder reference returned with their workspace. Read the customer's own inbox with `packos_list_my_approvals`. Use `packos_get_order_status` with a Vault order ID or Calyx sales-order number. An order status request does not require quoting again.

Report the source status, artwork revision and proof state as returned. A current file can still be waiting on approval. If a search is partial, say which answer is incomplete. Use the supplied Vault link for follow-up. If the member's role cannot open the item, say access is unavailable. Use the tools advertised by the connected gateway.

For a launch folder, use `packos_list_vault_folders` to resolve its workspace, parent and exact name. Use `packos_create_vault_folder` with one request ID per intended creation and reuse it on a retry. Use `packos_rename_vault_folder` with the current name you read. If the name changed, refresh and tell the customer before trying another edit. Folder writes need separate consent and the appropriate Vault role. Give the customer the resulting folder link.

Use `packos_get_folder_activity` to answer who changed a folder, and follow the returned cursor for older events. Use `packos_get_product_specification` for a SKU’s production values and their sources. Identify conflicting fields and pending reviews in the answer.

For a revision, open the product and use its SKU, asset ID and current version ID with `packos_prepare_artwork_revision`. Give the customer the returned upload page for their PDF or PDF-compatible Illustrator file. After they finish there, call `packos_upload_artwork_revision` with the ticket. Report the saved version number. If Vault says the current revision changed, read it again and ask which version the customer intends to replace.

Use `packos_file_vault_artwork` with the destination folder ID. Filing includes version history and makes the artwork visible to people with folder access. For a review, read the current product record, match the requested person against its eligible reviewers, and use `packos_request_artwork_review` with that reviewer ID and the current version ID. Report the recipient and request ID.
