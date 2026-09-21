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

Return `source_url`, `company`, `role`, `job_text`, `extraction_warnings`, and
`source_confidence`. Keep the original text for traceability; downstream skills
use the normalized text.
