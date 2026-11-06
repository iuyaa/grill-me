"""Run with: python -B -m unittest discover -s scripts -p 'test_*.py'."""

import tempfile
import unittest
from pathlib import Path

from package_skill import package_skill


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / "SKILL.md"
        self.skill.write_text('---\nname: grill\nmetadata:\n  version: "2.1.9"\n---\n\nBody.\n', encoding="utf-8")
        self.ref = self.root / "reference.md"
        self.ref.write_text("A reference.\n", encoding="utf-8")

    def test_check_preserves_edits_and_detects_changed_added_or_missing_files(self):
        self.assertEqual(package_skill(self.root), 2)
        self.ref.write_text("User edit.\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            package_skill(self.root, check=True)
        self.assertEqual(self.ref.read_text(), "User edit.\n")
        self.ref.write_text("A reference.\n", encoding="utf-8")
        extra = self.root / "local.md"
        extra.write_text("Local file.\n")
        with self.assertRaises(ValueError):
            package_skill(self.root, check=True)
        extra.unlink()
        self.ref.unlink()
        with self.assertRaises(ValueError):
            package_skill(self.root, check=True)

    def test_line_endings_do_not_create_false_local_edits(self):
        package_skill(self.root)
        self.ref.write_bytes(b"A reference.\r\n")
        self.assertEqual(package_skill(self.root, check=True), 2)

    def test_bump_is_numeric_and_manifest_covers_changed_version(self):
        package_skill(self.root, bump_patch=True)
        self.assertIn('version: "2.1.10"', self.skill.read_text())
        self.assertEqual(package_skill(self.root, check=True), 2)

    def test_invalid_version_does_not_write_files(self):
        self.skill.write_text("---\nname: grill\n---\n")
        with self.assertRaises(ValueError):
            package_skill(self.root, bump_patch=True)
        self.assertFalse((self.root / "manifest.json").exists())


if __name__ == "__main__":
    unittest.main()
