---
name: real-engineer-architecture
description: Architecture review for Codex focused on making modules deeper, simpler, more testable, and easier for agents to navigate. Use when the user asks to improve architecture, review structure, find refactor opportunities, reduce coupling, or make code more maintainable.
---

# Real Engineer Architecture

Find refactors that improve locality and leverage. Prefer a few high-confidence opportunities over a long list of decorative cleanup.

## Vocabulary

- Module: code with an interface and an implementation.
- Interface: everything a caller must know to use the module, including invariants, errors, ordering, config, and types.
- Implementation: the code hidden behind the interface.
- Deep module: small interface, substantial useful behavior.
- Shallow module: interface nearly as complex as its implementation.
- Seam: a place behavior can vary without editing callers.
- Adapter: a concrete implementation behind a seam.
- Locality: related change, knowledge, and bugs stay in one place.
- Leverage: callers get more behavior while knowing less.

## Review Process

1. Read the map.
   Inspect project docs, tests, module boundaries, and any `AGENTS.md`, `CONTEXT.md`, `docs/adr/`, or equivalent architecture notes.

2. Explore friction.
   Look for concepts that require bouncing across many files, pass-through wrappers, duplicated orchestration, hidden coupling, hard-to-test behavior, and tests that only exist because the real interface is awkward.

3. Apply the deletion test.
   If deleting a module makes complexity vanish, it was probably shallow. If deleting it spreads complexity across callers, it was probably earning its keep.

4. Present candidates.
   For each candidate include files, current friction, proposed direction, expected locality/leverage gain, test impact, and confidence: `Strong`, `Worth exploring`, or `Speculative`.

5. Do not over-prescribe.
   Ask which candidate the user wants to pursue before designing detailed interfaces, unless the user explicitly asked for an implementation plan.

6. If implementing, move in small steps.
   Add characterization tests where possible, create or clarify the seam, migrate one caller or path, run tests, then continue.

## Heuristics

- One adapter is often only a hypothetical seam; two adapters make the seam real.
- Pure helper extraction is not automatically better architecture.
- A good interface reduces what callers need to know.
- If a refactor contradicts an ADR, surface that conflict instead of quietly relitigating it.
