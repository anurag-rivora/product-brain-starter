# Product brain: always-loaded instructions

Fill in every section marked FILL IN. Keep this file short enough to read in two minutes. It is loaded on every turn, and the more instructions a model is given at once, the more it misses.

## The product in five lines

- FILL IN: what the product is. Example: A billing portal where small businesses pay invoices and request refunds.
- FILL IN: who uses it. Example: Account owners, finance staff and our support team.
- FILL IN: what matters most this quarter. Example: Fewer refund disputes.
- FILL IN: the main systems it touches. Example: Payments provider, invoice service, customer email.
- FILL IN: where the code lives. Example: github.com/your-team/billing-portal.

## Glossary

| Term | Meaning |
|---|---|
| FILL IN | Example: "Wholesale" means a customer on a trade agreement with volume pricing. |
| FILL IN | Example: "Credit note" means a document that reduces an invoice after issue. |

## Must-follow rules that apply everywhere

Only rules with no exceptions by area belong here. Area rules go in `brain/rules/`.

1. FILL IN. Example: Never show full card numbers in any screen, log or message.
2. FILL IN. Example: Amounts are stored in cents and shown in the customer's currency.
3. FILL IN. Example: Anything that moves money needs an audit log entry.

## Protocol

1. Read `brain/INDEX.md` first.
2. Open only entries with `status: approved` whose scope matches the area you are working on. Do not open the rest.
3. Treat `status: proposed` entries and anything in `brain/inbox/` as undecided. Never present them as fact.
4. Cite entry IDs (for example D-0001, R-0001) wherever you rely on them.
5. Label every assumption as an assumption, with your confidence and what would disprove it.
6. Ask rather than assume. If a question blocks the work, stop and ask.
7. Never set `status: approved` yourself. Only a named person does that. Write proposals to `brain/inbox/`.
8. Open files in `sources/` only to check a claim an entry makes. Never load them whole.
9. If an entry looks out of date or conflicts with another, say so. Do not pick one quietly.
10. To plan a feature, follow the nine planning steps in `steps/`, one at a time, starting with the executive summary.
