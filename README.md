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

Each new posting gets its own folder under
`job-applications/<ryan-or-chloe>/<company>/`. Within that company bucket, the
suite automatically groups comparable roles by job category or uses the
specific job title for a specialized role. It saves the pasted or extracted
posting as `job-description.md` before analysis. Review artifacts stay in that
posting folder, and an approved LaTeX resume is written there as `resume.tex`
without overwriting the base template.

## Contact Setup

Enter your information in a local `.env` file using these fields:

```dotenv
RESUME_NAME=""
RESUME_EMAIL=
RESUME_LINKEDIN_URL=
RESUME_WEBSITE_URL=
```

Fill in all four values. Keep your name in quotes, enter your email address,
and use full `https://` URLs for LinkedIn and your website. Keep `.env` local
and restrict it to your account with `chmod 600 .env`.

The contact helper requires Python 3.10 or newer and `python-dotenv`:

```sh
python3 -m pip install python-dotenv
```

After approved assembly, the skill runs `scripts/replace_resume_contact.py`
locally to create a separate `private-resume-<revision>.tex`. The header uses a
centered, bold `\Huge \scshape` name, 1pt spacing, and underlined contact links
separated by vertical bars. The helper reads `.env` without sending contact
values to the model, refuses to overwrite an existing artifact, and creates
owner-only output files.

The skill returns sanitized and private `.tex` files only. It never produces
a PDF locally and requires no LaTeX compiler. PDF compilation and
rendered-layout verification are left to you outside the skill workflow.

For Codex skill behavior and invocation details, see the
[official OpenAI documentation](https://developers.openai.com/codex/skills/).
