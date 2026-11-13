# Product Brain Starter: a free AI product brain for your team

**Product Brain Starter is a free, open-source AI product brain for product teams.** It is a folder of plain files:

- a decision log for your product decisions, rules and clarifications;
- an `AGENTS.md` (with `CLAUDE.md` pointing to it) that every AI tool reads first;
- four Claude Code skills;
- nine planning steps that make AI think a feature through before a coding agent builds it.

Copy it and fill in a few files. Your team, and every AI tool it uses, then works from the same checked answers. It works with Claude Code, Cursor, GitHub Copilot, Codex and ChatGPT. There is no server, no database and no sign-up.

**The free guide:** [Start your product brain](https://rivoraconnect.com.au/resources/guides/start-your-product-brain) walks through everything this repository does, step by step, with pictures and prompts you can use today.

> **What is an AI product brain?** A shared memory of how your product works: the decisions, rules, code knowledge and clarifications behind it, which people and AI tools draw on when they design and build each feature. See the [AI product brain glossary](https://rivoraconnect.com.au/glossary#ai-product-brain).

## Why it exists

Leadership asks for predictable delivery. Teams reach for AI to move faster, and they do move faster. AI also assumes whatever nobody told it: the rule for one client, the edge case, the decision from last month. The plan looks complete, the build starts, the gaps turn up as rework, and the date moves.

On an established product, the knowledge that matters was never written down where AI can use it:

- **Decisions live in conversations.** A meeting, a Slack thread or a call settles something, and the decision stays in the note-taker's transcript. ([How to keep product decisions made in Slack](https://rivoraconnect.com.au/problems/decisions-lost-in-slack))
- **Every AI starts from zero.** Each person re-explains the product to their own AI, and each AI fills the gaps differently. ([Why AI tools guess your product's rules](https://rivoraconnect.com.au/problems/ai-tools-guessing))
- **The same few people answer the same questions.** Work waits on them, and their knowledge leaves when they do. ([Why product teams wait on the same experts](https://rivoraconnect.com.au/problems/expert-queue), [Keep product knowledge when experts leave](https://rivoraconnect.com.au/problems/knowledge-leaving))
- **Instructions get buried.** In a 2025 study that gave 20 leading models up to 500 simple instructions at once, the best followed about 68% of them ([IFScale, Distyl AI](https://arxiv.org/abs/2507.11538)). One long context file is where the rule for one client gets skipped.

A product brain puts that knowledge in one checked place: each entry says what was decided, where it applies, who confirmed it, when, and where it came from. Before the plan is written, AI then works through every part of the feature, so the questions it would otherwise answer with an assumption come up first.

## What's inside

```
product-brain-starter/
  AGENTS.md              always loaded by every AI tool (CLAUDE.md points here)
  CLAUDE.md
  brain/
    INDEX.md             one line per entry: id, title, type, scope, status
    decisions/           D-0001 and on: what was decided, and where it applies
    rules/               R-0001 and on: rules for a product, area or client
    clarifications/      C-0001 and on: answers to questions people keep asking
    code-notes/          K-0001 and on: what the code does that nobody wrote down
    inbox/               proposed by AI, not yet confirmed by a person
    open-questions.md
  steps/                 the nine planning steps, one checklist each
  features/_template/    brief, questions and handoff for each feature
  sources/               transcripts and notes, opened only to check a claim
  .claude/skills/        capture, plan-in-nine-steps, write-handoff, brain-health
  .github/               pull request template and a CODEOWNERS example
  scripts/brain_health.py
```

Every entry in the decision log is one small Markdown file with front matter:

```yaml
---
id: D-0001
type: decision
title: Customers on the legacy plan keep paper invoices until June 2027
status: approved          # proposed | approved | replaced | stopped
scope: {product: billing, area: invoicing, client: legacy-plan}
confirmed_by: "Head of Billing"
confirmed_on: 2026-11-12
source: sources/2026-11-12-billing-sync.md
supersedes:
review_by: 2027-02-12
---
```

The examples are made up. Keep them as a guide for your first week, then delete them. For a spreadsheet version, see the free [decision log template](https://rivoraconnect.com.au/resources/tools/decision-log-template).

## Quick start: your first week

Start with one product area, and one feature you plan to build in the next month. A brain built around real work stays current.

1. **Day 1. Set up.** Click "Use this template" on GitHub, or copy the folder into your product repository as `product-brain/`. Fill in `AGENTS.md`: the product in five lines, the words your team uses, and the rules that apply everywhere. Agree who confirms entries in each area. The free [coding-agent context file builder](https://rivoraconnect.com.au/resources/tools/coding-agent-context-file-builder) helps with a first draft.
2. **Day 2. Capture.** Put three recent transcripts from your AI note-taker into `sources/` (a planning meeting, a client call, a design review). Run the `capture` skill on each. Proposals land in `brain/inbox/`, each quoting the line it came from.
3. **Day 3. Confirm.** Each named person reads their proposals, corrects them, approves them and moves them into `brain/`. A pull request review works well, with CODEOWNERS mapping each area to its confirmers. Only a person ever sets `status: approved`.
4. **Day 4. Plan one feature in nine steps.** Copy `features/_template/`, fill in the brief and run `plan-in-nine-steps`. A person approves each step before the next one starts.
5. **Day 5. Hand off.** Run `write-handoff` and give the result to your coding agent. Review the pull request against the entries it touched.

Then open the folder in Claude Code, Cursor or Codex and ask: "Read AGENTS.md and brain/INDEX.md and tell me what you know about this product."

## The nine planning steps

Before AI writes a plan, it works through nine steps. Each step is a checklist in `steps/`. Start with a five-line executive summary, so every person and AI knows what you're building and why now. Rewrite it last, once the other steps are approved.

| Step | What AI must think through before it writes |
|---|---|
| **1. Executive summary** | What it is, who it's for, why now, the value and the decision asked. In the final pass: the top delivery risk and how ready it is to build |
| **2. Feature intent** | The user problem, who it's for, today's workaround, the outcome, what's in and out of scope, and how you'll know it worked |
| **3. Impact on the current product** | Which screens, workflows, roles, data and integrations change, and whether each is new, changed, removed or unknown |
| **4. Frontend and UX** | The flow step by step, and every state: empty, loading, error, success, no permission. Validation, accessibility, mobile and copy |
| **5. Backend and platform** | Services and endpoints touched, each failure and how it is handled, background jobs, security and privacy needs |
| **6. System impact** | Which modules are touched and how they connect, with the risks and who should check them |
| **7. Data** | What is added, changed or removed, migration and backfill order, whether each step can be reversed, retention |
| **8. Implementation plan** | Where to start, the steps in order by team, blockers, rollout and rollback |
| **9. Delivery backlog** | Stories from the user's view, each with acceptance criteria, priority, dependencies and the decisions behind it |

Every step cites the entries it relies on, labels each assumption with what would prove it wrong, and lists the questions that block it, each with an owner. The handoff is built from approved steps only and ends with "stop and ask if unsure". More on this: [Requirements AI coding agents can follow](https://rivoraconnect.com.au/use-cases/requirements-for-coding-agents) and the free [feature readiness check](https://rivoraconnect.com.au/resources/tools/feature-readiness-check).

## How it works

Three ideas do most of the work:

1. **Scope before similarity.** The AI loads only what applies to the product, area or client you are working on, then looks for what is relevant. Loading everything buries the rules that matter.
2. **A person confirms before anything counts.** The AI proposes entries. A named person approves them.
3. **Later work reads only approved work.** Each planning step reads the approved steps before it. Drafts and proposals are undecided.

Four levels of storage keep the always-loaded part short:

| Level | Where | When the AI reads it |
|---|---|---|
| Always-on context | `AGENTS.md` | Every turn, so keep it short enough to read in two minutes |
| The memory | `brain/` | Through `brain/INDEX.md`, opening only approved entries whose scope matches |
| Feature records | `features/<slug>/` | While that feature is planned and built |
| Raw sources | `sources/` | Only to check a claim an entry makes |

This is how you give coding agents the product context they need without pasting everything in. More on this: [Product context for AI coding agents](https://rivoraconnect.com.au/use-cases/context-for-coding-agents).

## The skills

| Skill | Use it when | What it does |
|---|---|---|
| `capture` | A new transcript or note lands in `sources/` | Proposes decisions, rules, clarifications and code notes into `brain/inbox/`, each with the line it came from, a suggested scope and a confirmer |
| `plan-in-nine-steps` | You start planning a feature | Drafts one step at a time from approved entries, and stops for a person to approve each |
| `write-handoff` | The plan is approved | Builds a handoff for your coding agent from approved steps and approved entries only |
| `brain-health` | Weekly and monthly reviews | Runs the health check and suggests one action per problem |

**Claude Code** loads the skills in `.claude/skills/` when you open this folder. To use them in another repository, copy the four skill folders into that repository's `.claude/skills/`, or into `~/.claude/skills/` for every project.

**Cursor, Codex and GitHub Copilot** read `AGENTS.md`. To run a skill, ask the tool to follow its file, for example: "Follow the steps in .claude/skills/capture/SKILL.md for sources/2026-11-12-billing-sync.md."

**ChatGPT and Claude projects** work from files you upload, and uploaded copies go stale. Keep this repository as the source of truth, and upload `AGENTS.md` with only the entries a piece of work needs.

## The health check

```
python scripts/brain_health.py
python scripts/brain_health.py --today 2026-12-01
python scripts/brain_health.py --strict    # exit 1 if anything is flagged, for CI
```

Python 3, standard library only. It reads the front matter in `brain/` and never changes a file. It reports six numbers:

1. Open questions, and how long each has waited.
2. Entries with no confirmer or owner.
3. Approved entries past their review date.
4. Replaced or stopped entries still cited somewhere in the repository.
5. Inbox proposals waiting more than 14 days.
6. Entries scoped to "all".

Run it in a weekly 15-minute review: clear the inbox and the open questions. Once a month, owners check every entry past its review date: still true, replaced or stopped.

## FAQ

### What is an AI product brain?

An AI product brain is a shared memory of how your product works: the decisions, rules, code knowledge and clarifications behind it, which people and AI tools draw on when they design and build each feature. Each entry says what was decided, where it applies, who confirmed it, when, and where it came from. This repository is a do-it-yourself version you keep in git.

### How is this different from a CLAUDE.md or AGENTS.md file?

A `CLAUDE.md` or `AGENTS.md` file is loaded on every turn, so it has to stay short. Anthropic's own advice is to keep `CLAUDE.md` concise ([Claude Code best practices](https://code.claude.com/docs/en/best-practices)). A product brain keeps that file short and puts everything else in entries the AI opens only when they apply: decisions, rules scoped to a product, area or client, and the questions still open. `AGENTS.md` tells the AI how to use the brain.

### Does it work with Cursor, GitHub Copilot, Codex and ChatGPT?

Yes. The brain is plain Markdown in a folder. Cursor, Codex and GitHub Copilot read `AGENTS.md` as project instructions, Claude Code reads `CLAUDE.md` (which points to `AGENTS.md`) and loads the skills, and ChatGPT or Claude projects can work from uploaded files. Every tool reads the same entries, so they stop giving different answers.

### How is it different from architecture decision records (ADRs)?

ADRs record engineering decisions about how the system is built, usually by engineers for engineers. A product brain records product decisions, business rules and clarifications, often made by product managers, client leads and business owners. Each entry has a scope, so a rule for one client stays with that client, and a status that AI tools respect. Code notes sit alongside and can link to your ADRs.

### Can we keep it inside our product repository?

Yes. Copy the folder into your repository as `product-brain/`. CODEOWNERS maps each area to the people who confirm it, and the pull request template asks which entries a change relied on, so you can [trace code back to the product decision](https://rivoraconnect.com.au/use-cases/decisions-traceable-into-code).

### When does doing it yourself stop working?

It works well for one product and a few people. As the product grows, keeping it current becomes a job of its own:

- the confirmers become a bottleneck, and `confirmed_by` is typed by hand with nobody checking it;
- scope is a filter the AI applies on trust, and one repository shows every client's rules to everyone;
- as entries grow, the index stops fitting in the AI's context;
- conflicts between entries are found by eye;
- nobody can see exactly what the AI read before it wrote a plan.

## Further reading

**Problems this solves**
- [Why AI tools guess your product's rules](https://rivoraconnect.com.au/problems/ai-tools-guessing)
- [How to keep product decisions made in Slack](https://rivoraconnect.com.au/problems/decisions-lost-in-slack)
- [Why product teams wait on the same experts](https://rivoraconnect.com.au/problems/expert-queue)
- [Keep product knowledge when experts leave](https://rivoraconnect.com.au/problems/knowledge-leaving)

**Use cases**
- [Product context for AI coding agents](https://rivoraconnect.com.au/use-cases/context-for-coding-agents)
- [Requirements AI coding agents can follow](https://rivoraconnect.com.au/use-cases/requirements-for-coding-agents)
- [Trace code back to the product decision](https://rivoraconnect.com.au/use-cases/decisions-traceable-into-code)

**Free tools**
- [Decision log template](https://rivoraconnect.com.au/resources/tools/decision-log-template)
- [Feature readiness check](https://rivoraconnect.com.au/resources/tools/feature-readiness-check)
- [Expert queue calculator](https://rivoraconnect.com.au/resources/tools/expert-queue-calculator)
- [Coding-agent context file builder](https://rivoraconnect.com.au/resources/tools/coding-agent-context-file-builder)

**Notes**
- [A team that builds fast needs one product brain](https://rivoraconnect.com.au/resources/notes/one-product-brain)
- [AI product brain glossary](https://rivoraconnect.com.au/glossary#ai-product-brain)
- [Claude Projects: an alternative or an add-on?](https://rivoraconnect.com.au/compare/claude-projects)

## When you outgrow it

This starter is a convention your team keeps by hand. With more people, clients, products and AI tools, keeping it current gets hard. [Rivora Connect](https://rivoraconnect.com.au) is an AI product brain for product teams on established software. Your team designs each feature in Rivora, a person approves every part, a rule for one client stays with that client, and the next feature starts with everything your team confirmed. To talk through your setup, book a [free 30-minute session](https://rivoraconnect.com.au/free-session): your setup today, and where AI can help.

## Licence

MIT. See [LICENSE](LICENSE). Copy it, change it and use it at work.

Questions and suggestions are welcome as GitHub issues.

Made by [Rivora Connect](https://rivoraconnect.com.au).
