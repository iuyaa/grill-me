---
name: grill
description: "Clarify requirements and stress-test plans through targeted questions in dependency order. Use when key gaps, ambiguities, or conflicts in a request cannot be resolved from available context or authorized investigation and require user input or a decision; when the user wants assumptions, risks, or tradeoffs challenged; when a large goal needs decomposition into dependent decisions; or when resuming or publishing a decision session or checking implementation against an approved plan."
metadata:
  version: "2.1.0"
---

# Grill

Surface the decisions hidden inside an idea, resolve them in dependency order, and leave an approval boundary that later work can verify. Do not make the user choose a workflow before they can use the skill.

## Check for updates before use

At the first use in each conversation, before starting or resuming a decision session, follow [updates.md](references/updates.md). Check the official Grill repository for a newer version; when permitted and the local installation is unmodified, back it up, update the complete skill, and reread its entrypoint and required references before proceeding. Respect offline, pinned-version, and no-write instructions. If checking or safely updating is unavailable, briefly report that and continue with the installed version. Do not repeat checks between question rounds or recursively after rereading the updated skill.

## Interpret the invocation

`/grill <problem>` or `$grill <problem>` is the canonical entry. Infer the mode and depth internally, then begin with useful findings or the most consequential unanswered question. Explain scope or artifact choices in plain language when they affect the user; do not require a mode/depth announcement. Explicit modes override inference:

- `map`: decompose a portfolio-sized goal into dependent decision tickets.
- `plan`: resolve one decision, feature, or design into an approved brief or spec.
- `resume`: continue a persisted session.
- `status`: summarize resolved, ready, blocked, deferred, and out-of-scope decisions.
- `publish`: promote an approved session into the project's durable documentation.
- `check`: compare implementation evidence with an approved baseline.

If no mode is explicit, use `check` for conformance requests, `resume` for a named or uniquely active session, `map` for work too large for one coherent spec, and `plan` otherwise. Do not ask the user to select a mode when a reasonable route is available. Read [routing.md](references/routing.md) when starting or rerouting a session.

For implicit activation, first inspect the available context. If a straightforward request is already clear, carry out the authorized task without starting a Grill session. Explicit requests to discuss or stress-test still get a proportionate review; do not invent missing decisions to prolong it. Follow the entry and exit rules in [routing.md](references/routing.md) when the user wants to skip or stop questioning.

## Preserve authority boundaries

- Facts are the agent's job. Inspect the provided repository, documents, and authorized sources instead of asking the user for discoverable facts.
- Respect decision ownership. Preserve user decisions; make choices within an explicit delegation and identify them as agent decisions with reasons. Other recommendations remain proposals, not approval. Routine process choices are the agent's job within the authorized scope.
- Use the user's language for the session. Follow established project language and terminology for durable artifacts unless the user asks otherwise.
- `/grill` authorizes questioning and proportionate read-only investigation in the supplied scope. It does not by itself authorize implementation, commits, pushes, issue creation, external writes, production access, or destructive probes.
- The pre-use upgrade is limited maintenance of this Skill installation under the host's permissions; it does not authorize changes to the user's project or its `.grill/` sessions. In an explicitly read-only task, check for updates but leave the installation unchanged.
- While a `plan` or `map` session continues, do not implement until the user approves the presented design. A request to both design and implement still pauses for that exact approval. If the user ends questioning, use the exit rules in [routing.md](references/routing.md); leaving the session does not approve its draft.
- An explicitly authorized disposable experiment follows the `probe` rules in [plan.md](references/plan.md); its result cannot silently become retained implementation.
- `check` is read-only by default. Report drift and the smallest repair proposal; modify implementation only after an explicit fix request.
- Never rewrite an approved baseline to make an implementation pass. A changed decision creates a new baseline version.

## Run a decision session

For `plan` or `map`, read [decision-engine.md](references/decision-engine.md) and the vendored [upstream-grilling.md](references/upstream-grilling.md). Use the upstream content only for its interrogation primitive; the routing, tools, persistence, approval, and evidence rules in this skill remain controlling. Never require or invoke a separately installed `grilling` skill.

1. Inspect context and establish a fact ledger before asking detailed questions.
2. Frame the destination and explicit scope.
3. Build a dependency graph of unresolved decisions.
4. Ask only material questions in the current frontier that context or investigation cannot answer. If the user's purpose is still unknown and matters to the design, start with an open question without suggested answers. For concrete choices, give explained options and a recommendation.
5. Wait for the user's answers. Record decision ownership, briefly reflect back each settled part for correction, recompute the graph, and repeat.
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

When waiting for a user decision or approval, stop. Do not fill in their answer or describe the session as approved. An explicit request to end questioning uses the exit rules; it is not successful completion of an unapproved plan.
