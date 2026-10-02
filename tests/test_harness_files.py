import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class HarnessFilesTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('.claude-plugin', 'docs', 'skills', 'scripts'):
            shutil.copytree(ROOT / name, self.root / name)
        self.command = [sys.executable, str(self.root / 'scripts/build-harness-files.py')]

    def run_builder(self, *args):
        return subprocess.run([*self.command, *args], capture_output=True, text=True)

    def test_freshness_check_is_read_only_and_detects_changes(self):
        self.assertNotEqual(self.run_builder('--check').returncode, 0)
        self.assertFalse((self.root / '.codex-plugin').exists())
        self.assertEqual(self.run_builder().returncode, 0)
        self.assertEqual(self.run_builder('--check').returncode, 0)
        context = self.root / 'docs/harness-context.md'
        context.write_text(context.read_text() + '\nNew routing instruction.\n')
        before = (self.root / 'AGENTS.md').read_text()
        self.assertNotEqual(self.run_builder('--check').returncode, 0)
        self.assertEqual((self.root / 'AGENTS.md').read_text(), before)

    def test_new_skills_and_versions_propagate(self):
        skill = self.root / 'skills/new-task/SKILL.md'
        skill.parent.mkdir()
        skill.write_text('---\nname: new-task\ndescription: Plan a new task.\n---\n\nInstructions.\n')
        source = self.root / '.claude-plugin/plugin.json'
        metadata = json.loads(source.read_text())
        metadata['version'] = '9.8.7'
        source.write_text(json.dumps(metadata))
        self.assertEqual(self.run_builder().returncode, 0)
        for name in ('.codex-plugin/plugin.json', '.devin-plugin/plugin.json', '.qoder-plugin/plugin.json',
                     'plugin.json', 'gemini-extension.json', 'package.json'):
            self.assertEqual(json.loads((self.root / name).read_text())['version'], '9.8.7')
        self.assertIn('`new-task`: Plan a new task.', (self.root / 'AGENTS.md').read_text())
        for name in ('.codex-plugin/plugin.json', '.qoder-plugin/plugin.json', '.devin-plugin/plugin.json'):
            manifest = json.loads((self.root / name).read_text())
            self.assertEqual((self.root / manifest['skills']).resolve(), self.root / 'skills')
        self.assertEqual(json.loads((self.root / 'package.json').read_text())['pi']['skills'], ['./skills'])


if __name__ == '__main__':
    unittest.main()
