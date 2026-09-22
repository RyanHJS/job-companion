# Job Input

Provide exactly one primary source:

```yaml
source_type: url | pasted_text
source: "URL or complete job description"
person: "optional; infer Ryan or Chloe from the base resume"
company: "optional"
role: "optional"
```

For a URL, preserve the URL and report extraction warnings. For pasted text,
preserve the text exactly before normalization. Once complete job text is
available, resolve the person and company, choose a category or specific-job
grouping, allocate a unique `job_workspace`, and persist `job-description.md`
before continuing.
