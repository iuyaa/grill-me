# Dependency-aware decision engine

Use this protocol for `plan` and `map` alongside the vendored [upstream-grilling.md](upstream-grilling.md). The upstream reference supplies the basic design-tree and frontier primitive; this protocol controls its integration and completion rules.

## Separate facts, assumptions, and decisions

- A **fact** is discoverable from the authorized environment or a reliable source. Record its evidence.
- An **assumption** is currently unverified. Investigate it or label it; do not promote it to fact.
- A **decision** requires human authority, preference, risk acceptance, or a trade-off among viable options.

Do not ask the user which database the repository currently uses when the repository answers it. Do ask whether a new subsystem should continue using that database when this is a real design choice.

Read-only fact finding can proceed without a separate approval gate. Production access, paid calls, external writes, prototypes with side effects, and destructive probes require their normal authorization.

## Represent the graph

Keep facts and decision nodes separate. Each decision node should be able to answer:

```yaml
id: D-001
question: Which users are in the first release?
depends_on: []
status: open
options: []
recommendation: null
decision: null
rationale: null
reversibility: reversible
impact: []
```

Valid decision states are `open`, `ready`, `blocked`, `decided`, `deferred`, and `out_of_scope`.

The **frontier** is every open decision whose decision prerequisites are decided and whose required factual prerequisites are available. Do not place a question in the current round if its answer depends on another question still open in that round.

## Work the frontier

1. Recompute node states from dependencies.
2. Select a coherent frontier slice using the configured pressure level.
3. Research discoverable facts needed by that slice. Continue with unrelated ready decisions while slow research is pending when tools and permissions allow.
4. Ask the slice and wait.
5. Record the user's answers and rationale without silently expanding them.
6. Add, remove, or rewire downstream nodes exposed by the answers.
7. Repeat until no in-scope blocking decisions remain.

Prefer the host's structured user-input UI when it is available in the current mode and the frontier slice fits its question and option limits. Put the recommended option first. Otherwise use the text question format below; do not switch modes solely to obtain a menu.

Give every option a short title and a brief explanation of what choosing it means and its main benefit, cost, or trade-off. Use separate title/label and description fields when the host supports them. If the host accepts only option strings, include both in each string, separated by a newline when supported or a short separator otherwise. In text questions, put each explanation directly below its option title.

Use this shape for each question, adapting detail to the decision:

```text
❓ Q1 — First-release users

Which audience should the first release serve?

A. Internal sales only (Recommended)
   Keeps the first release focused on validating the internal workflow with a simpler access model.

B. Internal sales and partners
   Supports collaboration, but requires partner access controls and lead-sharing rules.

C. All customers
   Tests customer self-service, but adds onboarding, support, and access-control work to the first release.

➡️ Recommendation: A.

Why: it validates the workflow without exposing an unproven authorization model externally.
Reversibility: reversible, but expanding later requires role and audit decisions.
Impact: permissions, onboarding, support, and acceptance tests.
```

Offer options only when they are genuinely distinct. Prefer reaction to a reasoned proposal over a blank question. A recommendation is not a decision until the user accepts it.

## Avoid false completeness

Do not attempt to enumerate every imaginable future choice. The graph is complete for the current destination when:

- all reachable, in-scope blocking decisions are `decided`;
- deferrals name an owner or trigger and do not block the stated destination;
- out-of-scope items have an explicit boundary reason;
- acceptance criteria are observable or their verification is explicitly unavailable;
- assumptions and unresolved evidence gaps are visible;
- the next authorized action is clear.

If a suspected future question cannot yet be phrased precisely, keep it as fog in a `map`; do not invent a premature ticket.

## Synthesize before approval

When the frontier is clear, convert the decision history into one coherent design:

- `probe`: state the finding, evidence, limitations, and recommendation.
- `bounded`: present a short design covering approach, affected boundaries, error behavior, and verification.
- `architectural`: present genuine alternative approaches when they exist, recommend one, then cover components, interfaces, data flow, failure handling, security boundaries, migration, and testing in proportion to risk.
- `portfolio`: produce the navigable map; do not pretend the individual tickets are resolved.

Show resolved decisions, explicit defaults, deferred items, out-of-scope items, and remaining evidence gaps. Ask the user to approve the synthesized result. Stop and wait; do not continue into implementation.
