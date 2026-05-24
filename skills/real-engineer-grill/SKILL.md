---
name: real-engineer-grill
description: Requirement and design clarification for Codex before implementation. Use when the user asks to stress-test a plan, clarify a feature, write a spec, resolve ambiguous product behavior, or says to grill them on an idea.
---

# Real Engineer Grill

Clarify the work until implementation choices are grounded. Be rigorous without turning every task into a meeting.

## When To Use

Use this for ambiguous product requests, risky architecture decisions, fuzzy terms, or plans with hidden branches. For small obvious edits, ask only the blocking question or proceed with a stated assumption.

## Workflow

1. Read first.
   If the answer is in the codebase, docs, tests, issues, or existing UI, inspect those instead of asking the user.

2. Name the uncertainty.
   State the decision that matters and why it affects implementation.

3. Ask one useful question at a time.
   Each question should include a recommended answer so the user can correct or accept quickly.

4. Walk the decision tree.
   Resolve dependencies in order: user outcome, domain terms, constraints, data ownership, edge cases, failure modes, rollout, and verification.

5. Capture decisions.
   For repo work, record durable domain language or architecture choices in the repo's existing docs if the user wants that. Prefer existing conventions such as `AGENTS.md`, `CONTEXT.md`, `docs/adr/`, `docs/`, or issue specs.

6. Finish with an implementation-ready brief.
   Summarize the chosen behavior, out-of-scope items, test expectations, and any assumptions that remain.

## Question Quality

Good questions are concrete:

- "Should archived projects be hidden from search results, or visible with an archived badge? Recommended: visible with a badge so old links remain explainable."
- "Is `workspace` the billing boundary or only a collaboration boundary? Recommended: treat billing as account-level unless the code already says otherwise."

Avoid vague questions:

- "Any other requirements?"
- "Can you clarify?"
- "What should this do?"
