---
id: K-0001
type: code-note
title: Refund totals are rounded in the invoice service, not the portal
status: proposed          # proposed | approved | replaced | stopped
scope: {product: payments, area: refunds}
confirmed_by:
source: sources/2026-11-11-finance-qa.md
review_by: 2027-03-01
---

# Refund totals are rounded in the invoice service, not the portal

**Note.** The portal sends refund amounts in cents. The invoice service rounds the tax portion. Do not round again in the portal.

**Where to look first.** The invoice service's refund calculation, then the portal's refund form.

**Status.** Proposed by an assistant. A tech lead must check the code and approve it before anything relies on it.

*This example is made up. Keep it as a guide, then delete it.*
