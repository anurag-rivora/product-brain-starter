# Inbox

Proposals from the AI land here. Nothing in this folder counts until a named person approves it.

## How a proposal lands

1. A transcript or note goes into `sources/`.
2. The `capture` skill reads it with `brain/INDEX.md` and writes one file per proposed entry here, named like `D-0002-short-title.md`.
3. Each proposal has `status: proposed` and a `proposed_on` date, quotes the line it came from, suggests a scope and a confirmer, and says which approved entry it would contradict or replace.

## How a proposal gets approved

1. The suggested confirmer opens the file and edits it: fix the wording, the scope and the review date.
2. They fill in `confirmed_by` (or `owner` for rules) and `confirmed_on`, and set `status: approved`.
3. They move the file to its folder (`brain/decisions/`, `brain/rules/`, `brain/clarifications/` or `brain/code-notes/`) and add a row to `brain/INDEX.md`.
4. If it replaces an earlier entry, they set the old one to `replaced` and fill in `supersedes` on the new one.

A pull request review works well for this, with CODEOWNERS mapping each area to its confirmers.

A proposal nobody has touched in 14 days is reported by `brain-health`. Approve it, change it or delete it.
