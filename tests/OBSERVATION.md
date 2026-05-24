# Skill Observation

## Example Prompt

```text
线上反馈：优惠券在纽约时间 5/23 晚上被提前判定过期。请修一下。
```

## Without `real-engineer`

Likely response shape:

```text
This is probably a timezone comparison bug. I will inspect the expiry check,
convert both values to UTC, adjust the conditional, and rerun tests.
```

Problem: this jumps to a plausible fix before proving the failure. It may fix a
nearby timezone bug while missing the user's actual symptom.

## With `real-engineer`

Expected response shape:

```text
Mode: Diagnose. I will first build a failing repro for the exact coupon expiry
case, confirm it matches the user report, rank the likely causes, then fix the
smallest proven cause and keep the repro as regression coverage.
```

Difference: the skill forces a feedback loop before implementation. The output
is less eager but more reliable: reproduce, hypothesize, probe, fix, regression
test.

## Negative Trigger Example

```text
把这个 README 的语气改得更轻松一点。
```

Expected behavior: do not invoke `real-engineer`. This is routine writing/editing
work, not a debugging, TDD, architecture, prototype, or requirements-clarifying
task.
