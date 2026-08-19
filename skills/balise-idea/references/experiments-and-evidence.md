# Experiments and evidence

## Hypothesis card

Write the uncertainty before choosing a method:

```text
We believe [actor/context] will [observable behavior or outcome]
because [mechanism].
We will learn from [signal and source].
We would interpret [result] as [bounded implication], not as proof of [larger claim].
The test cannot establish [out-of-scope claim].
Cost/time/ethical limit:
Stop or escalation condition:
Decision to inform:
```

Good hypotheses are specific enough to be contradicted. Separate desirability, usefulness, usability, feasibility, viability, legitimacy, safety, timing, and implementation assumptions when a single test would otherwise produce an ambiguous signal.

## Choose the smallest informative test

Select by the uncertainty and mechanism, not by habit or a catalogue:

1. What decision is blocked?
2. What evidence would materially change it?
3. Which observable is closest to the claimed mechanism?
4. What is the cheapest reversible way to observe it?
5. What biases, selection effects, demand effects (participants changing behavior because they infer the test’s purpose), and missing cases remain?
6. What stronger or different test is needed if the early signal is promising?

Possible methods include contextual conversation, observation, artifact critique, paper or service prototype, a test entry point for a feature that does not exist yet (a “fake door”), a feature stub, concierge/manual service, landing page, pre-order or commitment, technical spike, controlled comparison, or analysis of existing behavior. Match the method to the question. An interview does not establish behavior; a prototype reaction does not establish durable use; and an A/B test does not automatically explain a mechanism.

## Hard gates and incident triggers

For sensitive, regulated, or high-stakes work, or whenever key facts or permissions are missing, do not run user-facing experiments, collect new sensitive data, train on restricted material, or change production without consent, authority, provenance, privacy, safety, clinical, legal, or ethics review. Set the status to `hold` or `stop`, name the accountable specialist route, and restrict learning to an authorized offline or synthetic exercise that cannot expose people or alter live decisions.

If an observed error or signal could create material harm, compliance exposure, privacy leakage, safety risk, or an irreversible consequence, pause the affected exposure and preserve the evidence. Record the incident trigger, owner, containment and rollback authority, and reopening condition. IDEA must not silently authorize rollback or incident closure; route those decisions to the accountable operational, legal, security, medical, research-ethics, or domain owner.

Before a high-stakes case can move out of `hold` or `stop`, complete these fields: risk class; affected or vulnerable population; exposure and version; accountable specialist owner; consent/assent and permitted-use status. Also record the incident ID, or an explicit reason there is none; containment status; rollback authority; reopening condition; and the review label mapped to a native IDEA state. For minors or clinical use, also record age band, guardian/assent requirements, jurisdiction, clinical and safeguarding owners, red-flag symptoms, emergency handoff, and harm thresholds. Missing fields are not evidence of safety.

## Read evidence in context

Record sample, setting, recruitment, exposure, comparison, measure, timing, missing data, and alternative explanations. Keep contradictory evidence visible. “Positive” means only that the observed signal met the declared interpretation in that context.

Use evidence states such as:

`unexamined → hypothesis → planned → observed → inconclusive | partially supported | contradicted`

Then choose a separate decision state: `reframe`, `hold`, `deepen`, `experiment`, `proceed`, `pivot`, `abandon`, or `stop`.

Do not use `validated` without defining the claim, scope, evidence strength, and remaining uncertainty. A decision can be rational without evidence being complete; record that it is a conditional decision and what would reopen it.

## Sensitive or under-documented tests

Do not expose people to material harm, deceptive commitments, privacy leakage, regulated advice, or irreversible changes for the sake of learning. Pause when consent, authority, data provenance, safety, or downstream impact is unclear. Escalate to legal, security, medical, research-ethics, data, or domain specialists as appropriate.
