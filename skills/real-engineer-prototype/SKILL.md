---
name: real-engineer-prototype
description: Throwaway prototyping for Codex to answer one design question. Use when the user wants to prototype, sanity-check a state model, try UI variants, mock up a workflow, or says they want to play with an idea before committing.
---

# Real Engineer Prototype

A prototype answers one question with disposable code. Keep it close enough to the real system to teach something, but clearly marked so nobody mistakes it for production.

## Pick The Shape

- Logic/state question: build a tiny runnable terminal, script, or local harness that lets the state model move through hard cases.
- UI question: create 2-4 structurally different variants, ideally inside the existing route or screen with real data and layout context.

If ambiguous, choose the shape that matches the surrounding code and state the assumption.

## Rules

- Mark prototype files, routes, and comments with `PROTOTYPE`.
- Use one command or URL to run it.
- Keep state in memory unless persistence is the thing being tested.
- Skip production polish, broad tests, and abstractions.
- Do not wire prototypes to real destructive mutations.
- Capture the answer before cleanup: winning variant, rejected approach, state-model decision, or open question.

## UI Variant Pattern

When prototyping UI:

1. Prefer an existing route or page. Use a `?variant=` search param where the framework supports it.
2. Make variants structurally different, not just different colors or copy.
3. Add a small development-only switcher if the project has a clean place for one.
4. Verify visually with the available browser tooling when the app can run locally.
5. After the user chooses, fold the winning idea into production code and delete losing variants.

## Logic Prototype Pattern

When prototyping logic:

1. Create representative fixtures or scenarios.
2. Provide a short loop or menu for exercising transitions.
3. Print the important state before and after each action.
4. Keep the prototype independent of external services unless the question depends on them.
