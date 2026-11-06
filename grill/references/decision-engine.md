# Dependency-aware decision engine

Use this protocol for `plan` and `map` alongside the vendored [upstream-grilling.md](upstream-grilling.md). The upstream reference supplies the basic design-tree and frontier primitive; this protocol controls its integration and completion rules.

## Separate facts, assumptions, and decisions

- A **fact** is discoverable from the authorized environment or a reliable source. Record its evidence.
- An **assumption** is currently unverified. Investigate it or label it; do not promote it to fact.
- A **decision** requires human authority, preference, risk acceptance, or a trade-off among viable options.

Do not ask the user which database the repository currently uses when the repository answers it. Do ask whether a new subsystem should continue using that database when this is a real design choice.

Read-only fact finding can proceed without a separate approval gate. Production access, paid calls, external writes, prototypes with side effects, and destructive probes require their normal authorization.

Keep user decisions, delegated agent choices, and unaccepted proposals distinct. Within an explicit delegation, choose sensible defaults grounded in the existing project, state the choice and reason, and record the delegation's scope. Otherwise keep a material recommendation open until accepted. Silence or outcome-focused language alone is not delegation. Do not ask the user to manage routine investigation, formatting, or file-placement choices already covered by project conventions and authorization.

When fact finding is delegated to a subagent, use a fresh context with only the question, relevant sources, constraints, and required evidence. Do not inherit the full conversation. Delegate only when useful and allowed by the host and user; the vendored upstream does not require spawning a subagent for every lookup.

## Understand intent before offering choices

Read the supplied context and relevant project material before the first substantive question. Preserve settled decisions. For a detailed request, briefly reflect the intent and relevant findings, then ask about the most consequential remaining gap. For a vague request, start there directly.

Ask only when the answer changes the outcome, scope, acceptance criteria, or material design choice and neither context nor proportionate investigation resolves it. If the purpose is still unknown and matters to those choices, ask one open question in the user's vocabulary, without suggested answers, options, or a recommendation about what they should want. Already-known intent does not need reconfirming. Explain what the answer would change when that is not obvious.

Explore goals, constraints, prior examples, and anti-goals only as relevant, not as a fixed questionnaire. An anti-goal is a result that would count as failure even if the feature worked, such as saving sales time by shifting excessive data entry onto salespeople. Record it as a constraint or acceptance criterion when it matters.

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
decided_by: null
delegation: null
rationale: null
reversibility: reversible
impact: []
```

Valid decision states are `open`, `ready`, `blocked`, `decided`, `deferred`, and `out_of_scope`.

For a resolved node, `decided_by` is `user` or `agent`. Agent decisions require `delegation` to identify the user's instruction and its scope; unresolved proposals leave both fields empty. Do not retroactively attribute old decisions without evidence. A delegated decision can unblock successors, but does not approve the final baseline.

The **frontier** is every open decision whose decision prerequisites are decided and whose required factual prerequisites are available. Do not place a question in the current round if its answer depends on another question still open in that round.

## Work the frontier

1. Recompute node states from dependencies.
2. Select a coherent frontier slice using the configured pressure level. Settle an open purpose question before batching downstream choices.
3. Research discoverable facts needed by that slice. Continue with unrelated ready decisions while slow research is pending when tools and permissions allow.
4. Ask the slice and wait.
5. Record the answers, decision ownership, and rationale without silently expanding them.
6. Add, remove, or rewire downstream nodes exposed by the answers.
7. Repeat until no in-scope blocking decisions remain.

For concrete decisions with meaningful alternatives, prefer the host's structured user-input UI when available and within its question and option limits. Put the recommended option first. For open intent questions, use a free-text question without options, in the host UI if supported or in chat. Otherwise use the text format below; do not switch modes solely to obtain a menu.

Give every option a short title and a brief explanation of what choosing it means and its main benefit, cost, or trade-off. Use separate title/label and description fields when the host supports them. If the host accepts only option strings, include both in each string, separated by a newline when supported or a short separator otherwise. In text questions, put each explanation directly below its option title.

Use this shape for a concrete choice question, adapting detail to the decision:

```text
❓ Q1 — First-release users

I recommend serving internal sales only in the first release. Shall we use that scope?

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

Offer options only when they are genuinely distinct. For a concrete recommendation, word the question so "yes" clearly accepts it. This does not apply to open intent questions. In a multi-question round, do not treat an ambiguous bare "yes" as approval of every recommendation; ask which item it refers to unless the user's answer clearly accepts the whole set. A selected option or clear acceptance resolves that decision, not an unseen design or unrelated action.

## Reflect and make ideas concrete

When a coherent part is settled, briefly play it back and invite correction before exploring the next branch. Distinguish what the user said, choices you made under delegation, and proposals still open. Scale the recap to the decision; do not add a fixed-length summary or separate approval ceremony after every answer.

When a layout, flow, or behavior is hard to express, use a small text sketch or an authorized visual tool to make the choice concrete. Offer a disposable prototype or experiment when it can resolve a real unknown more cheaply than more questions. Keep it limited to that unknown, bring its findings back to the frontier, and follow the experiment boundaries in [plan.md](plan.md). No browser companion or extra skill is required.

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
