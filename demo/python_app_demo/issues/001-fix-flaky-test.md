# Issue 001: Fix flaky test

## Problem
`test_checkout_id_is_even` is intentionally flaky and currently skipped.

## Acceptance criteria
- Replace randomness with deterministic behavior.
- Re-enable the test.
- Confirm targeted test run passes consistently.

## Suggested triage tier
**Agent-ready today** (clear repro, low blast radius, tests already exist).
