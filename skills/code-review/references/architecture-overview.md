# Architecture overview

Create an evidence-backed view of the system around a consequential architectural change or when the user explicitly requests an overview. Load this guide after the parent review identifies changes to boundaries, shared contracts, data flow, storage, topology, or dependencies that affect system behavior or operation. Routine changes within the existing architecture do not require this guide or a diagram. Requires repository/document read tools and the fixed review base and target revisions. Mermaid source is sufficient when rendering tools are unavailable.

## Establish the system

1. Identify affected repositories, their responsibilities, and the user or external entry points involved. Start with repository guidance and architecture records, then verify them against code at the reviewed revision.
2. Identify meaningful modules by responsibility and public contract, rather than drawing every file or class. Read entry points, imports, callers, API/schema definitions, messaging configuration, and storage access to trace the relevant flow end to end.
3. Follow dependencies across repository boundaries. Record who produces and consumes each contract, how data moves, and which versions or deployment order must agree. If another repository is unavailable, mark that boundary unverified and identify the missing evidence.
4. Define the view's scope: which behavior it explains and which neighboring systems it only shows as context. Include enough context to explain the change, without implying that an affected slice is the entire system.

## Use a consistent visual format

Use a Mermaid `flowchart LR` with these conventions:

- One labeled subgraph per repository; module nodes inside it carry their responsibility names. Show external actors/services outside repository groups and label them explicitly.
- Use ordinary boxes for modules/services and cylinder nodes for data stores. Keep the same node identifiers, names, grouping, and level of detail across revisions.
- Use solid directed arrows for runtime calls, events, or data movement. Label them with the operation or payload and transport when relevant. Orient arrows in the direction of the action: caller to callee, publisher to channel to consumer, writer to store. Label response edges separately when needed to explain behavior.
- Use dashed directed arrows for build/package dependencies, from consumer to dependency. Keep them distinct from runtime flow and include a brief legend. Omit them when there is no relevant build dependency.
- Split a crowded view by user journey or responsibility using the same conventions. Explain ordering, retries, or failure behavior in short accompanying prose when a static arrow cannot capture it.

For architectural changes, show **Before** at the fixed comparison base and **After** at the target revision. Retain identifiers for unchanged modules and explicitly describe added, removed, and changed boundaries or edges. For an explicitly requested overview of unchanged architecture, one current view with a statement of the verified scope is sufficient. Prefer portable diagrams over a harness-specific renderer; when Mermaid rendering is unavailable, provide the source with a short textual walkthrough.

## Ground the overview

Accompany the diagram with a compact evidence table:

| Element or contract | Responsibility / producer → consumer | Source at reviewed revision | Change or impact |
| --- | --- | --- | --- |

Populate it from observed modules and contracts. Cite file paths and symbols or lines, or revision-specific source links when available. Mark inference and inaccessible evidence explicitly; a diagram must not turn an assumption into a confirmed connection.

Explain the architectural delta and its consequences: ownership, compatibility, runtime hops, latency or throughput, failure propagation, security boundaries, and rollout coordination where affected. Separate observed effects from risks needing measurement. Explain documented rationale; label inferred rationale.

## Verify the view

Check every depicted module, edge, and contract against the relevant revision. Ensure the before view reflects the base rather than today's code. Reconcile the diagram, evidence table, and review findings; inspect Mermaid syntax with an available renderer if practical.

Finish when the user can follow the relevant path across modules and repositories, understand what changed and why, and locate the supporting evidence. Return unknowns as review limitations. Keep diagram context in the concise review summary and concrete defects in inline findings when posting is authorized.
