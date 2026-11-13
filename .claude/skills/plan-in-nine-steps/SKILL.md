---
name: plan-in-nine-steps
description: Plan a feature in nine steps using the checklists in steps/, starting with a five-line executive summary and ending with the delivery backlog. Loads only the brief and approved in-scope brain entries, drafts one step at a time, and stops for a person to approve each. Use when someone says "plan this feature", "plan in nine steps" or "draft the next step".
---

# Plan in nine steps

One step at a time. Each step reads only approved earlier steps. Start with a five-line summary, and rewrite it at the end.

## How to run it

1. Ask which feature (`features/<slug>/`). If it does not exist, copy `features/_template/` and ask the person to fill in `brief.md`.
2. Read `AGENTS.md`, `features/<slug>/brief.md` and `brain/INDEX.md`. Work out the scope from the brief.
3. Open only entries that are `status: approved` and whose scope matches. Read rules with severity `must` first. Ignore proposed entries.
4. Pick the next step in this order: 01 executive summary (first pass), 02 intent, 03 impact, 04 UX, 05 backend, 06 system impact, 07 data, 08 plan, 09 backlog, then 01 executive summary again (final pass). Skip a step marked not needed.
5. Check that every earlier step this one reads has been approved in the brief's steps table. If not, stop and say which one is missing.
6. Open `steps/<step>.md` and work through its checklist. Read the approved earlier steps it names. Do not read drafts.
7. Write the step to `features/<slug>/<step>.md`. In it:
   - Cite entry IDs for everything you rely on.
   - Label each assumption with a confidence and what would disprove it.
   - List sources.
   - Say "to be confirmed" instead of guessing.
8. List questions in `features/<slug>/questions.md` with an owner role and a blocking level. If a blocking question is open, stop here and ask.
9. Set the step to `draft` in the brief and ask the person to review and approve it. Only a person changes it to `approved` and fills in approver and date.
10. When answers arrive, run the `capture` skill so the answers worth keeping are saved with a scope.

## Do not

- Start the next step before the person approves this one.
- Treat a draft step or proposed entry as fact.
- Invent file paths, module names or endpoints.
