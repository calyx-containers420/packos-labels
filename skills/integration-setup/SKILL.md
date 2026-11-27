---
name: integration-setup
description: Set up infrastructure for a PackOS customer or manufacturer, register ERP, EDI, prepress and file connections, compare ERP customer and SKU identifiers, and verify individual artwork imports or recurring folders from Google Drive, OneDrive or Dropbox.
---

Confirm the workspace displayed in PackOS and the administrator's intended systems. Use the connected PackOS tools and the host's authorized browser. Ask for non-secret system names and the identity of one approved test file. Keep credentials, provider sign-in and secret-manager entries in the administrator's session.

**Workspace directory.** Call `packos_prepare_system_connections` with up to eight systems. Open its review URL in the workspace and check the proposed labels, systems and permissions against the actual page. The batch registers read-only identities at the shadow tier. With the administrator's authorization, use **Register missing systems** once. Read each resulting directory row. An existing entry that differs, is paused or is ambiguous stays under review. After a timeout or partial result, reopen the same link and reconcile before continuing. If the page lacks batch review, report its availability. If the host lacks browser control, give the administrator the same review link.

**Cloud artwork intake.** Call `packos_prepare_artwork_import` for the chosen provider. In Vault, check Transfers for a previous attempt, the available providers, the selected workspace and the connected identity. Hand provider sign-in and consent to the administrator when needed. With approval to import the chosen test file, use the native picker, check the selection, start the job, and follow its per-file state. Report the job and resulting Vault file or version when shown. Report processing pending or provider unavailable exactly as observed. Folder sync and outbound delivery require their own purpose and consent.

**Recurring artwork folders.** Use `packos_prepare_artwork_folder` when available. If the tool is absent, open **Connected folders** from **Add files** in the signed-in PackOS workspace. Confirm the workspace, chosen provider, account and exact source folder. Check **Your folders** for a matching recurring connection before creating one. A completed one-time folder copy still needs a separate recurring connection. If the provider is available and the admin wants this folder watched, let them handle the private consent screen and review its actual permission scope. Use their authorized browser session to select the folder and start the recurring check. If folder sync is unavailable, report the status shown.

For an interrupted check, reopen its report with the original folder ID and generation if available. Read Activity, Saved copies and Report. For a revision test, follow one approved source file that the admin has updated and match the new revision with the saved Vault version. Leave an overwrite or conflict resolution to the administrator. Report the actual result, including any pending check or missing Vault version.

**ERP customer and SKU preview.** Ask the manufacturer to identify an approved export sample, its LabelTraxx customer-number column, its PackOS SKU column, and optionally its expected LabelTraxx product-number column. An ERP's own account ID can differ from its LabelTraxx customer number. Use the private host file tools to extract only these identifiers. When local execution is available, run the bundled Python 3 helper with the approved file and the exact column labels, for example:

```sh
python3 scripts/prepare_erp_sample.py export.csv --customer-column "LT Customer" --sku-column "PackOS SKU" --product-column "LT Product"
```

The path is relative to this skill's directory. The helper prints the `sample` argument, reading up to 100 CSV records. Keep SKU case and product-number leading zeroes. Check tool discovery for the `sample` argument on `packos_manufacturer_mappings`. Call it with the confirmed manufacturer workspace and the extracted sample. Report the matched count and the one-based record numbers and reasons that need review. A duplicate check covers the supplied sample. Confirm the result has `state: mapping_preview` before reporting a comparison. If the gateway lacks this capability, report that only sample preparation is available. Only a separately authorized mapping change or quote rehearsal should cause a write.

**Manufacturer estimating.** For LabelTraxx use the manufacturer-setup skill. After enrollment call `packos_manufacturer_state` with `resume: true`. Use the returned next step and current connection generation. A queued import should be followed through its existing receipt. When checking a previously reviewed ticket, use its original company and reference.

Report each system's achieved milestone separately: directory identity, authorized vendor connection, verified first transfer, or confirmed ticket readback. If a tool is missing, name the unavailable workflow.
