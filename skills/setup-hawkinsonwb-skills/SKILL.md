---
name: setup-hawkinsonwb-skills
description: Set up workspace and repository agent guidance for the Hawkinsonwb Skills workflow, including repository boundaries, ticket tracking, validation, and review conventions. Use when adopting the skills across a project or workspace.
---

# Setup Hawkinsonwb Skills

Configure the conventions that let planning, work, review, and follow-up operate across repositories. Required tools: workspace file reading and editing. Tracker access is optional; record its connector or CLI only if it actually exists.

## Discover

Inspect existing workspace and repository guidance, repository roots, project documentation, and available tracker configuration. Prefer the existing canonical instruction file. The common filename is `AGENTS.md`; if the user calls it `AGENT.md`, clarify only when the filename choice matters to their harness. Preserve an existing harness equivalent such as `CLAUDE.md` and arrange a supported reference to shared guidance rather than duplicating it.

Find the workspace root and repositories involved in the project without scanning unrelated personal directories. Read relevant root and nested instructions. Preserve existing conventions and user edits; explain conflicts before making a consequential change.

## Fill consequential gaps

Ask a compact set of questions only for information not established by existing configuration:

- Which tracker and project should hold tasks? What ticket hierarchy, fields, and statuses are used? If no external tracker is desired, where should local Markdown tickets live?
- Which repositories belong to the workspace, and how are cross-repository tasks and dependencies represented?
- What defines ready, done, and handoff? Which validation, branch, PR, and review conventions apply?
- Which tracker/PR actions are already authorized, and which require the user to request them? Preserve existing authorization rather than broadening it during setup.

Do not ask the user to disclose credentials in chat. If integration is unavailable, record the access gap and local fallback; do not claim an account connection or tracker provisioning occurred.

## Write workspace guidance

Create or update the workspace's canonical guidance with the confirmed repository map, tracker and project identifiers, ticket location/format, workflow states, cross-repository dependency convention, handoff expectations, and authorization boundaries. Mark unknowns as unresolved rather than supplying fictional defaults.

Keep shared conventions at workspace scope and repository-specific commands and constraints in each repository's guidance. Use relative references where the harness supports them. For repositories outside the instruction file's discovery scope, add an explicit supported pointer or the minimum necessary local guidance so those sessions can find the workspace context. Respect each harness's actual loading behavior; a file's existence alone does not prove it is loaded.

Keep these instructions short and specific to this workspace. Explain the workflow briefly: `noodle` offers product and implementation planning, `noodle-big` shapes a product initiative, `work` aligns core logic and cross-repository contracts with the user before delivery, `code-review` checks requirements, architecture, and code, and `follow-up` resumes work or handles review feedback.

## Verify and hand off

Check every documented repository path and guidance reference. Verify commands against repository configuration where possible without running unrelated workloads. Use read-only checks to confirm tracker/project access if available. Report files changed, confirmed configuration, unresolved access or decisions, and how sessions in each repository discover the shared instructions.

Finish when the configured workspace can locate its guidance and track an actual task, or when the remaining human-owned setup steps are explicitly identified. Setup configures future work; it does not create product tickets or start implementation without a request.
