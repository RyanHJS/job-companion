# Proposal Record

```yaml
proposal_id: P-001
target: "role or bullet identifier"
label: rewritten | recombined | inferred | invented
current_text: "existing wording or null"
proposed_text: "exact bullet"
requirement: "job requirement addressed"
resume_basis: ["evidence identifiers"]
fit_score: 0
grounding_score: 0
plausibility_score: 0
specificity_score: 0
risk: low | medium | high
human_verification: not_needed | required
status: keep | edit | reject | confirm | pending
```

Proposal records are summarized in `templates/resume-proposal-diff.md` and
paired with the Markdown snapshots described in
`templates/resume-text-snapshot.md`. Proposal generation must not edit the
resume source.
