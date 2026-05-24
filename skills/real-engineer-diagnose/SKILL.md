---
name: real-engineer-diagnose
description: Disciplined debugging and performance diagnosis for Codex. Use when the user reports a bug, failing test, broken behavior, intermittent issue, crash, regression, slowness, or explicitly asks to debug or diagnose something.
---

# Real Engineer Diagnose

Debug by building a trustworthy feedback loop first. Do not drift into speculative fixes when the failure is not reproduced.

## Workflow

1. Build a fast pass/fail loop.
   Prefer, in order: failing test, focused CLI command, HTTP script, browser automation, replayed fixture, small harness, property/fuzz loop, differential check, or bisection script. Make the loop deterministic and narrow.

2. Reproduce the user's symptom.
   Confirm the loop shows the same failure the user described. Capture the exact error, wrong output, timing, console message, or visual symptom.

3. Rank hypotheses.
   Write 3-5 falsifiable hypotheses. Each hypothesis should say what observation would prove or disprove it. Share the ranking briefly when the diagnosis is nontrivial, then continue unless the user redirects.

4. Probe one variable at a time.
   Use debuggers, REPLs, targeted logs, or focused instrumentation. If adding temporary logs, tag them with a unique prefix such as `[DEBUG-a4f2]` so cleanup is easy.

5. Fix with regression coverage.
   Turn the minimized repro into a test when a correct seam exists. If the only possible test is too shallow to catch the real bug, say so and explain the architectural gap.

6. Clean up.
   Re-run the original loop, run relevant tests, remove temporary instrumentation, delete throwaway harnesses unless they are intentionally preserved, and summarize the actual cause.

## Guardrails

- Do not proceed without a feedback loop unless you explicitly explain why no loop can be built and what artifact is needed from the user.
- Do not test unrelated hypotheses in bulk.
- For performance regressions, measure baseline first, then change one thing.
- Treat intermittent bugs as reproduction-rate problems: loop, parallelize, seed, stress, and narrow until the failure rate is useful.
