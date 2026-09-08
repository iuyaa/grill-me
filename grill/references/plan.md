# Plan mode

Use `plan` for one coherent decision, feature, policy, or design. Its output is approved intent, not implementation.

## Start from the actual context

Inspect the current repository or supplied materials before detailed questioning. Prefer existing conventions and consumer contracts. Record relevant file paths, commands, source links, or observed runtime evidence in the fact ledger. Do not treat static code as proof of runtime behavior.

State the destination in one or two sentences:

- what will be true when this plan succeeds;
- who or what observes that success;
- the current scope boundary.

Then use the dependency-aware protocol in [decision-engine.md](decision-engine.md).

## Scale by depth

### Probe

Answer a feasibility question as cheaply as correctness permits. A read-only inspection does not need another permission round. Announce and obtain authorization before any side-effectful experiment. Report:

- the question tested;
- evidence gathered;
- conclusion and confidence;
- limitations;
- recommendation.

Any created experimental implementation is throwaway and cannot silently become production work.

### Bounded

Confirm that an existing flow can be inspected and the change stays within a small, understood boundary. Present a concise design in chat with:

- intended behavior and non-goals;
- affected components or files at the level currently knowable;
- error and edge behavior;
- verification approach.

Ask for explicit approval. Do not create a formal spec unless requested or persistence is needed.

### Architectural

Persist session state. When meaningful alternatives exist, present two or three approaches with trade-offs and lead with the recommendation; do not manufacture alternatives for appearance. Apply YAGNI to each approach.

The selected design should cover only relevant dimensions, typically:

- components and ownership boundaries;
- public interfaces and consumers;
- data model, lifecycle, and migration;
- authorization, privacy, and audit boundaries;
- failure handling and recovery;
- observability and operational constraints;
- testing and acceptance evidence;
- rollout and rollback when change risk warrants them.

Draft the spec from `assets/templates/spec.md`, run the review in [publish.md](publish.md), and ask the user to approve the exact version.

## End state

An approved plan must identify:

- its destination and non-goals;
- facts and their evidence;
- decisions and rationale;
- unresolved non-blocking deferrals;
- observable acceptance criteria;
- baseline version or exact approved chat design.

Approval does not itself authorize implementation unless the user already requested implementation. Even then, hand control back after approval so the implementation phase starts from the approved baseline.
