# COM7014 Project Brain

This is the control centre for the project. It combines the reusable quality controls from the Master's assignment system with the specific requirements extracted from the COM7014 learning materials.

## Two-layer model

- `PUBLIC/` contains publication-safe project governance and status information. It is versioned in the public GitHub repository.
- `PRIVATE/` exists only in the local workspace. It contains the assignment contract, detailed lesson synthesis, rubrics, supervisor notes, ethics records, decision history, project log, source ledger, topic analysis, risks, results, and publication review queue. The parent repository ignores the entire directory.

The private layer is itself a local Git repository so internal work has history without being sent to GitHub.

## Working rule

Every material change must leave evidence in the correct layer:

| Event | Public record | Private record |
|---|---|---|
| Publication-safe milestone | `PUBLIC/CHANGELOG.md` | `PRIVATE/PROJECT_LOG.md` |
| Scope or method decision | Sanitised summary if useful | `PRIVATE/DECISION_LOG.md` |
| New external source | Only if cited publicly | `PRIVATE/SOURCE_LEDGER.md` |
| Result | Only after verification and approval | `PRIVATE/RESULTS_LEDGER.md` first |
| Supervisor or tutor instruction | Never verbatim by default | `PRIVATE/SUPERVISION_LOG.md` |
| Potentially publishable file | After clearance | `PRIVATE/PUBLICATION_REVIEW_QUEUE.md` |

## Authority order

1. Current assessment brief and submission portal
2. Current rubric or marking matrix
3. Current tutor and supervisor instructions
4. Approved ethics and proposal documents
5. Dataset and artefact constraints
6. Confirmed assignment control file
7. COM7014 lesson materials
8. Reusable Assignment Brain and older projects

## Current gate

The working topic is selected and recorded in [`TOPIC.md`](../TOPIC.md). Assessed drafting, data collection, and artefact development remain blocked until the missing brief, rubric, and required proposal and ethics approvals are in place.
