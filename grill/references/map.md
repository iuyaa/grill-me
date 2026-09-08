# Map mode

Use `map` when a destination requires several coherent specs or sessions. The goal is a navigable decision map, not a backlog of implementation tasks and not delivery of the destination.

## Name the destination first

Resolve what reaching the end of the map means. The destination might be an approved platform spec, a migration strategy, or a portfolio decision. It fixes what belongs on the route.

Explore breadth-first to surface independently decidable areas and their prerequisites. If the entire route fits one coherent spec, stop before persisting a map and recommend `plan`.

## Map model

The map is an index. A decision's detail lives in one ticket record; the map contains its title, state, dependency relationship, and a one-line gist after resolution.

Maintain:

- **Destination**: the outcome the map is finding a route toward.
- **Decisions so far**: links to resolved ticket records with one-line gists.
- **Frontier**: open, unblocked decisions that can be worked now.
- **Blocked**: precise tickets waiting on other tickets or factual prerequisites.
- **Not yet specified**: in-scope fog that cannot yet be phrased as a precise question.
- **Out of scope**: consciously excluded work and the boundary reason.

A question becomes a ticket when it can be stated precisely, even if it cannot yet be answered. Fog becomes tickets only when earlier resolutions make it precise.

## Decision tickets

Size one decision ticket for one focused session. Use these types only when useful:

- `research`: agent-led fact finding that unblocks a decision;
- `prototype`: a cheap artifact needed for a human design reaction;
- `decision`: human-in-the-loop resolution; the default;
- `prerequisite`: authorized work that must occur before a decision is possible.

Decision tickets are not implementation tickets. A prototype stays disposable unless separately approved for implementation. A prerequisite does not expand authorization to production or external systems.

Each ticket records:

```yaml
title: First-release business boundary
type: decision
question: Which business workflow must the first release complete end to end?
depends_on: []
status: ready
resolution: null
evidence: []
```

## Persistence target

Default to local files under `.grill/<session>/` using `assets/templates/decision-map.md` and `assets/templates/decision-ticket.md`. If the project already has a decision tracker, adapt to it after inspection.

The destination determines the session identity and map boundary. Before it is approved, announce the proposed persistence location but do not create an empty or misleading canonical map. Persist the initial map after the destination is resolved.

Creating or editing external issues is an external mutation. Do it only when the user explicitly requested or approved that tracker write. When using a tracker, preserve native parent/child and blocking relationships where available; do not duplicate full ticket resolutions into the map.

## Chart and work

To chart a map:

1. Resolve the destination and scope boundary.
2. Identify the first precise tickets and coarse fog.
3. Create ticket identities before wiring their dependencies.
4. Compute the first frontier.
5. Record the map and stop. Do not resolve a human decision while pretending only to chart.

To work a map:

1. Reload the map rather than relying on conversation memory.
2. Use a named ticket or select an unblocked frontier ticket.
3. Resolve that ticket with `plan`, using fact research or an authorized prototype as prerequisites.
4. Store the resolution in the ticket, update its one-line map gist, and recompute dependencies.
5. Graduate newly precise fog into tickets and move newly excluded work out of scope.

Default to one human decision ticket per focused session. Independent read-only research may proceed concurrently when the environment and authorization permit it.

## Completion

The map is complete when the destination is still valid, no unresolved ticket or fog blocks it, decisions so far form a coherent route, and the next phase can consume named approved outputs. It is not complete merely because all currently visible tickets are closed.
