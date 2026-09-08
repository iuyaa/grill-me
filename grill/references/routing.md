# Routing and calibration

Use two independent classifications:

- **Mode** says what outcome is needed: `map`, `plan`, `resume`, `status`, `publish`, or `check`.
- **Depth** says how much ceremony and durable output are justified: `probe`, `bounded`, `architectural`, or `portfolio`.

Announce both before the first decision question:

```text
Mode: PLAN · Depth: BOUNDED · Reason: this changes one existing flow and can be approved in chat.
```

The announcement is a reversible routing decision, not a question. The user may override it.

For `resume`, `status`, and `publish`, inherit the persisted session depth. For `check`, classify depth from the approved baseline and implementation surface. If either is missing, report `Depth: UNDETERMINED` as a transient preflight result rather than misclassifying missing inputs as `probe`.

## Mode precedence

1. Honor an explicit subcommand.
2. Infer an explicit natural-language action such as "continue last time", "publish the ADR", or "check this implementation".
3. Resume a uniquely identifiable active session when that is clearly the subject.
4. Classify the supplied problem by scope.
5. Default to `plan` when evidence does not justify a heavier route.

If `/grill` has no payload:

1. Use the clear subject already present in the conversation.
2. Resume when exactly one relevant active session exists.
3. If several sessions are plausible, show their titles and statuses and ask which one.
4. If there is no subject or session, ask what idea, plan, or decision the user wants to clarify.

Do not silently replace or merge an unrelated active session.

## Mode classifier

| Signal | Mode |
| --- | --- |
| Broad destination spanning multiple independently decidable domains or multiple sessions | `map` |
| One coherent feature, design, policy, or decision | `plan` |
| Compare actual implementation with an approved intent | `check` |
| Continue, inspect, or summarize existing session state | `resume` or `status` |
| Promote approved decisions into durable project knowledge | `publish` |

If a proposed `plan` expands beyond one coherent spec, announce the discovered scope and upgrade to `map`. If a `map` investigation proves small enough for one spec before a map is persisted, recommend continuing as `plan`.

## Depth classifier

| Depth | Test | Default artifact |
| --- | --- | --- |
| `probe` | The outcome is a feasibility finding or recommendation, not retained implementation | Chat report; temporary artifacts stay explicitly throwaway |
| `bounded` | A well-scoped change to an existing, inspectable flow | Short design and approval in chat; persist only when requested or needed to resume |
| `architectural` | New subsystem, new project, shared interface change, durable data or security boundary, or multi-component restructuring | Persisted session plus versioned spec; ADR or domain model only when warranted |
| `portfolio` | Several coherent specs or sessions are required to reach the destination | Persisted decision map and tickets |

`UNDETERMINED` is not a fifth depth. It means a non-planning mode lacks the evidence needed to apply this table; resolve the missing precondition before classifying.

Familiarity with a technology does not make a new system `bounded`. Base the classification on the actual repository and change surface.

### Upgrade ratchet

Hidden complexity may upgrade `probe → bounded → architectural → portfolio`. Announce the evidence and stop lightweight work before proceeding at the heavier depth. Do not downgrade merely to avoid artifacts or approval. Before persistence, an initial `portfolio` guess may return to `architectural` when investigation shows the whole destination fits one spec.

## Pressure calibration

Pressure changes interaction style, not correctness:

| Pressure | Frontier slice | Challenge style |
| --- | --- | --- |
| `light` | 1–2 decisions | Lead with a practical default; challenge only material assumptions |
| `normal` | 2–4 related decisions | Explain primary trade-offs and failure modes |
| `hard` | Entire manageable frontier | Stress-test assumptions, counterexamples, reversibility, and edge cases |

Honor an explicit pressure request. Otherwise start at `normal` and adjust from user feedback. Do not infer that seniority warrants hostility. Never omit a material risk because pressure is light.

## Artifact policy

- `probe`: do not create a spec or retained implementation.
- `bounded`: keep the design in chat unless persistence is requested or the session will span contexts.
- `architectural`: use `.grill/<session>/` working state, then publish approved material into project conventions.
- `portfolio`: persist the map and ticket records; use an external tracker only when the user authorized those external writes.
- `check`: report in chat for a small check; persist beside the session when the baseline is persisted or the user requests a report.

Routing never grants mutation authority. Announce the intended persistence location before the first write.
