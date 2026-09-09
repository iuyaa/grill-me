---
name: grill
description: "Clarify requirements and stress-test plans through targeted questions in dependency order. Use when key gaps, ambiguities, or conflicts in a request cannot be resolved from available context or authorized investigation and require user input or a decision; when the user wants assumptions, risks, or tradeoffs challenged; when a large goal needs decomposition into dependent decisions; or when resuming or publishing a decision session or checking implementation against an approved plan."
---

# Grill

Surface the decisions hidden inside an idea, resolve them in dependency order, and leave an approval boundary that later work can verify. Do not make the user choose a workflow before they can use the skill.

## Interpret the invocation

`/grill <problem>` or `$grill <problem>` is the canonical entry. Infer the mode and depth, announce them in one short line with the reason, then begin useful work. Explicit modes override inference:

- `map`: decompose a portfolio-sized goal into dependent decision tickets.
- `plan`: resolve one decision, feature, or design into an approved brief or spec.
- `resume`: continue a persisted session.
- `status`: summarize resolved, ready, blocked, deferred, and out-of-scope decisions.
- `publish`: promote an approved session into the project's durable documentation.
- `check`: compare implementation evidence with an approved baseline.

If no mode is explicit, use `check` for conformance requests, `resume` for a named or uniquely active session, `map` for work too large for one coherent spec, and `plan` otherwise. Do not ask the user to select a mode when a reasonable route is available. Read [routing.md](references/routing.md) when starting or rerouting a session.

## Preserve authority boundaries

- Facts are the agent's job. Inspect the provided repository, documents, and authorized sources instead of asking the user for discoverable facts.
- Decisions belong to the user. Recommend a choice and explain why, but do not silently convert the recommendation into approval.
- Use the user's language for the session. Follow established project language and terminology for durable artifacts unless the user asks otherwise.
- `/grill` authorizes questioning and proportionate read-only investigation in the supplied scope. It does not by itself authorize implementation, commits, pushes, issue creation, external writes, production access, or destructive probes.
- Do not implement until the user has approved the presented design. An earlier request to both design and implement still pauses at this gate so the user can approve the exact design.
- `check` is read-only by default. Report drift and the smallest repair proposal; modify implementation only after an explicit fix request.
- Never rewrite an approved baseline to make an implementation pass. A changed decision creates a new baseline version.

## Run a decision session

For `plan` or `map`, read [decision-engine.md](references/decision-engine.md) and the vendored [upstream-grilling.md](references/upstream-grilling.md). Use the upstream content only for its interrogation primitive; the routing, tools, persistence, approval, and evidence rules in this skill remain controlling. Never require or invoke a separately installed `grilling` skill.

1. Inspect context and establish a fact ledger before asking detailed questions.
2. Frame the destination and explicit scope.
3. Build a dependency graph of unresolved decisions.
4. Ask only the current frontier: decisions whose prerequisites are settled. Give options when they are real, plus a recommendation, rationale, reversibility, and material impact.
5. Wait for the user's answers. Record them, recompute the graph, and repeat.
6. When no in-scope blocking decisions remain, synthesize the design at the selected depth and ask for explicit approval.

Ask one dependency frontier at a time, not necessarily one question at a time. Calibrate batch size and challenge level without weakening evidence or hiding risk.

## Load only the active mode

- For `plan`, read [plan.md](references/plan.md).
- For `map`, read [map.md](references/map.md).
- For `resume`, `status`, or any persistent `plan`/`map`, read [session-state.md](references/session-state.md).
- For `publish`, read [publish.md](references/publish.md) and [session-state.md](references/session-state.md).
- For `check`, read [check.md](references/check.md); also read [session-state.md](references/session-state.md) when the baseline is persisted.

Use the templates under `assets/templates/` when creating durable artifacts. Adapt them to existing repository conventions rather than duplicating a project source of truth.

## Completion rules

A session is not complete merely because questioning stopped.

- `map` completes when the destination, decision tickets, dependencies, frontier, fog, and out-of-scope boundary make the route navigable.
- `plan` completes when every in-scope blocking decision is resolved or explicitly deferred, acceptance criteria are testable, the design is presented, and the user approves it.
- `publish` completes when the approved version is written to the agreed canonical locations and reported; it never implies commit or push.
- `check` completes when each acceptance criterion has a result and evidence, unrun verification is labeled, and remaining risk is stated.

When waiting for a user decision or approval, stop. Do not fill in their answer, continue into implementation, or describe the session as approved.
