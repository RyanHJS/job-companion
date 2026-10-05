---
name: experience-recall
description: Use when job-fit analysis reveals weak or missing evidence that the candidate may have done but omitted from the resume
---

# Experience Recall

Recover omitted or underspecified experience with candidate-first choices, not
an interview-first questionnaire. Start from the highest-value job themes and
adjacent resume signals. Infer plausible bullet directions, show the candidate
what would help the application, and let them select or correct the closest
version. An inference is only a prompt for verification, never evidence by
itself.

Prioritize the few themes most likely to affect the hiring decision. Do not seek
exhaustive keyword coverage. Ask for input only when it could create a new
bullet or materially improve an existing bullet's contribution, technical
substance, scope, outcome, or relevance. If the answer would only determine
application eligibility or satisfy curiosity, do not ask.

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

## Candidate-first loop

1. Choose the highest-value bullet-addressable theme whose evidence is weak,
   missing, or underspecified. Confirm the needed fact is not already present.
2. Draft one useful bullet direction and three or four concise variants grounded
   in the available resume signals. Make the variants meaningfully different,
   such as discovery, coordination, implementation, or validation; do not
   merely swap synonyms.
3. Present the variants as `A`, `B`, `C`, and optionally `D`, followed by
   `None of these` and `Something else`. State that they are hypotheses and ask
   which is closest. Present one opportunity at a time and wait for the answer
   before proposing another opportunity.
4. Treat a selection as the candidate asserting that the general direction is
   true, not as automatic confirmation of every scope, outcome, or causal detail
   in its wording. Ask at most one short follow-up when an essential fact is
   still needed. Prefer a bounded choice when responsible options exist.
5. Record only the facts the candidate actually confirmed. Stop once the answer
   supports a bullet decision, the candidate rejects the opportunity, or the
   remaining detail would not materially improve the resume.

Use a direct open-ended question only when the resume and job theme do not
support responsible variants. In that fallback, ask for one missing fact rather
than a compound narrative covering ownership, audience, implementation, and
outcome. Do not administer knowledge checks or interview quizzes.

Return choice records using `templates/verification-question.md`, including the
theme, evidence basis, target bullet, proposed direction, variants, and exact
resume impact. Convert answers into evidence records with `confirmed`,
`partially_confirmed`, or `unconfirmed` status. Preserve the candidate's
correction when `Something else` is selected. Never turn an unselected option,
an unanswered prompt, or an inferred capability into a resume fact.
