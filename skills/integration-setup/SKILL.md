---
name: integration-setup
description: Set up infrastructure for a PackOS customer or manufacturer, register ERP, EDI, prepress and file connections, and verify an artwork import from Google Drive, OneDrive or Dropbox.
---

Confirm the workspace displayed in PackOS and the administrator's intended systems. Use the connected PackOS tools and the host's authorized browser. Ask for non-secret system names and the identity of one approved test file. Keep credentials, provider sign-in and secret-manager entries in the administrator's session.

**Workspace directory.** Call `packos_prepare_system_connections` with up to eight systems. Open its review URL in the workspace and check the proposed labels, systems and permissions against the actual page. The batch registers read-only identities at the shadow tier. With the administrator's authorization, use **Register missing systems** once. Read each resulting directory row. An existing entry that differs, is paused or is ambiguous stays under review. After a timeout or partial result, reopen the same link and reconcile before continuing. If the page lacks batch review, report its availability. If the host lacks browser control, give the administrator the same review link.

**Cloud artwork intake.** Call `packos_prepare_artwork_import` for the chosen provider. In Vault, check Transfers for a previous attempt, the available providers, the selected workspace and the connected identity. Hand provider sign-in and consent to the administrator when needed. With approval to import the chosen test file, use the native picker, check the selection, start the job, and follow its per-file state. Report the job and resulting Vault file or version when shown. Report processing pending or provider unavailable exactly as observed. Folder sync and outbound delivery require their own purpose and consent.

**Manufacturer estimating.** For LabelTraxx use the manufacturer-setup skill. After enrollment call `packos_manufacturer_state` with `resume: true`. Use the returned next step and current connection generation. A queued import should be followed through its existing receipt. When checking a previously reviewed ticket, use its original company and reference.

Report each system's achieved milestone separately: directory identity, authorized vendor connection, verified first transfer, or confirmed ticket readback. If a tool is missing, name the unavailable workflow.
