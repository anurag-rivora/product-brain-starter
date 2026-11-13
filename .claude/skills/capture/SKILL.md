---
name: capture
description: Turn a transcript or note in sources/ into proposed brain entries (decisions, rules, clarifications, code notes) written to brain/inbox/. Use when someone says "capture this", "file this call", or points at a new file in sources/. Never approves anything.
---

# Capture

Turns a source into proposals. A person approves them later.

## Steps

1. Confirm the source file is in `sources/`. If not, ask the person to put it there first.
2. Read `AGENTS.md` and `brain/INDEX.md`. Do not open other entries unless step 5 needs them.
3. Read the source. Find statements that are decisions, rules, answers to questions, or facts about the code. Skip opinions, chatter and anything still undecided.
4. For each one, write a file in `brain/inbox/` named `<D|R|C|K>-<next number>-<short-title>.md`, using the front matter in the example entries. Always set:
   - `status: proposed` and `proposed_on` (today's date). Never `approved`.
   - `scope` as narrow as the source supports (product, area, client). Do not use "all" unless the source clearly says it applies to everything.
   - `source` pointing to the file.
   - A suggested confirmer in the body: a role or a named person who owns this area.
   - The exact line quoted from the source.
5. Check each proposal against `INDEX.md`. If an approved entry in the same scope would be contradicted or replaced, open that entry and note it in the proposal: "Would replace D-00NN" or "Conflicts with R-00NN".
6. If the source leaves a question open, add a row to `brain/open-questions.md` with an owner role and whether it blocks.
7. Report: how many proposals, their IDs, who should confirm each, any conflicts, any new open questions. Remind the person that nothing counts until they approve it.

## Do not

- Set `status: approved`, fill in `confirmed_by` or `confirmed_on`, or move files out of the inbox.
- Invent a source line. If you cannot quote one, do not propose the entry.
- Edit the source.
