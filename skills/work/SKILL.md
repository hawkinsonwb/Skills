---
name: work
description: Implement an agreed task with scaffolding first, user alignment on core logic, and acceptance validation. Use when the user is ready to deliver a planned change.
---

# Work

Requires repository editing and validation tools; use the configured tracker when available.

1. **Agree on the plan.** Read the task, acceptance criteria, and workspace/repository guidance. Inspect existing code and working changes. Identify the important behavior and decisions, then establish the implementation plan with the user. For work spanning repositories, map the producer/consumer changes, dependencies, and implementation order in the same plan. Present shared contracts—including data shapes, behavior, and compatibility where relevant—and obtain user sign-off before dependent implementation. Reuse explicit decisions already agreed in the conversation.
2. **Build the scaffolding.** Add the necessary models, contracts, signatures, and wiring before core logic. Keep unfinished paths clearly identified and safe; avoid adding boilerplate the task does not need.
3. **Align on core logic.** Show the scaffolding and explain how it supports the desired outcome. Present the consequential logic in plain language or pseudocode—for example, where the data query belongs, what it selects, and how failures behave. Ask for feedback and wait for alignment before implementing those decisions. Independent scaffolding or investigation may continue while waiting.
4. **Implement together.** Walk the user through meaningful pieces as they are built, explaining important choices against acceptance criteria. Keep cross-repository changes in the same task/thread, recording decisions and dependency status in the shared plan. If a shared contract changes, show the impact on every affected repository and obtain renewed alignment before dependent work continues. Routine edits within the agreed plan can continue.
5. **Validate and hand off.** Run required checks and verify each acceptance criterion, including producer/consumer compatibility and integrated behavior across affected repositories. Present the important resulting behavior for user review, incorporate adjustments, and summarize decisions, validation, rollout order, and remaining blockers. Complete the configured tracker/PR handoff within existing authorization.

For a minor change with no consequential behavior or workflow decision, explain the approach and result without requiring every checkpoint. Shared-contract changes still require sign-off. The user must still have an opportunity to review before finalizing. Do not treat silence as alignment when a checkpoint is required.

Preserve unrelated work and keep unfinished scaffolding out of a completed handoff.
