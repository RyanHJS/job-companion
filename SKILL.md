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

## Resume Workspaces And Review Artifacts

Keep every resume and all of its resume-specific review artifacts in one folder:

`docs/resumes/<person>-<bucket>[-<target-or-date>]/`

Use a stable candidate slug and a broad role bucket, such as
`candidate-ai-engineer`, `candidate-research-engineer`, or
`candidate-full-stack-engineer`. Append a company or role slug when known;
otherwise append an ISO date or numeric suffix. Shared guidance remains outside
resume folders.

For every proposal run, maintain two complete normalized Markdown snapshots:
`resume-current.md` and `resume-proposed.md`. The current snapshot represents
the source resume; the proposed snapshot has only candidate changes applied.
Generate a Git-style word/line diff between them and keep the proposal table as
a compact rationale ledger. The Markdown diff is the primary wording-review
surface and the table explains evidence and editorial reasoning.

Proposal generation may change Markdown review artifacts, but must not edit the
source `.tex`, `.docx`, PDF, or other submission format. After explicit user
approval, `resume-assembly` applies only approved changes to the source,
compiles it, and verifies the rendered layout.

Pass structured outputs between specialists using the templates in `templates/`.
Preserve proposal IDs across turns. Keep inferred and invented claims visibly
marked and out of the final resume until the user confirms them. Never invent
metrics, scale, employers, dates, or production status.

If the user provides only a URL, start with intake. If extraction fails, ask for
the job text instead of guessing. If the user provides pasted text, skip URL
fetching and begin with requirements.
