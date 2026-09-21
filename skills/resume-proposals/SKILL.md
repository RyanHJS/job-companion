---
name: resume-proposals
description: Use when ranked job requirements and resume evidence should become exact, reviewable resume bullet changes
---

# Resume Proposals

Read the shared resume guidelines, ranked requirements, evidence map, and
answered recall questions. Generate discrete records using
`templates/proposal-record.md`; do not assemble a complete resume or edit the
source resume.

Use labels: `rewritten` for one existing bullet, `recombined` for multiple
existing evidence items, `inferred` for a plausible unstated capability, and
`invented` for a new hypothesis. Mark inferred and invented proposals as
requiring human verification. Never invent metrics, dates, employers, users, or
production status. Keep bullets qualification-led, specific, and within two
rendered lines in the target layout. Draft to the shared guideline's 24–25-word
target and 28-word maximum. Apply its bold-formatting rule. Avoid bullets whose
only purpose is naming a tool.

## Review artifact

Every proposal run must produce two complete normalized Markdown snapshots
using `templates/resume-text-snapshot.md`: `resume-current.md` and
`resume-proposed.md`. Preserve the current resume structure and change only
wording in scope for the proposal run.

Generate a Git-style word/line diff between the snapshots as the primary
wording-review surface. Also produce a compact rationale ledger using
`templates/resume-proposal-diff.md`; the ledger must contain one table with
these columns:

| Before | After | Why |
|---|---|---|
| Existing wording, or `New bullet` | Exact proposed wording | Requirement, evidence, and reason for the change |

Before presenting proposals to the user, spawn two independent reviewers:

1. A recruiter reviews every new proposal for immediate comprehensibility,
   role relevance, scan value, credibility, and wording that may confuse a
   non-specialist.
2. A technical hiring manager reviews every new proposal for technical
   coherence, meaningful engineering depth, unsupported implications, missing
   context, and interview questions the wording invites.

Reviewers must return proposal IDs, a high-level verdict, glaring issues, and
questions. They may suggest a direction but must not silently replace proposal
text. Record both perspectives using
`templates/proposal-perspective-review.md`; unresolved concerns remain visible
to the user.

Include the stable proposal ID and target location in the `Why` cell or as a
short heading immediately above the table. Include only changed points in the
ledger. Stop after generating the snapshots, diff, ledger, and two perspective
reviews; wait for user approval or corrections.

Do not edit, overwrite, format, compile, or otherwise mutate the original
`.tex`, `.docx`, PDF, or other resume source while proposing changes. Do not
generate a replacement source file as a side effect. Source edits belong only
to `resume-assembly`, after the user explicitly approves the proposal diff and
asks for the complete tailored resume.

Return an overall fit estimate, important requirements, proposals, unresolved
opportunities, and a next action for every proposal. Preserve stable IDs across
revisions.
