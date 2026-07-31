# Interface Writing Patterns

Use this reference when reviewing, rewriting, generating, or implementing copy for common interface patterns.

## Contents

- Orientation and navigation
- Actions and links
- Forms and input
- Errors and recovery
- Empty states
- Onboarding and help
- Status and feedback
- Settings
- Confirmations and destructive actions
- Consent and sensitive content

## Orientation and Navigation

### Titles and Headings

- Name the place, decision, or task.
- Make heading hierarchy reflect information hierarchy.
- Prefer stable object names over decorative or campaign-like wording.
- Avoid repeating navigation labels without adding context.
- Ensure the person can tell where they are and what can happen next.

### Navigation and Breadcrumbs

- Use the same term for the same destination.
- Organize labels around user concepts, not internal departments or system architecture.
- Keep sibling labels parallel in grammar and specificity.
- Use breadcrumbs to communicate hierarchy, not history, unless the product explicitly models history.
- Make the current location distinguishable without requiring visual styling alone.

## Actions and Links

- Begin action labels with a precise verb when natural in the locale.
- Name the real outcome: “Save draft”, “Send invite”, “Publish article”.
- Repeat a destructive consequence in its confirmation action: “Delete workspace”, not “Yes”.
- Keep recurring actions stable across a flow.
- Distinguish actions with different consequences: remove, delete, archive, discard, cancel, close, leave, revoke, and sign out.
- Make link text identify its destination or purpose outside surrounding prose.
- Avoid “Click here”, bare “Learn more”, “OK”, “Submit”, “Proceed”, and “Continue” when a more specific outcome is known.
- Do not label navigation as an action or an action as a destination.

## Forms and Input

- Keep a persistent visible label for each field.
- Use placeholders only for examples or expected formats, never as the sole label.
- State requirements, constraints, privacy implications, units, and consequences before input when possible.
- Ask only for information needed for the task.
- Use help text for guidance that is useful before submission.
- Use validation for a specific correction after or during input without blaming the person.
- Keep label, help, field, error, and action semantically connected.
- Do not use “optional” inconsistently; choose a product-wide convention.
- Preserve tokens and examples that help people enter valid data.

## Errors and Recovery

An actionable error normally answers:

1. What happened?
2. What is affected?
3. What can the person do next?

Rules:

- Use human language rather than internal codes.
- Place field errors near the relevant field and make the correction specific.
- Distinguish user-correctable validation from system failure.
- Match the recovery to the cause: edit, retry, reconnect, wait, change permissions, use another method, or contact support.
- Preserve entered data whenever the product does.
- Avoid blame, jokes, “Oops”, and generic “Something went wrong”.
- Do not promise a resolution time the system cannot verify.
- Do not tell the person to retry if retrying cannot change the result.

## Empty States

Distinguish:

- first use;
- valid zero data;
- no search results;
- no filtered results;
- unavailable content;
- permission-limited content;
- loading failure.

For each state:

- explain what belongs in the space when useful;
- orient the person without overexplaining;
- provide the most useful available next action;
- name the query or active filter when relevant;
- offer a clear exit such as changing the query or clearing filters.

Do not place essential persistent guidance only in an empty state that disappears when content exists.

## Onboarding and Help

### Onboarding

- Help the person complete a first useful task rather than touring every feature.
- Present one meaningful concept or action per step.
- Show progress when multiple steps are required.
- Allow skip, exit, resume, or return only when the product supports them.
- Assume limited product knowledge without sounding patronizing.
- Do not make optional setup sound mandatory.

### Tooltips and Contextual Help

- Add information beyond the visible label.
- Keep the message short and tied to the current moment.
- Do not hide essential requirements, consequences, or recovery only in a tooltip.
- Use a longer help surface for procedures or complex explanations.
- Ensure the trigger and content have keyboard and touch equivalents when implemented.

## Status and Feedback

- Name the object and actual result when ambiguity is possible.
- Distinguish saved, sent, uploaded, submitted, queued, processing, processed, and published.
- Do not imply success before the system confirms it.
- Use progress language only when progress is measurable or meaningfully staged.
- Avoid noisy confirmations for routine reversible actions.
- Keep consequential results visible long enough to understand.
- State whether an asynchronous process can continue in the background when confirmed.

## Settings

- Label toggles for the state that applies when enabled: “Send read receipts”.
- Add consequence text when the label alone is insufficient.
- Avoid double negatives and implementation terms.
- Group settings by user purpose rather than internal subsystem.
- Distinguish immediate effects from changes that require save, restart, or reauthentication.
- State scope when a setting affects a workspace, organization, device, or account.

## Confirmations and Destructive Actions

- Name the object and action.
- Explain the material consequence.
- State reversibility, retention, or recovery only when confirmed.
- Use a confirmation action that repeats the exact operation.
- Make cancellation or safe exit clear.
- Avoid “Yes / No” and double negatives.
- Do not add confirmation to routine reversible actions without a demonstrated need.
- Use stronger friction for proportionally higher risk, not dramatic language.

## Consent and Sensitive Content

- Make the choice, purpose, consequence, scope, and reversibility understandable.
- Keep acceptance and refusal labels honest and specific.
- Do not hide refusal, withdrawal, or material conditions in secondary prose.
- Do not change legal effect while simplifying language.
- Separate required processing from optional preference when the product does.
- Avoid coercion, false urgency, disguised advertising, or shame.
- Flag substantive changes for legal, privacy, policy, security, or domain review.
