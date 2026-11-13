#!/usr/bin/env python3
"""Print a short health report for the product brain.

Standard library only. Run from the repo root:

    python scripts/brain_health.py
    python scripts/brain_health.py --today 2026-12-01
    python scripts/brain_health.py --strict    (exit 1 if anything is flagged)

It reads the front matter of files under brain/. It never changes a file.
"""

import argparse
import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRAIN = ROOT / "brain"
ENTRY_DIRS = ["decisions", "rules", "clarifications", "code-notes"]
SKIP_DIRS = {".git", "node_modules", "__pycache__"}
TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".example", ".txt"}
FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.S)


def parse_front_matter(text):
    """Read simple 'key: value' lines. Nested values stay as plain text."""
    match = FRONT_MATTER.match(text)
    if not match:
        return {}
    data = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line[0] in " \t#" or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value[:1] not in ('"', "'") and " #" in value:
            value = value.split(" #", 1)[0].strip()
        data[key.strip()] = value.strip("\"'")
    return data


def parse_date(value):
    try:
        return datetime.strptime((value or "").strip()[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def rel(path):
    return path.relative_to(ROOT).as_posix()


def load_entries():
    entries = []
    for folder in ENTRY_DIRS:
        for path in sorted((BRAIN / folder).rglob("*.md")):
            if path.name.lower() == "readme.md":
                continue
            meta = parse_front_matter(path.read_text(encoding="utf-8"))
            if meta.get("id"):
                meta["_path"] = path
                entries.append(meta)
    return entries


def open_question_rows():
    """Rows from brain/open-questions.md whose status is not answered or closed."""
    path = BRAIN / "open-questions.md"
    rows = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 6 or not re.match(r"^Q-\d+", cells[0]):
            continue
        if cells[5].lower() in ("answered", "closed"):
            continue
        rows.append({"id": cells[0], "raised_on": parse_date(cells[4]), "blocking": cells[3]})
    return rows


def inbox_proposals():
    folder = BRAIN / "inbox"
    found = []
    if not folder.exists():
        return found
    for path in sorted(folder.glob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        meta = parse_front_matter(path.read_text(encoding="utf-8"))
        proposed = parse_date(meta.get("proposed_on"))
        if proposed is None:
            proposed = datetime.fromtimestamp(path.stat().st_mtime).date()
        found.append((path.stem, proposed))
    return found


def repo_text_files():
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in TEXT_SUFFIXES:
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        yield path


def still_cited(entry):
    """Files that mention a replaced or stopped entry (its own file and the index excluded)."""
    pattern = re.compile(r"\b" + re.escape(entry["id"]) + r"\b")
    hits = []
    for path in repo_text_files():
        if path == entry["_path"] or path == BRAIN / "INDEX.md":
            continue
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.lstrip().startswith("supersedes:"):
                continue
            if pattern.search(line):
                hits.append(rel(path))
                break
    return hits


def scoped_to_all(entry):
    scope = entry.get("scope", "").lower()
    return scope == "all" or re.search(r"[:\s,{]all\s*[,}]|^\{?\s*all\s*\}?$", scope) is not None


def main():
    parser = argparse.ArgumentParser(description="Product brain health report")
    parser.add_argument("--today", help="Override today's date (YYYY-MM-DD)")
    parser.add_argument("--strict", action="store_true", help="Exit 1 if anything is flagged")
    args = parser.parse_args()
    today = parse_date(args.today) if args.today else date.today()
    if today is None:
        sys.exit("Bad --today value. Use YYYY-MM-DD.")

    entries = load_entries()
    approved = [e for e in entries if e.get("status") == "approved"]

    # 1. Open questions and their age
    questions = []
    for row in open_question_rows():
        age = (today - row["raised_on"]).days if row["raised_on"] else None
        questions.append((row["id"], age, row["blocking"]))
    for e in entries:
        if e.get("type") == "clarification" and (e.get("status") == "proposed" or not e.get("answer")):
            asked = parse_date(e.get("asked_on"))
            questions.append((e["id"], (today - asked).days if asked else None, e.get("blocking", "")))

    # 2. Approved entries with no confirmer or owner
    no_person = [e["id"] for e in approved if not e.get("confirmed_by") and not e.get("owner")]

    # 3. Approved entries past review_by, or older than 90 days
    stale = []
    for e in approved:
        review_by = parse_date(e.get("review_by"))
        confirmed = parse_date(e.get("confirmed_on"))
        if review_by and review_by < today:
            stale.append((e["id"], "past review_by " + review_by.isoformat()))
        elif confirmed and (today - confirmed).days > 90:
            stale.append((e["id"], "confirmed %d days ago" % (today - confirmed).days))

    # 4. Replaced or stopped entries still cited elsewhere
    cited = []
    for e in entries:
        if e.get("status") in ("replaced", "stopped"):
            hits = still_cited(e)
            if hits:
                cited.append((e["id"], hits))

    # 5. Inbox proposals older than 14 days
    old_proposals = [(name, (today - d).days) for name, d in inbox_proposals() if (today - d).days > 14]

    # 6. Entries scoped to "all"
    all_scope = [e["id"] for e in entries if scoped_to_all(e)]

    flagged = 0
    print("Product brain health, %s" % today.isoformat())
    print("Entries: %d (%d approved), inbox proposals: %d" % (len(entries), len(approved), len(inbox_proposals())))
    print()

    def line(n, label, count, detail=""):
        nonlocal flagged
        flagged += 1 if count else 0
        print("%d. %-52s %d%s" % (n, label, count, ("   " + detail) if detail else ""))

    ages = ", ".join("%s (%s)" % (q, ("%dd" % a) if a is not None else "age unknown") for q, a, _ in questions)
    line(1, "Open questions", len(questions), ages)
    line(2, "Approved entries with no confirmer or owner", len(no_person), ", ".join(no_person))
    line(3, "Approved entries past review_by or older than 90 days", len(stale),
         ", ".join("%s (%s)" % s for s in stale))
    line(4, "Replaced or stopped entries still cited", len(cited),
         ", ".join("%s in %s" % (i, "; ".join(h)) for i, h in cited))
    line(5, "Inbox proposals older than 14 days", len(old_proposals),
         ", ".join("%s (%dd)" % p for p in old_proposals))
    line(6, "Entries scoped to \"all\"", len(all_scope), ", ".join(all_scope))
    print()
    print("Nothing flagged." if not flagged else "%d of 6 checks flagged. A person decides what to do about each." % flagged)
    return 1 if (args.strict and flagged) else 0


if __name__ == "__main__":
    sys.exit(main())
