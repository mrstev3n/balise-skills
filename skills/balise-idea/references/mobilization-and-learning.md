# Mobilization and learning loops

## Decision states

Choose the smallest defensible state:

- `abandon`: the opportunity, mechanism, or evidence no longer justifies work;
- `hold`: important uncertainty or dependency remains, with a reopening condition;
- `stop`: the current test, exposure, or action must end because a safety, authorization, or other hard gate is not met;
- `reframe`: the problem, actor, context, or mechanism changed;
- `deepen`: research or comparison is still the highest-value next move;
- `experiment`: a bounded learning action is ready;
- `proceed`: enough evidence and readiness justify a specified next implementation step;
- `pivot`: the evidence supports a materially different opportunity or mechanism.

Do not choose `deepen` merely because work can continue. Use it only when further research or comparison could change the decision.

## Review labels are not approvals

If an external review uses `SHIP`, `FIX-FIRST`, or `RETHINK`, translate it to IDEA’s native state rather than treating it as a release decision:

- `SHIP` may mean `experiment` or `proceed` only when authorization, safety, reversibility, and evidence scope are explicit;
- `FIX-FIRST` means `hold` or `deepen` until the named gap is closed;
- `RETHINK` means `reframe`, `pivot`, or `stop` depending on the evidence.

None of these labels overrides the hard gates in [experiments-and-evidence.md](experiments-and-evidence.md), authorizes a production change, or closes a high-stakes incident.

## Readiness brief

When the user asks to move an idea into execution, keep the brief narrow:

```text
Desired learning/result:
Non-goals:
Current evidence and limits:
First reversible action:
Learning milestones:
Owner / participants / missing authority:
Dependencies and resources:
Risks and affected people:
Stop, pause, or escalation criteria:
Review date or trigger:
```

This is a readiness and learning brief, not a full project plan, business plan, fundraising deck, backlog, or delivery schedule. Route detailed implementation, architecture, legal, security, finance, marketing, or operations work to specialists.

## Short execution loop

1. State the result and non-goals.
2. Perform the smallest authorized reversible action.
3. Observe the declared signal and record surprises/contradictions.
4. Compare the result with the hypothesis and its scope.
5. Revise the idea, opportunity, or test.
6. Decide whether to proceed, pivot, reframe, hold, or stop.

Every loop should leave a concise decision record. Do not claim completion from a plan, a prototype, a local test, or an unreviewed artifact alone.

## Stop and route

Stop or escalate when evidence is contradictory and the stakes are high, the user’s authorization is insufficient, data provenance is uncertain, a vulnerable population may be affected, the action is irreversible, or a specialist decision is required. State the blocker concretely and preserve the safe next option.
