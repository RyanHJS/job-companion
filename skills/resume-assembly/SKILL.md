---
name: resume-assembly
description: Use only after the user has reviewed resume proposals and explicitly asks for a complete tailored resume
---

# Resume Assembly

Read the shared resume guidelines, reviewed current/proposed Markdown snapshots,
their Git-style diff, the rationale ledger, and accepted proposal records.
Proceed only when the user has explicitly approved the relevant changes and
asked for assembly. Include only proposals marked accepted or explicitly
confirmed. Preserve chronology, dates, titles, formatting conventions, and
contribution scope. Keep unconfirmed inferred or invented claims out of the
final resume.

Only at this stage may you edit the resume source (`.tex`, `.docx`, or another
requested source format). Apply the approved Markdown diff. For a LaTeX base,
write the complete tailored source to `resume.tex` in the same job-specific
folder as `job-description.md`; do not overwrite the base template. For another
source format, preserve its format and filename in that folder instead of
fabricating LaTeX. Compile when the format supports it, keep rendered output in
the same folder, verify the rendered layout, and return the complete tailored
resume plus a short change log. Do not introduce new edits during assembly;
send new ideas back through `resume-proposals`.
