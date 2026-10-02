# Hawkinsonwb Skills

Brandon's reusable skills for AI agents. Write each skill once in `skills/` and distribute the same files across harnesses using the open [Agent Skills format](https://agentskills.io/specification).

## Baseline skills

| Skill | Purpose |
| --- | --- |
| [noodle](skills/noodle/SKILL.md) | Plan a focused product outcome or discuss its implementation, with optional tasks. |
| [noodle-big](skills/noodle-big/SKILL.md) | Explore a broad product initiative and agree on milestones and connected tasks. |
| [work](skills/work/SKILL.md) | Build scaffolding, align core logic with the user, then implement and validate. |
| [code-review](skills/code-review/SKILL.md) | Review requirements and code, with a consistent architecture overview and concise inline findings. |
| [follow-up](skills/follow-up/SKILL.md) | Resume work, with a dedicated guide for PR review feedback. |
| [setup-hawkinsonwb-skills](skills/setup-hawkinsonwb-skills/SKILL.md) | Configure workspace and repository guidance, including a work tracker. |

Run `setup-hawkinsonwb-skills` in your workspace first, then use `noodle` → `work` → `code-review` → `follow-up`. Choose `noodle-big` for broad product planning. Invocation syntax depends on your harness; you can also ask it to use a skill by name.

The setup skill records tracker, repository, and workflow conventions in `AGENTS.md` (or your harness's existing equivalent). Skills read those conventions across repositories. With no tracker available, they can keep work in local Markdown tickets. Publishing tickets, posting reviews, and merging follow the user's authorization and the workspace's rules.

`noodle` has separate product and implementation planning guides. `work` includes user checkpoints before consequential core logic and sign-off on cross-repository contracts. Each skill includes the supporting instructions it needs when installed alone.

`code-review` uses its [architecture overview guide](skills/code-review/references/architecture-overview.md) for consequential architectural changes or an explicitly requested overview. Routine changes skip this step. The guide defines evidence-backed diagrams of module boundaries, data flow, and cross-repository contracts, with matching before/after views for architectural changes.

## Install

The skills CLI below covers supported harnesses. Native Codex, Copilot, Gemini, Pi, Devin, Qoder, and Grok packaging, plus optional Cline/Cursor/Kiro/Windsurf discovery rules, are documented in [harness packaging](docs/harness-packaging.md). All consume the canonical skills. Gemini uses the shared `AGENTS.md` context.

Requires Node.js with npm/npx and Git. Run project installs from the project that should receive the skills.

```bash
# Choose skills and agents interactively (project scope)
npx skills@latest add hawkinsonwb/Skills

# Global: all skills, every supported agent, without prompts
npx skills@latest add hawkinsonwb/Skills --all --global

# Project: all skills, every supported agent, without prompts
npx skills@latest add hawkinsonwb/Skills --all

# One agent, globally (replace codex with an ID below)
npx skills@latest add hawkinsonwb/Skills --skill '*' --agent codex --global

# One skill (replace my-skill with an existing name)
npx skills@latest add hawkinsonwb/Skills --skill my-skill --agent codex
```

| Harness | Agent ID |
| --- | --- |
| Codex | `codex` |
| Claude Code | `claude-code` |
| Gemini CLI | `gemini-cli` |
| Antigravity | `antigravity` |
| Cursor | `cursor` |
| GitHub Copilot | `github-copilot` |
| OpenCode | `opencode` |
| Amp | `amp` |
| Cline | `cline` |
| Roo Code | `roo` |
| Windsurf | `windsurf` |
| Continue | `continue` |
| Kiro CLI | `kiro-cli` |

For every other harness and its installation paths, use the maintained [supported-agent list](https://github.com/vercel-labs/skills#supported-agents). The CLI handles destination paths. Global availability requires a harness that supports global skills.

### Claude Code plugin

Alternatively, install the entire collection as a native plugin:

```text
/plugin marketplace add hawkinsonwb/Skills
/plugin install hawkinsonwb-skills@hawkinsonwb-skills
```

Choose either the plugin or the skills CLI for Claude Code to avoid duplicate skills. Plugin discovery uses the same `skills/` directory. See [Claude's marketplace documentation](https://code.claude.com/docs/en/plugin-marketplaces).

## Add a skill once

Create `skills/my-skill/SKILL.md` with this structure, replacing the example with real instructions:

```markdown
---
name: my-skill
description: Describe what the skill accomplishes and when an agent should use it.
---

# My Skill

Write the guidance the agent needs to complete this task.
```

Use a unique lowercase name with digits and single hyphens, at most 64 characters, matching its folder. Add `scripts/`, `references/`, or `assets/` inside that folder only when needed. Link references from the instructions and resolve paths relative to the skill directory.

Keep the core instructions independent of any model or harness. Document required tools and isolate optional harness-specific metadata inside the skill. A shared file format does not make a harness-specific tool available everywhere.

Commit and push the folder. Both installation methods discover it without per-skill registration. This layout and the multi-agent installer approach are inspired by [mattpocock/skills](https://github.com/mattpocock/skills/).

## Contributing

These guidelines apply when editing this repository. Projects using the installed skills retain their own workspace conventions.

- Keep each skill's canonical instructions in `skills/<name>/SKILL.md`. Add a skill once; harness packaging consumes that collection directly.
- Follow the [Agent Skills specification](https://agentskills.io/specification). Keep instructions portable, declare required tools, and bundle supporting resources inside the skill folder using relative references.
- Keep every skill usable when installed individually. Put examples in documentation rather than creating installable example skills.
- Update README installation instructions when distribution changes. Bump the version in `.claude-plugin/plugin.json` when releasing plugin changes.
- Edit the sources of generated files: `.claude-plugin/plugin.json` for release metadata, `docs/harness-context.md` for shared routing, and `docs/repository-conventions.md` for repository guidance. Regenerate the harness files and `AGENTS.md`, then commit them with their source changes.

### Generate and validate

Harness metadata, optional discovery rules, and shared `AGENTS.md` context are generated from `.claude-plugin/plugin.json`, `docs/harness-context.md`, `docs/repository-conventions.md`, and the canonical skills:

```bash
python3 scripts/build-harness-files.py
python3 scripts/build-harness-files.py --check
python3 -m unittest discover -s tests
```

Run generation after adding, renaming, or changing skills or release metadata. Commit the generated files with the source changes. The check reports missing or stale files without modifying them.

## Develop and update

```bash
# From this checkout, install unpublished changes into selected agents
npx skills@latest add .

# Refresh skills installed from GitHub
npx skills@latest update
```

Installed files are separate from this checkout; rerun the local install after edits. For a private repository, use an authenticated Git URL such as `git@github.com:hawkinsonwb/Skills.git` as the source.

### Other agents and manual installation

Copy the **whole skill folder**, including its resources, into the harness's documented skill directory. Alternatively, link each skill folder from a stable local checkout; edits then remain visible through that link. Repeat installation when adding a new folder.

For a harness without native skills, attach or load `SKILL.md` as task instructions and make its resources available explicitly. This provides the guidance, but automatic discovery and invocation depend on the harness. For hosted UIs that accept skill archives, package one whole skill folder per archive and follow that product's upload instructions.

## License

[MIT](LICENSE).
