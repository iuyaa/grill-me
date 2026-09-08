# Publish mode and spec review

`publish` promotes an approved decision session into durable project knowledge. It is not a synonym for dumping the conversation into files.

## Choose existing project conventions

Inspect the repository for existing sources such as `AGENTS.md`, `CONTEXT.md`, architecture docs, ADR directories, domain models, RFCs, or feature specs. Preserve their ownership and format. Avoid creating a second source of truth when an established location exists.

Route content by meaning:

| Content | Durable destination |
| --- | --- |
| Local feature behavior and acceptance criteria | Feature spec or approved plan |
| Cross-task vocabulary, stable facts, and standing constraints | Existing context or glossary document |
| Costly-to-reverse technical choice affecting multiple consumers | ADR or equivalent decision record |
| Entities, relationships, states, lifecycle, and invariants | Domain model |
| Session mechanics, frontier, and recovery context | `.grill/<session>/checkpoint.yaml` only |

Do not create an ADR for every answer. Do not write volatile session state into a long-lived context file.

## Review before approval

Before presenting the exact spec for approval, check it for:

1. unfinished markers or vague requirements;
2. contradictions between decisions, architecture, and acceptance criteria;
3. requirements with multiple plausible interpretations;
4. unverified assumptions presented as facts;
5. missing consumer, migration, authorization, failure, or rollback impact when relevant;
6. acceptance criteria that cannot be mechanically or observably checked;
7. scope too broad for one implementation plan;
8. open decisions that still block the destination.

Correct mechanical inconsistencies. Return substantive gaps to the decision frontier; do not decide them on the user's behalf.

## Exact approval and versioning

Ask the user to approve the exact reviewed content. On approval:

- mark the baseline `APPROVED`;
- assign a monotonically increasing version;
- compute a digest when a spec file exists;
- record approval time and user authority;
- preserve earlier approved versions or their immutable history.

Any substantive post-approval edit returns the new version to `DRAFT` or `DESIGN_PRESENTED` until approved again. Formatting-only edits may retain the decision version, but the file digest must reflect the actual content used by `check`.

## Perform the publish

An explicit `publish` request authorizes the scoped documentation writes needed for the agreed destinations. It does not authorize code changes, commit, push, issue-tracker mutation, or unrelated doc cleanup.

After publishing, report:

- session and approved version;
- files created or updated;
- whether context, ADR, or domain model was intentionally not needed;
- validation performed;
- anything left uncommitted or unverified.

Use `assets/templates/spec.md` as a fallback when the project has no established spec format.
