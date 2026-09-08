Yes, Master Chief Sparkle. That is an excellent **two to three minute recorded demo**. The key is to show the workflow transitions, not wait for agents to work.

Use **two issues** if you can prepare them in advance:

1. Issue 001: Fix flaky test
2. Issue 003: Improve logging, after tightening its acceptance criteria

Show one agent-created PR in detail, then show the second issue moving through the same workflow more quickly.

# Recommended demo storyline

**Issue assigned → agent works → PR opened → human reviews → human merges**

Record the agent execution separately, then edit out the waiting time.

# Recording plan

Record these sections as separate clips:

1. Issue assignment
2. Agent implementation
3. Pull request creation
4. Human review
5. Merge
6. Final summary

This lets you cut directly between completed stages.

# Two to three minute demo script

## 0:00 to 0:20: Introduce the workflow

### Do

Open the repository directory:

```text
demo/python_app_demo/
```

Show the `issues/` directory.

### Say

> “This demo shows a human-controlled agent workflow. We start with a GitHub issue, assign it to an agent, let the agent implement the fix and open a pull request, then a human reviews and merges the change.”

> “The agent accelerates implementation, but the human remains responsible for the merge decision.”

---

## 0:20 to 0:40: Show the issue

### Do

Open:

```text
issues/001-fix-flaky-test.md
```

Highlight the acceptance criteria:

- Replace randomness with deterministic behavior.
- Re-enable the test.
- Confirm the targeted test passes consistently.

### Say

> “This issue is a good candidate for agent assignment because it is narrowly scoped, has clear acceptance criteria, and has a low blast radius.”

> “The existing test is skipped because it uses a random value, so the agent has a precise problem to solve.”

---

## 0:40 to 0:55: Assign the issue to the agent

### Do

Show the issue assignment or agent task creation.

Use a concise task prompt:

> “Fix Issue 001 by making `test_checkout_id_is_even` deterministic, re-enabling it, and running the targeted and full test suites. Do not modify unrelated pricing or logging code.”

### Say

> “The human owns the assignment decision. I am giving the agent enough context to make a focused change, including what not to modify.”

---

## 0:55 to 1:05: Cut to the completed agent work

### Do

Use an edit or transition to skip the runtime.

Show the completed agent result or the pull request link.

### Say

> “While the agent worked, it inspected the test, made the smallest appropriate change, ran validation, and opened a pull request.”

> “For this recording, I have removed the waiting time, but the workflow itself is unchanged.”

This sentence is useful because it makes the editing transparent.

---

## 1:05 to 1:35: Show the pull request

### Do

Open the agent-created pull request. Show:

- Pull request title.
- Issue reference.
- Changed file.
- Test results.
- CI status.
- Agent summary.

Show the changed test:

```python
import unittest


class FlakyDemoTests(unittest.TestCase):
    def test_checkout_id_is_even(self) -> None:
        # Use a fixed value so the test result is repeatable.
        checkout_id = 42

        # Confirm the deterministic checkout ID is even.
        self.assertEqual(checkout_id % 2, 0)
```

### Say

> “The agent has raised a pull request instead of changing production directly. That gives us a review boundary.”

> “The implementation is deliberately small. It removes uncontrolled randomness, re-enables the test, and preserves the original assertion.”

> “The comments explain both why the fixed value exists and what behavior the assertion verifies.”

---

## 1:35 to 2:00: Human review

### Do

Review the diff and check the validation results.

### Say

> “Now I am reviewing the change as a human. I am checking that the implementation matches the issue, that the scope is limited, and that the tests provide credible evidence.”

> “I am also checking that the agent did not make unrelated changes to pricing, logging, or other parts of the application.”

Ask these three questions during the review:

1. Does the test now run instead of being skipped?
2. Is the input deterministic?
3. Does the full test suite pass?

---

## 2:00 to 2:20: Approve and merge

### Do

Approve the pull request and merge it using the repository’s normal merge process.

### Say

> “The change satisfies the acceptance criteria, the tests pass, and the diff is appropriately scoped.”

Then say the ownership statement:

> “I checked the diff. I own this merge.”

### Important point

Do not say that the agent merged the code. The agent opened the pull request. The human reviewed and approved the production change.

---

## 2:20 to 2:45: Show the second issue moving through the workflow

### Do

Briefly show another issue, such as the logging issue:

```text
issues/003-improve-logging.md
```

Show its pull request or completed workflow without explaining every detail.

### Say

> “The same workflow can be repeated for other issues. This second example shows that the agent is not working outside a controlled process. Each task still has an issue, a pull request, validation, and human approval.”

> “For higher-risk or under-specified work, the human may stop the process before assignment or request more specification first.”

---

# Suggested visual flow

Use a simple slide or screen overlay showing:

```text
Issue
  ↓
Human triage
  ↓
Agent assignment
  ↓
Agent implementation
  ↓
Pull request
  ↓
Human review
  ↓
Human approval
  ↓
Merge to production
```

When you move between screens, briefly say the stage name:

> “Issue.”

> “Assignment.”

> “Implementation.”

> “Pull request.”

> “Human review.”

> “Merge.”

This makes the workflow easy to follow even after editing.

# Best demo setup

Prepare these before recording:

- A clean repository state.
- Issue 001 already available.
- An agent task prompt ready to paste.
- A completed agent pull request.
- Passing test results.
- A second completed issue or pull request.
- A clean browser tab for the issue.
- A clean browser tab for the pull request.
- A terminal tab showing the test commands.

For the strongest result, record the agent working in a separate capture. Then cut from:

```text
Agent task started
```

directly to:

```text
Pull request opened
```

You can say:

> “I have removed the implementation wait time from this recording. The next screen shows the completed agent result.”

# What not to demonstrate

For a short recording, avoid:

- Running every issue from start to finish.
- Explaining all application files.
- Showing long agent reasoning or progress logs.
- Discussing dependency upgrades in detail.
- Demonstrating a security alert unless you want to emphasize why some issues remain human-only.
- Merging without showing the review step.

# Strong closing statement

> “This workflow gives us speed without removing accountability. The agent handles scoped implementation and raises a pull request. The human reviews the evidence, owns the approval, and controls what reaches production.”

# Shortest possible version

If you need to finish in under two minutes:

1. Show Issue 001.
2. Assign it to the agent.
3. Cut to the completed pull request.
4. Show the diff and passing tests.
5. Review the change.
6. Say:

> “The agent created the pull request, but I reviewed the diff and validation results.”

7. Merge it.
8. Say:

> “I checked the diff. I own this merge.”

That gives you the complete story with a clear separation between **agent execution** and **human production ownership**.
