# Harness packaging

Audited against [Ponytail](https://github.com/DietrichGebert/ponytail/tree/6c97ffa48710714672214915ad092e3fc6e85516) on October 2, 2026. This collection provides six instruction-based skills. The `skills/` folders remain canonical, including all supporting references.

## Included packaging

| Surface | Files | Installation |
| --- | --- | --- |
| Claude Code | `.claude-plugin/plugin.json`, `marketplace.json` | README plugin commands |
| Codex | `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json` | Native marketplace commands below |
| Copilot CLI | Root `plugin.json` and the Claude marketplace | Native marketplace commands below |
| Gemini CLI | `gemini-extension.json`, `AGENTS.md` | Extension install below; loads `skills/` |
| Pi | `package.json` with `pi.skills` | Git package install below |
| Qoder | `.qoder-plugin/plugin.json`, optional `.qoder/rules/` | Local plugin loading or skills CLI |
| Devin | `.devin-plugin/plugin.json`, optional `.devin/rules/` | Git plugin install below |
| Grok Build | `.grok-plugin/marketplace.json`, root `plugin.json` | Marketplace install below |
| Cline | `.clinerules/hawkinsonwb-skills.md` | Optional workspace rule alongside installed skills |
| Cursor | `.cursor/rules/hawkinsonwb-skills.mdc` | Optional workspace rule alongside installed skills |
| Kiro | `.kiro/steering/hawkinsonwb-skills.md` | Optional workspace steering alongside installed skills |
| Windsurf | `.windsurf/rules/hawkinsonwb-skills.md` | Optional workspace rule alongside installed skills |
| Antigravity and compatible agents | `.agents/rules/hawkinsonwb-skills.md` | Optional rule where supported; install skills through CLI |

Rules provide discovery and routing; they contain neither copies of the full skills nor runtime hooks. Install the skills before using a copied rule. The skills CLI installs skills, not these optional rules. Copy only the named rule into the matching directory in a target workspace, preserving that workspace's existing files. Rules copied into other repositories are snapshots and must be refreshed after collection changes.

`AGENTS.md` is the shared routing context, including Gemini's configured extension context. Its maintenance section applies only when editing this repository. There is no separate Gemini context file.

## Native install alternatives

Use one installation method per harness to avoid duplicate skills. These commands work after the packaging changes are pushed to the remote repository.

```bash
# Codex
codex plugin marketplace add hawkinsonwb/Skills
codex plugin add hawkinsonwb-skills@hawkinsonwb-skills

# GitHub Copilot CLI
copilot plugin marketplace add hawkinsonwb/Skills
copilot plugin install hawkinsonwb-skills@hawkinsonwb-skills

# Gemini CLI
gemini extensions install https://github.com/hawkinsonwb/Skills

# Pi (Git install; this package is not published to npm)
pi install git:github.com/hawkinsonwb/Skills

# Devin CLI
devin plugins install hawkinsonwb/Skills

# Qoder: from this checkout, local plugin loading
qoder --plugin-dir .

# Grok Build
grok plugin marketplace add hawkinsonwb/Skills
grok plugin install hawkinsonwb-skills@hawkinsonwb-skills
```

For plugin enablement, reload behavior, feature flags, and installed-version compatibility, follow the host's documentation: [Codex](https://developers.openai.com/plugins/build/plugins), [Copilot CLI](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference), [Gemini](https://geminicli.com/docs/extensions/reference/), [Pi](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/packages.md), [Qoder](https://docs.qoder.com/cli/plugins-reference), [Devin](https://docs.devin.ai/cli/extensibility/plugins/overview), and [Grok Build](https://docs.x.ai/build/features/skills-plugins-marketplaces).

## Ponytail surfaces covered by existing skill installation

OpenCode, OpenClaw, Hermes, and other agents supported by the skills CLI consume the canonical skill folders. Use the README's `--agent` option with `opencode`, `openclaw`, or `hermes-agent`. OpenCode's [native skills support](https://opencode.ai/docs/skills/) needs no JavaScript plugin here. OpenClaw needs no duplicate `.openclaw/skills/` tree, and these skills have not been published to ClawHub. Hermes needs no `plugin.yaml` or Python lifecycle handlers for instruction-only installation.

Ponytail's `.opencode/plugins/`, `pi-extension/`, Hermes `plugin.yaml`/`__init__.py`, `hooks/`, MCP service, commands, and post-install scripting implement its runtime behavior. This collection has no such runtime, so those files have no corresponding role. Benchmark assets, translated READMEs, and product branding are also outside this packaging change. We do not publish an npm package or claim marketplace listing merely by adding manifests.

## Maintenance and verification

Edit `.claude-plugin/plugin.json` for release metadata, `docs/harness-context.md` for common routing wording, and `docs/repository-conventions.md` for repository maintenance instructions. Skill catalog entries come from each canonical `SKILL.md`. Run `python3 scripts/build-harness-files.py` and commit the generated results, including the shared `AGENTS.md`. `.agents/plugins/` and `.agents/rules/` are intentionally tracked; machine-local `.agents` content remains ignored.

Generation checks and isolated tests verify freshness, skill catalogs, version consistency, and canonical resource paths. Claude's native validator checks its marketplace and manifest. Other host formats are checked against their documented layout and parsed as JSON, but have not been installed end to end in every harness.
