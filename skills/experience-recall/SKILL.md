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

## Questioning loop

1. Ask a focused broad question about whether the candidate has used the
   capability and in what context.
2. Branch on the answer. Ask progressively more specific questions about the
   candidate's personal contribution, implementation choices, scope, users,
   deployment status, validation, metrics, and outcomes.
3. If the answer remains vague and the capability is material to the role, ask
   one short scenario or multiple-choice check. Test practical understanding
   relevant to the claimed work, not trivia or memorized definitions.
4. Stop when the evidence is sufficiently specific for a resume decision, or
   when the candidate says they do not know or did not do the work. Do not
   interrogate every inferred technology.

Prefer “Did you personally...?” and “Which part did you own?” over generic
questions. Ask a few high-value questions per turn and wait for answers before
branching further. Keep the tone investigative and non-accusatory: a knowledge
check clarifies the strength and boundaries of evidence; it is not a pass/fail
employment test.

Return question records using `templates/verification-question.md`, including
the requirement, evidence basis, inferred capability, question, and why the
answer matters. Convert answers into evidence records with `confirmed`,
`partially_confirmed`, `unconfirmed`, or `knowledge_only` status. A knowledge
check can strengthen or weaken confidence in the candidate's explanation, but
it cannot establish that the candidate shipped the work. Never turn an
unanswered question, inferred capability, or quiz answer into a resume fact.
