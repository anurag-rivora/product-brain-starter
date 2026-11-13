---
id: R-0001
type: rule
title: Wholesale refunds need a second approver
severity: must            # must | should | advisory
status: approved          # proposed | approved | replaced | stopped
scope: {product: payments, area: refunds, client: wholesale}
owner: "Payments lead"
confirmed_on: 2026-11-10
source: sources/2026-11-10-refunds-review.md
supersedes:
review_by: 2027-02-10
---

# Wholesale refunds need a second approver

**Rule.** A refund for a wholesale customer cannot be completed until a second person, different from the requester, approves it.

**Applies to.** Every refund path for wholesale customers: portal, support tool and any bulk refund.

**Why.** Wholesale refunds are large and were the source of two reversal errors last quarter.

**Source line.** "Anything over the wholesale threshold needs a second pair of eyes." (sources/2026-11-10-refunds-review.md)

*This example is made up. Keep it as a guide, then delete it.*
