---
name: balise-trustworthy-flows
description: Audits and repairs consequential decisions in selected Figma flows—including consent, permissions, subscriptions, pricing, cancellation, destructive actions, and data sharing—by reconstructing the flow, locating observable decision risks, comparing choice symmetry, and creating clearly labeled alternatives without claiming runtime behavior or legal compliance.
---

# Trustworthy Flows for Figma

Protect a person's ability to understand, choose, refuse, leave, revoke, and recover across consequential product flows. Audit the decision system, not the visual polish of one screen.

Do not call other skills or depend on references, scripts, assets, or files outside this document.

## Core rules

1. Preserve source frames, components, libraries, prototype links, and annotations unless the user explicitly asks to edit them.
2. Work within the selection and the adjacent path needed to understand entry, commitment, outcome, exit, revocation, and recovery.
3. Reuse existing components, variants, properties, variables, styles, Auto Layout, tokens, naming, and product language.
4. Separate **observed**, **prototype-verified**, **declared**, **hypothetical**, and **proposed** evidence.
5. Never infer intent from the interface. Describe the visible mechanism and plausible consequence.
6. Never invent price, stock, urgency, social proof, consent persistence, deletion, notification, permission, analytics, or backend behavior.
7. Do not diagnose a person's cognitive bias. State that the presentation may exploit or amplify a known bias.
8. Do not declare an interface legal, compliant, safe, accessible, or free of manipulation from a Figma file.
9. Preserve legitimate protective friction. Challenge friction that appears to serve only the product's preferred choice.
10. Use synthetic data. Never place real personal, financial, health, authentication, research, or client data in test frames.
11. If entry, commitment, or exit is missing, produce a partial finding and open questions. Never invent a branch.
12. Route serious legal, privacy, accessibility, financial, child-safety, or coercive-control risks to qualified review.

## Infer the mode

- **Audit:** reconstruct and report without editing.
- **Compare:** compare selected branches, alternatives, or versions against one contract.
- **Repair:** create the smallest cooperative correction after explicit edit intent.
- **Design:** design a new consequential flow with disclosure, choice, exit, and recovery.
- **Verify:** exercise visible prototype paths and report evidence and unknowns without editing.

Default ambiguous review requests to **Audit**. Audit and Verify are read-only. Repair and Design create labeled copies by default. Edit a source frame or shared component only on explicit instruction.

## Follow the decision workflow

### 1. Frame the decision

Determine from the prompt, selection, and canvas:

- the person's documented goal before the request or interruption;
- the decision and its immediate trigger;
- the available options, including refuse, defer, leave, customize, or do nothing;
- the immediate and delayed consequences for money, data, access, time, rights, content, and relationships;
- the platform, audience, jurisdiction, sector, and vulnerability context when known;
- the requested mode and deliverable.

Ask one concise question only when a missing fact would materially change the analysis or authorize an edit. Otherwise proceed with explicit unknowns.

### 2. Inspect the Figma system

Inspect:

- selected layers, parent frame, section, and adjacent flow;
- alternate branches and post-decision screens;
- components, instances, component sets, variants, and properties;
- variables, modes, styles, and design tokens;
- Auto Layout, dimensions, constraints, and layout guides;
- prototype connections and interactive components;
- annotations, naming conventions, and representative content.

Do not infer runtime behavior from layer names. An absent frame does not prove that production behavior is absent.

### 3. Reconstruct the smallest complete flow

Map:

`entry → request → disclosure → choice → commitment → confirmation → outcome → exit → revocation → recovery`

Include back, refusal, interruption, failure, re-entry, and post-decision controls when they affect the choice.

If a critical branch is absent, label the map **Partial** and list the unknown. Do not treat a proposed reconstruction as observed behavior.

### 4. Build a decision contract

For each consequential moment, record:

| Field | Question |
| --- | --- |
| User goal | What was the person trying to accomplish before this request? |
| Decision | What choice is the interface asking them to make? |
| Options | Can they accept, refuse, defer, customize, exit, or do nothing? |
| Material disclosure | Which price, recurrence, data, recipient, condition, loss, or right may change the choice? |
| Disclosure timing | Does that information appear before commitment and while it remains useful? |
| Default | What is selected initially and what happens without action? |
| Consequences | What changes now and later? |
| Comparative effort | How many steps, how much search and reading, and which channel or delay does each branch require? |
| Exit and revocation | How can the person refuse, cancel, withdraw, export, delete, or revoke later? |
| Recovery | Can they undo, correct, restore, or escalate? |
| Provenance | Where do price, stock, urgency, recommendation, or social proof come from? |
| Evidence | Is the point observed, prototype-verified, declared, hypothetical, or proposed? |

### 5. Evaluate eight trust dimensions

1. **Comprehension:** object, terms, options, and consequences are understandable when they matter.
2. **Autonomy:** the primary goal remains possible without an unnecessary forced detour, hidden penalty, or undue pressure.
3. **Symmetry:** accept, refuse, defer, leave, and revoke have proportionate visibility and effort.
4. **Transparency:** cost, recurrence, data use, recipients, conditions, and limits appear before commitment.
5. **Predictability:** labels, controls, and conventions truthfully announce their effect.
6. **Reversibility:** undo, correction, cancellation, withdrawal, or recovery matches the risk.
7. **Proportion:** friction protects against a concrete risk using the least restrictive approach.
8. **Protection:** the flow considers contextual vulnerability and plausible abuse without increasing exposure.

### 6. Diagnose the mechanism

Use the mechanism before the pattern name:

| Mechanism | Signals |
| --- | --- |
| **Perception** | low contrast, small type, peripheral placement, competing movement, false grouping |
| **Comprehension** | jargon, double negative, fragmentation, mental calculation, memory across screens |
| **Decision** | anchoring, defaults, loss framing, unverifiable proof, artificial scarcity |
| **Expectation** | familiar control with unexpected outcome, misleading label, moving target |
| **Resource depletion** | repetition, delay, interruption, excessive steps, time pressure |
| **Forcing** | account, data, permission, consent, or sharing blocks the primary task |
| **Emotion** | shame, guilt, fear, regret, or social threat makes refusal punitive |
| **Compulsion** | autoplay, infinite feed, streak, variable reward, or missing stopping cue |

Write the diagnostic chain:

`localized observation → mechanism → trust dimension → plausible consequence → evidence or unknown → remediation`

Do not report a color difference as a deceptive pattern without explaining its role in the complete choice.

### 7. Use pattern labels as secondary vocabulary

The vocabulary is living and non-exhaustive:

| Pattern | Core question |
| --- | --- |
| Addictive Design | Can the person see and control time, spend, pause, and completion? |
| Comparison Prevention | Can options be compared in one structure using the same units and terms? |
| Confirmshaming | Is refusal framed as shameful, irresponsible, or socially costly? |
| Currency Confusion | Is the real monetary equivalent visible before commitment? |
| Disguised Ads | Is the commercial source identifiable before interaction? |
| Fake Scarcity | Is limited supply accurate, scoped, and dated? |
| Fake Social Proof | Are activity and endorsements authentic, contextualized, and sourced? |
| Fake Urgency | Is the deadline real and is its outcome explained? |
| Forced Action | Is the secondary action necessary for the requested function? |
| Hard to Cancel | Is cancellation materially harder than signup? |
| Hidden Costs | Is the total mandatory price visible before comparison and commitment? |
| Hidden Subscription | Are recurrence, first charge, renewal, and cancellation clear? |
| Nagging | Does the system respect a refusal already expressed? |
| Obstruction | Are exit, refusal, correction, export, or deletion unnecessarily difficult? |
| Preselection | Does the default commit the person to a consequential product-preferred option? |
| Sneaking | Is a charge, product, data use, or condition introduced without adequate awareness? |
| Trick Wording | Does the label directly describe action and consequence? |
| Visual Interference | Does salience match importance and consequence rather than product preference? |

Do not force every finding into one label. Multiple mechanisms may combine across the flow.

### 8. Prioritize proportionally

Consider consequence, exposure, detectability, reversibility, recovery cost, contextual vulnerability, cumulative mechanisms, and evidence strength.

- **Critical:** plausible or observed grave consequence with high exposure or very difficult recovery, such as unauthorized charge, irreversible loss, sensitive-data exposure, effective inability to withdraw, or serious safety risk. Recommend a validation pause and qualified review; do not claim authority to block.
- **Major:** autonomy is substantially reduced through strong asymmetry, late material disclosure, repeated pressure, or obstruction, but exit remains possible.
- **Moderate:** trust or comprehension is weakened by ambiguity, questionable hierarchy, missing provenance, or localized friction without a demonstrated grave consequence.

The presence of cost, consent, deletion, or a vulnerable audience does not automatically make a finding Critical. Do not create a numerical score that implies scientific precision.

### 9. Repair cooperatively

Preserve the legitimate product objective while restoring informed choice.

#### Disclose

- Show total price, mandatory fees, recurrence, first charge, renewal, data use, recipients, and consequential limits before commitment.
- Keep decision-critical information visible. Do not rely on a tooltip or hidden detail for the essential fact.

#### Compare

- Use direct labels and stable order for accept, refuse, defer, customize, cancel, and delete.
- Compare branches by visibility, steps, search, reading, authentication, channel, and delay.
- Match salience and effort to consequence, not commercial preference. Pixel-identical controls are not universally required.

#### Ask actively

- Avoid preselection for significant cost, recurring commitment, data use, permission, or waiver.
- Use a safe default when inaction could harm the person.

#### Respect refusal

- Persist the refusal.
- Ask again only after a meaningful and explainable context change.
- Do not substitute an indefinite “later” for a durable refusal.

#### Enable exit and revocation

- Place cancellation, withdrawal, export, deletion, and permission management in the expected context.
- State effective date, retained access, future charge status, and data consequence.
- Avoid repeated retention offers, artificial channel switching, or unnecessary authentication.

#### Prevent and recover

Prefer, in order:

1. prevent the error;
2. make the action reversible;
3. support review and correction;
4. add a precise confirmation when the action remains rare and irreversible.

Use explicit verbs, identify the affected object, and show undo, trash, grace period, or recovery when supported by the product.

#### Preserve protective friction

Keep asymmetric friction only when it protects against a concrete risk, is necessary and minimally restrictive, applies consistently to comparable risks, does not merely serve conversion, and preserves a clear exit.

### 10. Create the Figma work area

When editing is authorized, create a clearly labeled area near the source:

```text
Trustworthy Flows — [flow]
├── Source
├── Decision map
├── Findings
├── Cooperative alternative
├── Prototype evidence
└── Open product, technical, accessibility, safety, and legal questions
```

Then:

- duplicate source frames for proposals;
- align opposing branches for visual and step comparison;
- reuse components, variants, properties, variables, styles, and tokens;
- preserve Auto Layout and content-driven sizing for decision-critical copy;
- use representative synthetic values;
- label every frame and annotation with evidence level;
- prototype only transitions that can be built and checked reliably;
- annotate persistence, backend effect, data provenance, analytics, and accessibility behavior that Figma cannot prove.

Do not detach instances, flatten layers, create a parallel design system, or modify a shared main component without explicit authorization.

## Evidence levels

- **Observed:** visible in the inspected frames or prototype; point to the exact location.
- **Prototype-verified:** reproduced through an inspected prototype connection; this still does not prove production behavior.
- **Declared:** supplied by an annotation or prompt but not verified.
- **Hypothetical:** explicit inference or missing-path question.
- **Proposed:** alternative design or behavior not implemented.

Only Observed and Prototype-verified support factual statements about the Figma artifact. Declared, Hypothetical, and Proposed remain qualified.

## Accessibility and safety boundaries

For consequential moments, inspect visible error identification, labels and instructions, correction, duplicate prevention, target separation, help placement, status feedback, and recovery when they affect the decision.

Figma can show intention and some dimensions. It cannot prove focus, semantics, keyboard behavior, announcements, zoom, reflow, assistive-technology support, or WCAG conformance.

If a monitored device, coercive actor, child, or high-risk population may be involved, flag and route the risk. A notification, history, log, or obvious emergency exit can expose a person seeking help. Preserve the source and do not invent a quick-escape or hidden-history pattern without specialist threat research.

## Legal boundary

Regulatory sources have different jurisdictions and scopes. A Figma finding may be compatible with a source category but cannot establish applicability, violation, valid consent, or compliance.

Use:

> This flow presents a deceptive-design risk compatible with category X in source Y. The visible evidence is A, B, and C. The proposal reduces the risk by changing D. This design analysis is not legal advice or a compliance certification.

Do not say:

- “This is illegal.”
- “The consent is valid.”
- “This design is compliant.”
- “No deceptive pattern exists.”
- “The user was manipulated.”

## Verify the proposal

Re-run both directions where represented:

- accept and refuse;
- enter and leave;
- subscribe and cancel;
- grant and revoke;
- delete and recover;
- commit and correct;
- normal, error, interruption, back, and repeated-request paths.

Check that each created route has a visible outcome, no dead end, and an annotation for every behavior outside the file.

## Report completion

End with:

1. scope and mode;
2. reconstructed flow and missing branches;
3. findings by severity and exact location;
4. mechanism, affected dimension, plausible consequence, and evidence level;
5. alternatives created or recommended;
6. prototype paths checked;
7. runtime, accessibility, safety, and legal reviews still required;
8. residual risk and open decisions.

If no material risk is found, state which paths and decision conditions passed. Do not claim that the entire product is trustworthy.

## Completion standard

Finish only when:

- the relevant flow, not one isolated screen, has been inspected;
- entry, commitment, outcome, exit, and recovery are mapped or marked missing;
- every finding is localized and evidence-labeled;
- mechanism and consequence are explained without inventing intent;
- opposing paths and post-decision controls are compared;
- source frames remain preserved unless direct editing was authorized;
- alternatives preserve legitimate product value without preserving exploitation;
- prototype claims remain separate from runtime claims;
- serious safety risks are routed rather than improvised;
- no legal or accessibility certification is claimed.
