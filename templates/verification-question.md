# Candidate Choice

Present one concrete bullet opportunity as a lightweight choice:

```yaml
question_id: Q-001
requirement: "requirement being tested"
capability_theme: "high-level job theme"
resume_signal: "why the current resume suggests this may exist"
target_bullet: "new bullet or exact existing bullet this answer could improve"
proposed_direction: "the useful claim this opportunity could establish"
options:
  A: "first plausible bullet variant"
  B: "second meaningfully different variant"
  C: "third meaningfully different variant"
  D: "optional fourth variant"
  none: "None of these"
  other: "Something else"
question: "Which option is closest? Reply with a letter, none, or a correction."
follow_up_needed: contribution | implementation | scope | metric | outcome | none
resume_impact: "how a confirmed answer would create or materially improve the bullet"
selection_effects: "which facts each selection would and would not confirm"
```

Each option must be plausible from the stated resume signal, useful for the
stated requirement, and distinct in substance. Do not emit the choice when the
target, impact, or selection effects are unclear, or when the answer is already
stated in the resume or prior user input. Never invent a metric or imply that an
option is known to be true. Do not ask about education eligibility, enrollment,
work authorization, location, availability, compensation, or other
application-screening criteria.

After a selection, ask no more than one short follow-up for an essential fact.
Use an open-ended prompt only when responsible options cannot be formed. Avoid
compound questions and generic prompts such as "Tell me more about this."
