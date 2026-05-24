# Real Engineer For Codex

[![GitHub stars](https://img.shields.io/github/stars/ArcQian-bit/codex-real-engineer-skills?style=social)](https://github.com/ArcQian-bit/codex-real-engineer-skills/stargazers)
[![MIT license](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Website](https://img.shields.io/badge/site-GitHub%20Pages-blue.svg)](https://arcqian-bit.github.io/codex-real-engineer-skills/)

One Codex skill for real engineering: debugging, TDD, requirements grilling,
rapid prototyping, and architecture review.

This is a Codex-native collection inspired by Matt Pocock's `mattpocock/skills`.
It folds the overlapping workflows into one router skill: `real-engineer`.

The goal is simple: make Codex behave less like an autocomplete box and more
like a disciplined senior engineer.

## Links

- Website: https://arcqian-bit.github.io/codex-real-engineer-skills/
- Install guide: https://arcqian-bit.github.io/codex-real-engineer-skills/install-codex-real-engineer-skill.html
- Examples: https://arcqian-bit.github.io/codex-real-engineer-skills/examples.html
- Comparison: https://arcqian-bit.github.io/codex-real-engineer-skills/codex-skills-comparison.html
- Promotion kit: [PROMOTION.md](PROMOTION.md)

## Why Star This

- You use Codex and want better defaults for real software work.
- You want one small, readable skill instead of a huge process framework.
- You like Matt Pocock's "real engineering" workflow but want it cleaned up for
  Codex instead of Claude Code.
- You want reusable debugging, TDD, prototyping, and architecture-review habits
  that work across repos.

## Quick Install

```bash
curl -fsSL https://raw.githubusercontent.com/ArcQian-bit/codex-real-engineer-skills/main/install.sh | bash
```

Restart Codex after installing so the new skills are discovered.

You can also install manually:

```bash
git clone https://github.com/ArcQian-bit/codex-real-engineer-skills.git
cp -R codex-real-engineer-skills/skills/real-engineer ~/.codex/skills/
```

## One Skill, Five Modes

| Mode | Use it when | What it changes |
| --- | --- | --- |
| Diagnose | Something is broken, slow, flaky, or failing | Codex builds a reproducible feedback loop before guessing |
| TDD | You want test-first implementation | Codex works in red/green/refactor vertical slices |
| Grill | A feature or design is fuzzy | Codex asks concrete questions with recommended answers |
| Prototype | You need to test a UI, workflow, or state model | Codex builds disposable prototypes that answer one question |
| Architecture | A codebase is hard to change or reason about | Codex looks for deeper modules, better seams, and testable interfaces |

The collection is deliberately one skill rather than five separate skills. That
prevents duplicate triggers such as a bug-fix request activating both a
diagnosis skill and a TDD skill.

## Example Prompts

After restarting Codex, try:

```text
Use real-engineer to debug this failing checkout test.
```

```text
Use real-engineer and implement this endpoint test-first.
```

```text
Use real-engineer to stress-test this feature idea before coding.
```

```text
Use real-engineer and find the top refactor opportunities here.
```

## What Was Adapted For Codex

The original workflows are excellent, but some parts assume Claude Code:
slash-command setup, Claude hooks, and Claude-specific subagent wording. This
pack keeps the engineering discipline and removes those tool-specific
assumptions.

The single skill is named `real-engineer` to avoid collisions with other
installed skills such as `tdd`, `diagnose`, or `prototype`.

## Share

If this helps, star the repo and share it with other Codex users:

> I made a Codex-native `real-engineer` skill inspired by Matt Pocock-style
> engineering workflows: diagnose, TDD, grill, prototype, and architecture
> review. One readable `SKILL.md`, no Claude-specific setup.
>
> https://github.com/ArcQian-bit/codex-real-engineer-skills

More launch copy is in [PROMOTION.md](PROMOTION.md).

## Attribution

Adapted from ideas and workflows in Matt Pocock's MIT-licensed
`mattpocock/skills` repository:

https://github.com/mattpocock/skills
