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

As soon as complete job text and the base resume are available, resolve the
candidate as Ryan or Chloe from the resume identity or explicit user context,
and extract the company from the posting. If either cannot be determined
reliably, ask only for the missing value before creating the workspace. Never
create an `unknown` person or company bucket.

Create the company bucket under the person, then choose whether the posting
belongs in a broad job-category bucket or a specific-job bucket:

`job-applications/<person>/<company>/<grouping>/<YYYY-MM-DD>-<role>[-<sequence>]/`

Prefer an existing matching category for comparable roles. Create a concise
filesystem-safe category when the role fits a reusable family. Otherwise use
the normalized specific job title so a specialized role is not flattened into
an inaccurate category. Record `grouping_type` as `category` or `specific_job`
and record the chosen `grouping_slug`. Use a numeric sequence to avoid
collisions. A retry may reuse a workspace only when both its source and content
match.

Persist the complete pasted or extracted posting to `job-description.md` using
`templates/job-description.md` before requirements analysis. Preserve pasted
text exactly. For a URL, preserve the source URL and the complete extracted
job-specific text. Never overwrite a different posting, and retain the file even
when downstream analysis stops.

Return `source_url`, `person`, `company`, `role`, `grouping_type`,
`grouping_slug`, `job_text`, `job_workspace`, `job_description_path`,
`extraction_warnings`, and `source_confidence`. Downstream skills use the
normalized text and write their artifacts into `job_workspace`.
