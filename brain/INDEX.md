# Brain index

One row per entry. The AI reads this file first, filters by scope and status, and opens only matching approved entries. Keep it current: add a row when an entry is approved.

| id | title | type | scope | status | review_by |
|---|---|---|---|---|---|
| D-0001 | Customers on the legacy plan keep paper invoices until June 2027 | decision | product: billing, area: invoicing, client: legacy-plan | approved | 2027-02-12 |
| R-0001 | Wholesale refunds need a second approver | rule | product: payments, area: refunds, client: wholesale | approved | 2027-02-10 |
| C-0001 | Can a partial refund be issued after an invoice is closed? | clarification | product: payments, area: refunds | approved | 2027-03-01 |
| K-0001 | Refund totals are rounded in the invoice service, not the portal | code-note | product: payments, area: refunds | proposed | 2027-03-01 |

Status values: `proposed`, `approved`, `replaced`, `stopped`.
