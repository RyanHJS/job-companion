#!/usr/bin/env python3
# ruff: noqa: I001
"""Inject private contact details into a generated resume TeX file offline."""

from __future__ import annotations

import argparse
import os
import re
import tempfile
from pathlib import Path

class AssemblyError(ValueError):
    """Contact errors contain no private values."""


def escape_latex(value: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "{": r"\{", "}": r"\}", "$": r"\$", "&": r"\&",
        "#": r"\#", "_": r"\_", "%": r"\%",
        "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    }
    if any(ord(char) < 32 and char not in "\n\r\t" for char in value):
        raise AssemblyError("unsupported_control_character")
    return "".join(replacements.get(char, char) for char in value)


def parse_private_env(path: Path, *, allowed_keys: set[str], ignore_unknown_keys: bool = False) -> dict[str, str]:
    from io import StringIO
    from dotenv import dotenv_values
    from dotenv.parser import parse_stream

    text = path.read_text(encoding="utf-8")
    bindings = list(parse_stream(StringIO(text)))
    if any(binding.error for binding in bindings):
        raise AssemblyError("private_env_malformed")
    keys = [binding.key for binding in bindings if binding.key]
    if len(keys) != len(set(keys)):
        raise AssemblyError("private_env_duplicate")
    if not ignore_unknown_keys and any(key not in allowed_keys for key in keys):
        raise AssemblyError("private_env_key_not_allowed")
    values = dotenv_values(stream=StringIO(text), interpolate=False)
    fields = {key: value for key, value in values.items() if key in allowed_keys}
    if any(not value or not value.strip() for value in fields.values()):
        raise AssemblyError("private_contact_missing_required")
    if any(re.search(r"\$(?:\{|[A-Za-z_])", value) for value in fields.values()):
        raise AssemblyError("private_env_expansion")
    for key in ("RESUME_LINKEDIN_URL", "RESUME_WEBSITE_URL"):
        if key in fields and not re.fullmatch(r"https://[^\s]+", fields[key], re.IGNORECASE):
            raise AssemblyError("private_env_invalid_url")
    return fields


CONTACT_KEYS = {
    "RESUME_NAME",
    "RESUME_EMAIL",
    "RESUME_LINKEDIN_URL",
    "RESUME_WEBSITE_URL",
}
MARKED_BLOCK = re.compile(
    r"(?P<start>^% JOB_COMPANION_CONTACT_START\s*$).*?"
    r"(?P<end>^% JOB_COMPANION_CONTACT_END\s*$)",
    re.MULTILINE | re.DOTALL,
)
CENTER_BLOCK = re.compile(r"\\begin\{center\}.*?\\end\{center\}", re.DOTALL)


def _display_url(value: str) -> str:
    return re.sub(r"^https://", "", value, flags=re.IGNORECASE).rstrip("/")


def contact_block(fields: dict[str, str]) -> str:
    if CONTACT_KEYS - fields.keys():
        raise AssemblyError("private_contact_missing_required")
    name = escape_latex(fields["RESUME_NAME"])
    email = escape_latex(fields["RESUME_EMAIL"])
    linkedin_url = escape_latex(fields["RESUME_LINKEDIN_URL"])
    website_url = escape_latex(fields["RESUME_WEBSITE_URL"])
    linkedin_label = escape_latex(_display_url(fields["RESUME_LINKEDIN_URL"]))
    website_label = escape_latex(_display_url(fields["RESUME_WEBSITE_URL"]))
    return (
        "\\begin{center}\n    "
        + r"\textbf{\Huge \scshape "
        + name
        + r"} \\ \vspace{1pt}"
        + "\n    "
        + r"\href{mailto:"
        + email
        + r"}{\underline{"
        + email
        + r"}} $|$"
        + "\n    "
        + r"\href{"
        + linkedin_url
        + r"}{\underline{"
        + linkedin_label
        + r"}} $|$"
        + "\n    "
        + r"\href{"
        + website_url
        + r"}{\underline{"
        + website_label
        + "}}\n"
        + r"\end{center}"
    )


def replace_contact(source: str, fields: dict[str, str]) -> str:
    replacement = contact_block(fields)
    marked = MARKED_BLOCK.search(source)
    if marked:
        return source[: marked.start()] + replacement + source[marked.end() :]
    center = CENTER_BLOCK.search(source)
    if center:
        return source[: center.start()] + replacement + source[center.end() :]
    raise AssemblyError("resume_contact_block_missing")


def write_private(path: Path, content: bytes) -> None:
    if path.exists():
        raise AssemblyError("output_file_exists")
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        temporary.chmod(0o600)
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    path.chmod(0o600)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="sanitized input .tex")
    parser.add_argument("--output", required=True, type=Path, help="private output .tex")
    parser.add_argument(
        "--private-file",
        type=Path,
        default=Path(__file__).resolve().parents[1] / ".env",
        help="project dotenv file (defaults to .env)",
    )
    args = parser.parse_args()
    try:
        if not args.output.name.startswith("private-resume-"):
            raise AssemblyError("private_output_prefix_required")
        private_mode = args.private_file.stat().st_mode & 0o777
        if private_mode & 0o077:
            raise AssemblyError("private_file_permissions_too_open")
        fields = parse_private_env(
            args.private_file, allowed_keys=CONTACT_KEYS, ignore_unknown_keys=True
        )
        required = CONTACT_KEYS - fields.keys()
        if required:
            raise AssemblyError("private_contact_missing_required")
        source = args.input.read_text(encoding="utf-8")
        result = replace_contact(source, fields).encode("utf-8")
        write_private(args.output.expanduser().resolve(), result)
    except (AssemblyError, OSError, UnicodeError, ImportError):
        raise SystemExit("resume_contact_replacement_failed")
    print(args.output.expanduser().resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
