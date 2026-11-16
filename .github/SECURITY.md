# Security policy

This policy covers the Product Brain Starter itself: the four skills, the instructions in `AGENTS.md` and `CLAUDE.md`, the health script, the templates and the links.

If you made your own copy of the starter, this file describes the starter. Replace it with your own policy, or delete it.

## Report a problem privately

Please report security problems privately, and keep them out of public issues.

1. Open the **Security** tab of this repository and choose **Report a vulnerability**. Only the maintainers can see the report.
2. If that does not work for you, email anurag@rivoraconnect.com.au with "Security: product-brain-starter" in the subject.

Tell us what you found, how to reproduce it, and what someone could do with it. We aim to reply within five working days and to tell you what we will do and when.

## What to report

- A skill or instruction file that could lead an AI tool to run commands, change or delete files outside the brain, reach the network, or leak information without the person asking for it.
- The health script doing anything beyond reading files in the repository and printing a report.
- A link that points somewhere unsafe or has been taken over.
- Anything in this repository or its history that should not be public.

## What the starter does

- The skills read and write Markdown files in this folder. `brain-health` also runs `scripts/brain_health.py`. None of them gives your AI tool extra permissions: your tool's own permission settings still apply.
- `scripts/brain_health.py` uses the Python standard library only. It reads files in the repository, prints a report and changes nothing. It makes no network calls.
- There are no dependencies, workflows, hooks or tool settings to install.

## Supported versions

Only the latest version on the `main` branch is supported, and fixes land there. If you copied the starter earlier, compare your copy with `main` and take the change.
