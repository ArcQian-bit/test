---
name: real-engineer-tdd
description: Test-driven development for Codex using red/green/refactor and vertical slices. Use when the user asks for TDD, red-green-refactor, test-first development, integration tests, or wants a feature or bug fix built with strong regression coverage.
---

# Real Engineer TDD

Use test-first development to create a tight feedback loop. Favor behavior through public interfaces over implementation detail tests.

## Workflow

1. Understand the public behavior.
   Inspect existing tests and nearby interfaces. Identify the smallest user-visible or caller-visible behavior that proves the path works.

2. Plan vertical slices.
   Avoid writing all tests first. Each cycle should be one behavior, one failing test, one minimal implementation, then repeat.

3. Red.
   Write one focused test that fails for the right reason. The test should read like a capability, not a transcript of internals.

4. Green.
   Implement only enough code to pass the current test. Do not add speculative options, generalized abstractions, or future behavior.

5. Repeat.
   Add the next behavior only after the previous test passes.

6. Refactor.
   Once green, improve names, remove duplication, deepen modules, and simplify interfaces. Run tests after each meaningful refactor step.

## Good Tests

- Exercise public interfaces or realistic integration paths.
- Assert observable behavior.
- Survive internal refactors.
- Use real collaborators unless mocking an external system, expensive boundary, nondeterministic service, or hard-to-trigger failure.

## Bad Tests

- Verify private methods, call order, or implementation shape.
- Mock internal collaborators only because the design is hard to test.
- Assert database internals instead of behavior through the module's interface.
- Encode a guessed API before implementation teaches you what the API should be.

## Cycle Checklist

```text
[ ] Test fails for the intended reason
[ ] Test describes behavior, not implementation
[ ] Code is minimal for this behavior
[ ] Relevant tests pass
[ ] Refactor only happened after green
```
