# Routing and calibration

Use two independent classifications:

- **Mode** says what outcome is needed: `map`, `plan`, `resume`, `status`, `publish`, or `check`.
- **Depth** says how much ceremony and durable output are justified: `probe`, `bounded`, `architectural`, or `portfolio`.

Use these classifications internally and in checkpoints. Explain their effect in the user's terms when it matters:

```text
This changes one existing flow, so a short design here should be enough.
```

The user may override routing. Lead with the work, not process labels. Say when discovered scope changes the intended output or persistence.

For `resume`, `status`, and `publish`, inherit the persisted session depth. For `check`, classify depth from the approved baseline and implementation surface. If either is missing, report `Depth: UNDETERMINED` as a transient preflight result rather than misclassifying missing inputs as `probe`.

## Enter and leave questioning

On implicit activation, inspect the supplied context first. Do not start a session for an already-clear, straightforward task. When material gaps do require a conversation, a brief one-time offer to proceed with stated defaults is appropriate; do not offer it automatically when the user explicitly requested Grill or a design discussion.

If the user asks to stop questioning, honor that even in an explicitly invoked session:

- Stop the interview. Briefly state what is settled, what remains unknown, and any material defaults the user delegated to you.
- Continue the normal workflow only if the user has requested that work, and only within that scope and delegation. A bare "stop" or cancellation is not an implementation request. A missing essential fact, access, or authority still blocks the affected action; do not invent it or resume a broad interview.
- Do not mark unanswered decisions as accepted or a draft as `APPROVED`. Approval of one recommendation is not approval of an unseen design. Preserve earlier approved baselines.
- If state already exists, set `session.questioning: stopped`, retain unresolved nodes and approval state, and record the next authorized action. Do not create persistence solely to record an opt-out. Explicit resumption reactivates questioning; ordinary later tasks do not.

## Mode precedence

1. Honor an explicit subcommand.
2. Infer an explicit natural-language action such as "continue last time", "publish the ADR", or "check this implementation".
3. Resume a uniquely identifiable active session when that is clearly the subject; do not implicitly resume one whose questioning was stopped.
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
| `light` | 1–2 decisions | Keep intent questions open; offer practical defaults for concrete choices and challenge material assumptions |
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
