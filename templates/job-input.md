# Job Input

Provide exactly one primary source:

```yaml
source_type: url | pasted_text
source: "URL or complete job description"
company: "optional"
role: "optional"
```

For a URL, preserve the URL and report extraction warnings. For pasted text,
preserve the text exactly before normalization. Once complete job text is
available, allocate a unique `job_workspace` and persist
`job-description.md` before continuing.
