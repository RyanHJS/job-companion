---
name: job-companion-suite
description: Use when tailoring a resume to a job from a URL or pasted description and the work needs requirement analysis, evidence recovery, scored bullet proposals, and iterative human review
---

# Job Companion Suite

Coordinate the suite for one job application. Read the shared [resume
guidelines](references/resume-writing-guidelines.md) before writing or judging
resume content. Use the specialist skills in this order:

## Session Learning And Evolution

Treat each session as a bounded source of learning for the suite. When the user
explicitly settles an editorial decision, or repeated rendered evidence shows
that a heuristic is too strict or too loose, record the decision in the shared
resume-writing guidelines during the same session. Preserve the rationale and
scope of the change; distinguish confirmed rules from provisional observations.

When a durable rule changes, update the canonical reference at
`references/resume-writing-guidelines.md` and any maintained review copy such
as `docs/reviews/resume-writing-guidelines.md`. Do not change factual evidence,
invent claims, or promote a one-off preference into a general rule without
the user's confirmation. For example, if later review establishes that a 35-word
maximum reliably fits the target layout, replace the earlier bullet-length
heuristic and retain the rendered-layout requirement.

1. [`job-intake`](skills/job-intake/SKILL.md): normalize a URL or pasted job
   description.
2. [`job-requirements`](skills/job-requirements/SKILL.md): rank what the
   employer is actually asking for.
3. [`resume-evidence`](skills/resume-evidence/SKILL.md): inventory what the
   current resume demonstrates.
4. [`experience-recall`](skills/experience-recall/SKILL.md): recover omitted
   or underspecified experience through
   adaptive, requirement-linked questions. Infer adjacent capabilities only as
   prompts for verification; branch from broad experience questions into
   implementation details and use an occasional practical knowledge check when
   an answer is vague. Ask a few high-value questions, wait for answers, and
   update the evidence before proposing claims.
5. [`resume-proposals`](skills/resume-proposals/SKILL.md): produce exact,
   labeled bullet changes; do not rewrite the full resume yet.
6. Before user review, spawn two independent proposal reviewers: one acting as
   a recruiter and one as a technical hiring manager. Each reviews every new
   proposal for clarity, relevance, credibility, glaring issues, and questions
   it invites. They critique rather than silently rewrite.
7. [`proposal-judge`](skills/proposal-judge/SKILL.md): independently score and
   rank proposals when a cheap subagent is available.
8. [`resume-assembly`](skills/resume-assembly/SKILL.md): assemble only accepted
   proposals after the user asks for the complete resume.

## Job Application Workspaces And Review Artifacts

Create a separate workspace for every new job description as soon as intake
succeeds:

`job-applications/<person>/<company>/<grouping>/<posting>/`

Resolve `<person>` automatically as `ryan` or `chloe` from the base resume or
explicit user context. Extract `<company>` from the posting. If either value
cannot be determined reliably, ask for that missing value before creating the
workspace; do not create an `unknown` bucket.

Within the person's company bucket, classify the posting under either a broad,
reusable job category or the specific job title. Prefer an existing matching
category when it accurately groups comparable roles, such as `ai-engineering`
or `product-management`. Use a normalized specific title when the job is
specialized, does not fit a stable category, or grouping it would hide a
meaningful distinction. Record the choice as `category` or `specific_job` in
`job-description.md`.

Use filesystem-safe slugs. Name `<posting>` with the capture date and role slug,
adding a numeric sequence when the path already exists. A retry of the same
intake may reuse its workspace only when the source and job-description content
match; never overwrite a different posting.

Before requirements analysis, save the complete pasted or extracted posting as
`job-description.md` using
[`templates/job-description.md`](templates/job-description.md). Include the
source type, source URL when present, capture date, company, and role. Keep this
file even if later analysis stops or the user rejects all resume changes.

Keep every artifact for that posting in the same workspace, including the
normalized job description, resume snapshots, proposal diff and reviews, the
approved tailored source, and rendered output. Shared guidance remains outside
job-application folders.

For every proposal run, maintain two complete normalized Markdown snapshots:
`resume-current.md` and `resume-proposed.md`. The current snapshot represents
the source resume; the proposed snapshot has only candidate changes applied.
Generate a Git-style word/line diff between them and keep the proposal table as
a compact rationale ledger. The Markdown diff is the primary wording-review
surface and the table explains evidence and editorial reasoning.

Proposal generation may change Markdown review artifacts, but must not edit the
source `.tex`, `.docx`, PDF, or other submission format. After explicit user
approval, `resume-assembly` applies only approved changes to the source,
stores the tailored LaTeX source as `resume.tex` in the job workspace, compiles
it, and verifies the rendered layout. When the supplied base uses another source
format, preserve that format and filename instead of fabricating LaTeX.

Pass structured outputs between specialists using the templates in `templates/`.
Preserve proposal IDs across turns. Keep inferred and invented claims visibly
marked and out of the final resume until the user confirms them. Never invent
metrics, scale, employers, dates, or production status.

If the user provides only a URL, start with intake. If extraction fails, ask for
the job text instead of guessing. If the user provides pasted text, skip URL
fetching and begin with requirements.
