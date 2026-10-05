---
name: job-requirements
description: Use when normalized job text must be converted into ranked, traceable hiring requirements
---

# Job Requirements

Read normalized job text and produce ranked requirement records. Separate
must-have qualifications, responsibilities, preferred signals, seniority,
domain context, and likely evaluation criteria. Preserve exact supporting
quotes or character ranges where possible. Collapse synonyms and distinguish a
real hiring signal from incidental keyword mentions.

Group important requirements into high-level capability themes and keyword
families. A family may include equivalent role language, tools, methods, and
outcomes, but it must preserve meaningful distinctions between capabilities.
Use these families for semantic matching rather than requiring literal phrase
overlap or maximizing keyword frequency.

Return requirement IDs, category, importance, wording, source quote, why it
matters, capability theme, and keyword family. Identify the few themes most
likely to affect the hiring decision. Include company and role metadata only
when supported. Do not compare against the resume or propose edits here.

Mark education eligibility, enrollment, graduation timing, work authorization,
sponsorship, location, availability, compensation, and application logistics as
`screening_only`. Preserve them for job traceability, but exclude them from
resume bullet-gap analysis, experience-recall questions, and bullet proposals.
