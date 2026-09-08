# Check mode

Use `check` to verify implementation conformance against an exact approved baseline. It is evidence gathering, not a second design session and not automatic repair.

## Preconditions

Identify:

- the approved spec or exact approved chat design;
- its version and digest when persisted;
- the implementation scope and revision being checked;
- the acceptance criteria and explicit non-goals.

If there is no approved baseline, return `MISSING_BASELINE`. Offer to reconstruct a draft through `plan`, but do not pretend a conversation fragment is approved. If a persisted spec digest differs from its approval record, return `BASELINE_CHANGED` and resolve which version is authoritative before judging implementation.

## Evidence ledger

Map every acceptance criterion to evidence and one result:

- `PASS`: sufficient evidence shows conformance.
- `DRIFT`: implementation contradicts the baseline.
- `MISSING_EVIDENCE`: the criterion may be satisfied, but available evidence cannot establish it.
- `SPEC_GAP`: implementation exposes a decision the approved baseline never made.
- `NOT_RUN`: required verification was not executed.
- `OUT_OF_SCOPE`: observed behavior is outside this baseline and is not scored.

Use the strongest proportionate evidence available: source inspection, focused static analysis, tests, builds, real runtime interaction, logs, or deployment evidence. Never inflate a static/type/build pass into runtime, browser, migration, production, or cutover proof.

For each criterion record:

```text
ID | Requirement | Result | Evidence | Observed behavior | Remaining risk
```

Re-fetch or re-read all members before evaluating batch or compound behavior. When required access, fixtures, services, or credentials are unavailable, label the affected checks rather than substituting fabricated evidence.

## Classify drift

Distinguish:

- implementation defect: approved behavior was not delivered;
- intentional but unapproved change: implementation chose a different behavior;
- spec gap: no approved answer exists;
- evidence gap: the behavior cannot currently be verified;
- baseline drift: the supposedly approved document changed.

Do not rewrite the spec to recategorize an implementation defect as intended behavior. A desired intent change goes back through `plan` and creates a new baseline version.

## Report and repair boundary

Report totals, blocking items, exact verification commands or interactions, unrun checks, and remaining risk. Use `assets/templates/check-report.md` for a persisted report.

Recommend the smallest repair that would restore conformance, but do not edit code or docs unless the user explicitly asks for a fix. If repair is authorized:

1. preserve the original check report;
2. implement against the same approved version unless the user approves a new one;
3. rerun affected checks plus proportionate regression;
4. issue a new report rather than overwriting the old result.

`check` completes when every criterion is classified, not necessarily when every criterion passes.
