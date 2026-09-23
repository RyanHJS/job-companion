---
name: experience-recall
description: Use when job-fit analysis reveals weak or missing evidence that the candidate may have done but omitted from the resume
---

# Experience Recall

Recover omitted or underspecified experience through an adaptive, requirement-
linked interview. Start from the job requirements and resume evidence, then
reason about adjacent capabilities that the demonstrated work may imply. For
example, Triton and ONNX inference deployment may justify asking about PyTorch,
model export, CUDA, preprocessing, or performance validation, but the inference
is only a prompt for verification, never evidence by itself.

Ask a question only when its answer could create a new bullet or materially
improve an existing bullet's contribution, technical substance, scope, outcome,
or relevance. Before asking, identify the exact bullet opportunity and how each
possible answer would change it. If the answer would only determine application
eligibility or satisfy curiosity, do not ask.

Treat facts already stated in the current resume as accepted evidence. Do not
ask the candidate to re-verify its metrics, user counts, rollout status,
technologies, dates, employers, or contribution scope. Ask about an existing
claim only when another user-provided source directly contradicts it, the claim
is internally ambiguous, or the user explicitly requests a fact check. State
the concrete conflict instead of asking a generic credibility question.
“Internally ambiguous” means the resume contains conflicting values or wording
with two materially different factual interpretations; missing proof or
methodology is not ambiguity.

Never ask about education eligibility or enrollment, graduation deadlines, work
authorization, sponsorship, location, availability, compensation, demographic
information, or other application-screening criteria. This skill optimizes
experience and project bullet points; it does not screen the candidate.

## Questioning loop

1. Identify a high-value job requirement whose bullet evidence is missing or
   materially underspecified. Skip requirements unrelated to bullet content.
2. Confirm the answer is not already present in the resume or prior user input.
3. Ask one focused question about the candidate's personal contribution,
   implementation choice, scope, or outcome, naming the bullet it could improve.
4. Branch only when the first answer reveals a concrete bullet opportunity that
   still needs one essential detail. Stop when the evidence supports a resume
   decision or the candidate says they did not do the work.

Prefer “Did you personally...?” and “Which part did you own?” for omitted work,
not work already documented in the resume. Ask a few high-value questions per
turn and wait for answers before branching further. Do not administer knowledge
checks or interview quizzes; they do not establish resume evidence.

Return question records using `templates/verification-question.md`, including
the requirement, evidence basis, target bullet, question, and exact resume
impact. Convert answers into evidence records with `confirmed`,
`partially_confirmed`, or `unconfirmed` status. Never turn an unanswered
question or inferred capability into a resume fact.
