# Python App Demo: Backlog Triage + Agent Workflow

This demo folder is a small Python app plus a demo backlog that helps a squad practice risk-based triage and agent-assisted delivery.

## Demo objectives

- Route work by **risk**, not lines changed.
- Keep a **human owner** for assignment decisions each sprint.
- Run **the same PR pipeline** for agent and human authored changes.
- Track **outcomes** (rework rate by tier), not just throughput.

## Demo triage model

Use the backlog in `issues/` and sort low-priority work into these tiers:

1. **Agent-ready today**  
   Clear repro, low blast radius, existing test coverage.
2. **Agent-ready with more spec work**  
   Candidate task, but acceptance criteria need to be tightened first.
3. **Human only**  
   Judgment-heavy, high blast radius, or under-specified.

## Run the sample app

```bash
python -m demo.python_app_demo.app.main
```

## Run the tests

```bash
python -m unittest discover -s demo/python_app_demo/tests -p "test_*.py"
```

## Demo script: Watch a Squad Clear a Backlog Item

1. **Assign**: a scoped issue with clear acceptance criteria is assigned to the coding agent.
2. **Code**: the agent works in isolation, updates code, runs tests, and opens a draft PR.
3. **Review (agent)**: a Rubber Duck pass checks consistency with repository conventions and issue intent.
4. **Review (human)**: a person checks the diff, flagged items, and required CI checks.
5. **Merge**: human approves and owns the merge decision.

Say out loud at merge time: **"I checked the diff. I own this merge."**
