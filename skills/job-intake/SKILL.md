---
name: job-intake
description: Use when a job description arrives as a URL or raw text and must be normalized before resume analysis
---

# Job Intake

Accept one URL or pasted job description. For a URL, fetch and extract the
job-specific content, preserve the source URL, and report extraction warnings.
Remove navigation, cookie notices, duplicated text, and unrelated page content.
If the page is blocked, requires login, or lacks enough job text, ask the user
to paste the description. Never fill missing content from assumptions.

As soon as complete job text is available, create a new job workspace at
`job-applications/<company>-<role>-<YYYY-MM-DD>[-<sequence>]/`. Use `unknown`
for missing company or role metadata and a numeric sequence to avoid collisions.
A retry may reuse a workspace only when both its source and content match.

Persist the complete pasted or extracted posting to `job-description.md` using
`templates/job-description.md` before requirements analysis. Preserve pasted
text exactly. For a URL, preserve the source URL and the complete extracted
job-specific text. Never overwrite a different posting, and retain the file even
when downstream analysis stops.

Return `source_url`, `company`, `role`, `job_text`, `job_workspace`,
`job_description_path`, `extraction_warnings`, and `source_confidence`.
Downstream skills use the normalized text and write their artifacts into
`job_workspace`.
