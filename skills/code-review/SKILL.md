---
name: code-review
description: Review product requirements, architectural changes, and code correctness in a PR or change set, and produce concise evidence-backed findings, preferably inline.
---

# Code Review

Read repository/workspace guidance and the originating requirements. Fix the review target and comparison base, then inspect the diff and affected callers. For PRs, refresh the revision, existing threads, and checks using available PR tools.

## Product requirements review

Map acceptance criteria to behavior and validation. Check user journeys, scope boundaries, and relevant failure cases. Report missing or contradictory behavior. If requirements are unavailable, identify that review gap and continue the technical review.

## Implementation review

### Architectural changes

First check the diff for consequential changes to module/service boundaries, shared contracts, data flow, storage, deployment topology, or cross-repository dependencies. Run this portion only when such a change affects system behavior, compatibility, performance, or operation, or when the user requests an architecture review. Routine local fixes, refactors within existing contracts, styling, and documentation changes can proceed directly to code review without an architecture overview.

When needed, use the [architecture overview guide](references/architecture-overview.md) to explain the affected boundaries and dependencies. Reuse verified context and scope new diagrams to the architectural change rather than remapping the whole system.

Assess performance implications and departures from the existing architecture. Use the guide's matching before/after views for meaningful changes, explain the rationale supported by code or design records, and document the impact on callers, operation, and future changes. Label an inferred rationale and ask about an unexplained consequential change.

### Code review

Check correctness, performance, security implications, maintainability, and readability. Read surrounding code and tests; run targeted checks where useful. Ground each concern in a realistic trigger and distinguish newly introduced defects from existing issues.

## Findings and disposition

Prioritize by severity and impact. Give each finding a precise location, concrete evidence, resulting behavior, and an actionable correction. Separate confirmed issues from potential concerns and optional improvements. Keep comments concise and specific.

When posting is authorized, prefer inline PR comments on the current diff over a large general comment. Use a short summary for overall disposition, architecture diagrams, and review limits; avoid duplicating inline findings. If a finding has no valid inline location or PR tools are unavailable, provide a concise located finding locally or in the authorized summary.

Keep review read-only unless fixes are requested. Approve only when requested or already authorized and the current revision has no unresolved blockers with sufficient review evidence. Approval does not authorize merging. State when no actionable issue was found and which behavior remains unverified.
