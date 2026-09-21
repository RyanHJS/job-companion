# Job Description

Persist one file for every new posting at
`job-applications/<company>-<role>-<YYYY-MM-DD>[-<sequence>]/job-description.md`.

```yaml
---
source_type: url | pasted_text
source_url: "URL or null"
captured_at: "YYYY-MM-DD"
company: "company or unknown"
role: "role or unknown"
---
```

After the metadata, include the complete pasted description or the complete
job-specific text extracted from the URL. Preserve pasted text exactly. Do not
replace a different posting already stored at the target path; allocate the next
numeric sequence instead.
