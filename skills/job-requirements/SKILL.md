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

Return requirement IDs, category, importance, wording, source quote, and why it
matters. Include company and role metadata only when supported. Do not compare
against the resume or propose edits here.

Mark education eligibility, enrollment, graduation timing, work authorization,
sponsorship, location, availability, compensation, and application logistics as
`screening_only`. Preserve them for job traceability, but exclude them from
resume bullet-gap analysis, experience-recall questions, and bullet proposals.
