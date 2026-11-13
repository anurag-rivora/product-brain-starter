---
name: write-handoff
description: Build features/<slug>/handoff.md for a coding agent from approved steps and approved brain entries only. Use when someone says "write the handoff" or "hand this to the coding agent".
---

# Write handoff

Builds a frozen bundle from approved work. Drafts are left out.

## How to run it

1. Ask which feature (`features/<slug>/`). Read `brief.md` and its steps table.
2. List the steps marked `approved` and the steps marked `not needed` (with reasons). If the implementation plan (08) is not approved, stop and say so.
3. Read only the approved steps. Ignore any step marked draft or not started.
4. Collect the entry IDs those steps cite. Open each one in `brain/` and keep only entries with `status: approved`. If a cited entry is now `replaced` or `stopped`, stop and tell the person.
5. Write `features/<slug>/handoff.md` using `features/_template/handoff.md`:
   - Objective: two sentences, from the approved executive summary (01).
   - Plan: from the approved plan, in order, with where to look first.
   - Rules that apply: each approved rule in full, with ID and severity.
   - Decisions that apply: ID plus one line each.
   - Open questions: id, question, blocking level and owner. Blocking ones go first.
   - Steps not needed, with reasons.
   - End with "Stop and ask if unsure".
6. Add the date and the list of approved steps used at the top.
7. Tell the person where the file is, and which steps and entries went in. Remind them the PR template asks which entries the change touched.

## Do not

- Include draft steps, proposed entries or anything in `brain/inbox/`.
- Summarise a rule. Rules go in full.
- Send stories to a tracker. That needs a person's OK.
