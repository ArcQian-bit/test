# Skill Observation

## Example Prompt

```text
请 review 这个分支，重点看会不会引入用户可见回归。
```

## Without `pr-reviewer`

Likely response shape:

```text
I will look through the changes, summarize what changed, and mention anything
that seems risky.
```

Problem: this often becomes a summary instead of a review. It may praise the
change before naming concrete defects, and it may skip file/line evidence.

## With `pr-reviewer`

Expected response shape:

```text
Findings first. I will inspect the diff and nearby contracts, report only
actionable regressions with file/line references, and call out remaining test
gaps if no issue is found.
```

Difference: the app forces maintainer-style review output: findings, severity,
evidence, fix direction, then residual risk.

## Fallback Example

```text
线上反馈：优惠券在纽约时间 5/23 晚上被提前判定过期。请修一下。
```

Expected behavior: use `real-engineer` Diagnose mode unless a narrower app was
explicitly requested. Codex should reproduce the exact symptom before guessing.

## Negative Trigger Example

```text
把这个 README 的语气改得更轻松一点。
```

Expected behavior: do not invoke this collection unless the user asks for
`docs-keeper` or repository documentation alignment. This is routine writing.
