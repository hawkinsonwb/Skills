# Repository conventions

These maintenance conventions apply when editing the `hawkinsonwb/Skills` repository. When this collection is installed as a plugin in another project, use that project's guidance and the requested skill instead.

Keep the canonical skill collection in `skills/<name>/SKILL.md`. Add each skill once; the installer and Claude plugin consume that directory directly.

When adding or editing skills, follow the Agent Skills specification linked in README.md. Keep shared instructions portable, declare tool requirements, and place supporting resources inside the skill folder with relative references.

Keep README installation instructions current when distribution changes. Update `.claude-plugin/plugin.json`'s version when releasing plugin changes so installed plugins can receive updates.

Keep examples in documentation rather than installable skill folders. Each skill must remain usable when installed individually, including its supporting resources.

Harness metadata, discovery rules, and `AGENTS.md` are generated. After changing skills, `docs/harness-context.md`, `docs/repository-conventions.md`, or Claude plugin metadata, run `python3 scripts/build-harness-files.py`; check with `python3 scripts/build-harness-files.py --check`. Maintain release metadata in `.claude-plugin/plugin.json`, routing wording in `docs/harness-context.md`, and these maintenance instructions in `docs/repository-conventions.md`.
