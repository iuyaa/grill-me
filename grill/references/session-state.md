# Session state

Persist only when needed: `architectural` and `portfolio` depth, explicit save/resume requests, or checks whose baseline must survive the current context. Keep `probe` and ordinary `bounded` work in chat by default.

## Location and files

Use the project root if it can be identified; otherwise use the current working directory. Before the first write, announce the intended location:

```text
.grill/<session-slug>/
```

Typical contents:

```text
checkpoint.yaml
spec.md
decision-map.md
tickets/
check-report.md
```

Use the templates under `assets/templates/`. Adapt existing files rather than overwriting unrelated content. Do not commit, push, create external issues, or modify canonical project docs unless that action is separately requested or approved.

## Checkpoint contract

The checkpoint is operational state, not the final project source of truth. It should contain:

- session identity, mode, depth, pressure, and state;
- destination and scope boundary;
- fact ledger with evidence pointers;
- decision graph and current frontier;
- deferred and out-of-scope nodes;
- artifact paths and versions;
- approval status, exact baseline version, and digest when available;
- the next safe action.

Do not persist raw secrets, credentials, personal data copied from sources, hidden reasoning, or a full chat transcript. Store only the minimum decisions, rationale, evidence pointers, and recovery context.

## State model

Track three independent status axes so publishing and checking do not erase design state:

```text
design:       DRAFT → DESIGN_PRESENTED → APPROVED
publication:  UNPUBLISHED → PUBLISHED
conformance:  UNCHECKED → CHECKED
```

- `DRAFT`: decisions or evidence remain open.
- `DESIGN_PRESENTED`: a complete candidate is awaiting approval.
- `APPROVED`: the user approved an exact chat design or spec version.
- `PUBLISHED`: that approved version was promoted to agreed canonical docs.
- `CHECKED`: an implementation was compared with the approved baseline.

Publishing requires `design: APPROVED`. Checking requires an approved baseline but does not require publication.

Implementation is an external lifecycle event, not permission granted by the checkpoint. Record implementation references when observed, but do not infer authorization from the state.

Changing an approved decision creates a new draft version and resets publication and conformance for that new version. Preserve the previous approved baseline and its check reports; never mutate history so an old implementation appears conformant.

## Approval record

For persisted specs record:

```yaml
approval:
  status: approved
  approved_at: 2026-09-03T10:00:00+08:00
  approved_by: user
  baseline_version: 1
  baseline_digest: sha256-of-approved-spec
```

Use the actual timestamp and digest. If the exact approved content exists only in chat, record a concise immutable summary and label the lack of a file digest.

## Resume and status

On `resume`:

1. Locate the named or uniquely relevant session.
2. Reload its files and verify referenced artifacts still exist.
3. Reinspect drift-prone facts when cheap and material.
4. Summarize the destination, resolved decisions, current frontier, blockers, and next action.
5. Continue from the frontier; do not replay settled questions unless evidence or scope changed.

On `status`, remain read-only. Report counts and named items for `decided`, `ready`, `blocked`, `deferred`, and `out_of_scope`, plus approval and artifact versions.

Before updating state, re-read the current file. If it changed concurrently, merge only when identities and versions make the merge unambiguous; otherwise stop and report the conflict.
