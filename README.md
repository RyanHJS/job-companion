# Job Companion Suite

Job Companion Suite is a Codex skill for tailoring an existing resume to a
specific job. It analyzes the job, maps requirements to evidence in the base
resume, asks targeted questions when evidence is missing, and proposes exact
changes for review before assembling a final resume.

## Install In Codex

Ask Codex to install the skill from this repository:

```text
$skill-installer
Install the skill from https://github.com/RyanHJS/job-companion
```

Codex detects installed skills automatically. Restart Codex if the skill does
not appear after installation.

## Use In Codex

Invoke the suite with `$job-companion-suite`, then provide:

- a job posting URL or the pasted job description; and
- the base resume or resume template to tailor.

For example:

```text
$job-companion-suite

Tailor my base resume for this role.

Job: https://example.com/jobs/senior-ai-engineer

Base resume:
[Paste the current resume or attach the base resume file.]
```

You can paste the job description instead of a link:

```text
$job-companion-suite

Job description:
[Paste the complete job description.]

Base resume:
[Paste the current resume or attach the base resume file.]
```

The suite starts with job intake and evidence analysis. It presents proposed
resume changes for review before editing the source resume or assembling a
final version.

Each new posting gets its own folder under `job-applications/`. The suite saves
the pasted or extracted posting as `job-description.md` before analysis. Review
artifacts stay in that folder, and an approved LaTeX resume is written there as
`resume.tex` without overwriting the base template.

For Codex skill behavior and invocation details, see the
[official OpenAI documentation](https://developers.openai.com/codex/skills/).
