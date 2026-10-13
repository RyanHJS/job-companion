import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "replace_resume_contact.py"


class ContactTests(unittest.TestCase):
    def test_offline_header_and_private_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "resume.tex"
            original = "before\n\\begin{center}old\\end{center}\nafter\n"
            source.write_text(original)
            env = root / ".env"
            env.write_text(
                'RESUME_NAME="Example & Person"\n'
                'RESUME_EMAIL=person@example.invalid\n'
                'RESUME_LINKEDIN_URL=https://linkedin.com/in/example_person\n'
                'RESUME_WEBSITE_URL=https://example.invalid/\n'
                'OTHER_SETTING=ignored\n'
            )
            env.chmod(0o600)
            output = root / "private-resume-test.tex"
            command = [sys.executable, str(SCRIPT), "--input", str(source),
                       "--output", str(output), "--private-file", str(env)]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            content = output.read_text()
            self.assertIn(r"\textbf{\Huge \scshape Example \& Person} \\ \vspace{1pt}", content)
            self.assertIn(r"\href{mailto:person@example.invalid}{\underline{person@example.invalid}}", content)
            self.assertIn(r"\href{https://linkedin.com/in/example\_person}{\underline{linkedin.com/in/example\_person}}", content)
            self.assertIn(r"\href{https://example.invalid/}{\underline{example.invalid}}", content)
            self.assertEqual(output.stat().st_mode & 0o777, 0o600)
            self.assertEqual(source.read_text(), original)
            self.assertEqual(list(root.glob("*.pdf")), [])
            retry = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(retry.returncode, 0)
            self.assertEqual(output.read_text(), content)

    def test_empty_fields_fail_without_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            env = root / ".env"
            env.write_text('RESUME_NAME=""\nRESUME_EMAIL=\nRESUME_LINKEDIN_URL=\nRESUME_WEBSITE_URL=\n')
            env.chmod(0o600)
            output = root / "private-resume-test.tex"
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--input", str(root / "resume.tex"),
                 "--output", str(output), "--private-file", str(env)],
                capture_output=True, text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
