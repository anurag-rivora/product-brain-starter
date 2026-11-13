---
name: brain-health
description: Check the health of the product brain and print a short report. Use for the weekly or monthly review, or when someone says "how healthy is the brain" or "run brain health".
---

# Brain health

## Steps

1. Run `python scripts/brain_health.py` from the repo root. If Python is not available, do the checks by hand from the front matter.
2. The six checks:
   1. Open questions and how long each has waited.
   2. Entries with no confirmer or owner.
   3. Approved entries past `review_by`, or confirmed more than 90 days ago.
   4. Replaced or stopped entries still cited elsewhere in the repo.
   5. Inbox proposals older than 14 days.
   6. Entries scoped to "all".
3. Print a short report: one line per check with the count, then the IDs behind any non-zero count and one suggested action each.
4. Do not fix anything. Do not approve, move or delete entries. A person decides.

## Suggested actions

- Open questions: assign an owner and a date.
- No confirmer or owner: ask the area owner to confirm or stop the entry.
- Past review: the owner re-confirms, replaces or stops it.
- Cited but replaced or stopped: update the citing file to the current entry.
- Old proposals: approve, change or delete.
- Scoped to "all": narrow the scope, unless it truly applies everywhere.
