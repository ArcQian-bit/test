# Codex Real Engineer Skills

[![GitHub stars](https://img.shields.io/github/stars/ArcQian-bit/test?style=social)](https://github.com/ArcQian-bit/test/stargazers)
[![MIT license](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Codex skills for real engineering, not vibe coding.

This is a Codex-native adaptation of the best engineering workflows from
Matt Pocock's `mattpocock/skills`: debugging with feedback loops, TDD through
vertical slices, rigorous requirement clarification, disposable prototypes, and
architecture review focused on deeper modules.

The goal is simple: make Codex behave less like an autocomplete box and more
like a disciplined senior engineer.

## Why Star This

- You use Codex and want better defaults for real software work.
- You want small, readable skills instead of a huge process framework.
- You like Matt Pocock's "real engineering" workflow but want it cleaned up for
  Codex instead of Claude Code.
- You want reusable debugging, TDD, prototyping, and architecture-review habits
  that work across repos.

## Quick Install

```bash
curl -fsSL https://raw.githubusercontent.com/ArcQian-bit/test/main/install.sh | bash
```

Restart Codex after installing so the new skills are discovered.

You can also install manually:

```bash
git clone https://github.com/ArcQian-bit/test.git
cp -R test/skills/* ~/.codex/skills/
```

## Skills

| Skill | Use it when | What it changes |
| --- | --- | --- |
| `real-engineer-diagnose` | Something is broken, slow, flaky, or failing | Codex builds a reproducible feedback loop before guessing |
| `real-engineer-tdd` | You want test-first implementation | Codex works in red/green/refactor vertical slices |
| `real-engineer-grill` | A feature or design is fuzzy | Codex asks concrete questions with recommended answers |
| `real-engineer-prototype` | You need to test a UI, workflow, or state model | Codex builds disposable prototypes that answer one question |
| `real-engineer-architecture` | A codebase is hard to change or reason about | Codex looks for deeper modules, better seams, and testable interfaces |

## Example Prompts

After restarting Codex, try:

```text
Use real-engineer-diagnose on this failing checkout test.
```

```text
Use real-engineer-tdd and implement this endpoint test-first.
```

```text
Use real-engineer-grill and stress-test this feature idea before coding.
```

```text
Use real-engineer-architecture and find the top refactor opportunities here.
```

## What Was Adapted For Codex

The original workflows are excellent, but some parts assume Claude Code:
slash-command setup, Claude hooks, and Claude-specific subagent wording. This
pack keeps the engineering discipline and removes those tool-specific
assumptions.

The skill names are prefixed with `real-engineer-` to avoid collisions with
other installed skills such as `tdd`, `diagnose`, or `prototype`.

## Share

If this helps, star the repo and share it with other Codex users:

> I made a Codex-native adaptation of Matt Pocock-style "real engineering"
> skills: diagnose, TDD, grill, prototype, and architecture review. Small,
> readable `SKILL.md` files, no Claude-specific setup.
>
> https://github.com/ArcQian-bit/test

## Attribution

Adapted from ideas and workflows in Matt Pocock's MIT-licensed
`mattpocock/skills` repository:

https://github.com/mattpocock/skills
