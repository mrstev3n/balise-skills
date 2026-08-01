# Accessibility and runtime verification

Use this reference when implementing or testing state behavior.

## Status communication

- Do not rely on color, motion, or position alone.
- Provide text or programmatic status for loading, success, errors, queued work, and offline changes.
- Use live announcements deliberately; repeated or verbose updates can overwhelm users.
- Announce meaningful completion and failure, not every decorative transition.

## Focus

- Keep keyboard focus visible.
- Do not move focus merely because content updated.
- Move focus when a new context requires immediate action, such as a blocking dialog or form error summary.
- Restore focus to the triggering control when dismissing overlays when appropriate.
- Ensure retry and recovery actions are reachable in a logical order.

## Loading and disabled controls

- Expose busy state programmatically where supported.
- Prevent duplicate activation while preserving an understandable label.
- Avoid removing controls during pending work when that causes layout or focus loss.
- If a control is disabled, explain the unmet requirement in nearby text or through an accessible description.

## Errors and validation

- Associate field errors with their fields.
- Preserve entered values and valid selections.
- Use concise, corrective language without blame.
- Provide an error summary for long or multi-section forms when useful.
- Do not use placeholders as the only error or recovery instruction.

## Dynamic content

- Keep DOM and reading order stable when possible.
- Avoid skeletons that are announced as meaningful content.
- Respect reduced motion and high-contrast modes.
- Verify zoom, text enlargement, reflow, and narrow widths.
- Preserve scroll and focus when background updates replace data.

## Runtime evidence ladder

1. **Static inspection:** structure, copy, variants, and annotated intent.
2. **Component render:** visual state under controlled props or fixtures.
3. **Interaction test:** state transitions and focus behavior.
4. **Integrated runtime:** network, persistence, routing, and error handling.
5. **Assistive-technology check:** announcements, semantics, and navigation.

Report the highest level actually exercised. A Figma prototype is not integrated runtime evidence.

## Test conditions

When available, verify:

- delayed response;
- empty response;
- partial response;
- validation failure;
- network rejection and timeout;
- offline and reconnect;
- repeated activation;
- back and refresh;
- stale data and conflict;
- keyboard-only navigation;
- screen-reader status output;
- reduced motion, zoom, and high contrast.
