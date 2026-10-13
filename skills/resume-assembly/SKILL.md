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
fabricating LaTeX. Never produce a PDF locally. Return the complete tailored
resume plus a short change log. Do not introduce new edits during assembly;
send new ideas back through `resume-proposals`.

## LaTeX Header And Contact Details

Use the following header format in the sanitized `resume.tex`:

```latex
\begin{center}
    \textbf{\Huge \scshape MY NAME} \\ \vspace{1pt}
    \href{mailto:MY EMAIL}{\underline{MY EMAIL}} $|$
    \href{https://linkedin.com/in/MY NAME}{\underline{linkedin.com/in/MY NAME}} $|$
    \href{https://MY NAME.vercel.app}{\underline{MY NAME.vercel.app}}
\end{center}
```

Ensure the LaTeX source loads `hyperref`. Keep review placeholders in
`resume.tex`. Restore real contact details only through this skill's local
`scripts/replace_resume_contact.py` helper, which reads an owner-only `.env`
file. Locate the helper relative to the suite root, not the job workspace.
Do not echo contact values into chat or model inputs. See the suite README
for the four required fields and the `python-dotenv` dependency.

Run locally with a unique revision filename:

```sh
python3 /path/to/job-companion/scripts/replace_resume_contact.py \
  --input "JOB_DIR/resume.tex" \
  --output "JOB_DIR/private-resume-REVISION.tex" \
  --private-file "/path/to/.env"
```

Require successful contact injection and a nonempty private `.tex` artifact.
The helper refuses to overwrite an existing output and sets owner-only output
permissions. Check the source locally for unresolved placeholders and the
expected header structure without printing private values. The helper restores
contacts only; resolve other placeholders from confirmed evidence.

Return the private `.tex` as the final LaTeX artifact and the sanitized
`resume.tex` as the review source. Never run local PDF compilation or rendering,
including `pdflatex`, Tectonic, `latexmk`, or Docker rendering. No LaTeX compiler
is required. State that PDF compilation and rendered-layout verification have
not been performed. If injection or source checks fail, report the incomplete
step and available artifacts without claiming they are submission-ready.
