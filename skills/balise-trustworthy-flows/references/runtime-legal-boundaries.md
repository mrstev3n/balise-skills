# Runtime, legal, and source boundaries

Load this reference whenever a finding touches implementation evidence, accessibility, privacy, regulation, or jurisdiction.

## Static evidence boundary

A design, screenshot, or specification may show visible intent. It cannot by itself prove:

- persisted refusal, consent, cancellation, or permission;
- actual charge, renewal, inventory, deadline, recommendation, or activity;
- deletion across backups and third parties;
- access control, encryption, retention, or revocation;
- runtime focus, semantics, keyboard support, announcements, or target behavior;
- comprehension, behavioral effect, or absence of harm;
- legal compliance.

Request source code, rendered-product evidence, logs, test results, data provenance, or specialist review according to the claim.

## Legal workflow

Before applying a rule, identify:

1. country and territorial connection;
2. product and provider type;
3. sector and transaction type;
4. affected population;
5. data or tracking involved;
6. current source, date, and institutional status;
7. overlap or exclusion between applicable regimes.

Separate:

- observable design risk;
- source-compatible category;
- technical fact;
- legal qualification reserved for review.

Never convert guidance, a staff report, or a nonbinding policy analysis into a universal legal rule.

## Source-specific limits

### FTC

*Bringing Dark Patterns to Light* is a 2022 staff report from the US Federal Trade Commission. It documents consumer-protection concerns and enforcement examples; it is not a universal certification standard. Legal conclusions depend on facts and current US law.

Source: https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf

### OECD

*Dark Commercial Patterns* is nonbinding policy analysis. Use it for definition, mechanisms, harms, evidence, and policy context, not to declare legality.

Source: https://www.oecd.org/en/publications/dark-commercial-patterns_44f5e846-en.html

### EDPB

Guidelines 03/2022 v2.0 address deceptive design patterns in social-media platform interfaces in the GDPR context. Use the six families as privacy-risk signals; do not infer a GDPR violation from a Figma frame.

Source: https://www.edpb.europa.eu/system/files/2023-02/edpb_03-2022_guidelines_on_deceptive_design_patterns_in_social_media_platform_interfaces_v2_en_0.pdf

### CNIL cookies and trackers

In the French tracker context, distinguish mandatory parity of effort from recommended presentation. Accept and refuse should have the same degree of simplicity; withdrawal should be as simple as giving consent. Same-screen placement and comparably readable, salient buttons are strongly recommended. Pixel-identical controls are not a universal requirement. Cookie walls require contextual assessment.

Recheck both sources at the time of analysis:

- consolidated recommendation: https://www.cnil.fr/sites/default/files/2026-01/recommandation_cookies_consolidee.pdf
- FAQ: https://cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies/FAQ

### EU Digital Services Act

Article 25 does not apply to every site or application. Check:

- territorial scope under Article 2;
- whether the provider is an online platform under Article 3(i);
- the Article 19 exclusion in principle for micro and small enterprises, including its exceptions such as VLOP designation;
- Article 25(2): Article 25 does not apply to practices covered by Directive 2005/29/EC or the GDPR. Exclusion from Article 25 does not make a practice lawful.

A Figma artifact cannot establish these legal conditions.

Source: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2065

## Accessibility scope

Apply each WCAG criterion only when its conditions hold. For consequential flows, commonly relevant WCAG 2.2 Understanding pages include:

- 3.3.1 Error Identification;
- 3.3.2 Labels or Instructions;
- 3.3.3 Error Suggestion;
- 3.3.4 Error Prevention (Legal, Financial, Data);
- 3.3.7 Redundant Entry;
- 2.5.2 Pointer Cancellation;
- 2.5.8 Target Size (Minimum);
- 3.2.6 Consistent Help;
- 4.1.3 Status Messages.

Index: https://www.w3.org/WAI/WCAG22/Understanding/

Do not describe this subset as complete accessibility conformance. Verify the implementation with keyboard and assistive technologies.

## Safe output language

Prefer:

> The observed flow presents a risk compatible with [category/source]. The visible evidence is [facts]. Confirm [runtime or jurisdictional dependency] before drawing a legal conclusion.

Avoid:

- “This is illegal.”
- “The consent is valid.”
- “This design is compliant.”
- “No dark pattern exists.”
- “The user was manipulated.”
