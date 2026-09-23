# Verification Question

Ask one concrete question tied to one bullet opportunity:

```yaml
question_id: Q-001
requirement: "requirement being tested"
resume_signal: "why the current resume suggests this may exist"
target_bullet: "new bullet or exact existing bullet this answer could improve"
question: "Did you ...? What did you personally own, for whom, and what happened?"
answer_needed: contribution | implementation | scope | metric | outcome
resume_impact: "how the answer would create or materially improve the bullet"
answer_branches: "how yes, no, or materially different answers change the bullet decision"
```

Do not emit the question when `target_bullet`, `resume_impact`, or
`answer_branches` is unclear, or when the answer is already stated in the resume
or prior user input. Do not ask about education eligibility, enrollment, work
authorization, location, availability, compensation, or other
application-screening criteria. Prefer questions that recover omitted
contribution, implementation, scope, outcome, or scale. Avoid generic prompts
such as “Tell me more about this.”
