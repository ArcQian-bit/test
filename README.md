# Coolest Codex Apps

[![GitHub stars](https://img.shields.io/github/stars/ArcQian-bit/codex-real-engineer-skills?style=social)](https://github.com/ArcQian-bit/codex-real-engineer-skills/stargazers)
[![MIT license](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Website](https://img.shields.io/badge/site-GitHub%20Pages-blue.svg)](https://arcqian-bit.github.io/codex-real-engineer-skills/)

The coolest Codex app collection: 10 small, readable skills for serious
software work. The pack keeps the "real engineering" discipline from the first
`real-engineer` skill, then adds focused apps for the workflows Codex users
reach for every day.

It is inspired by the public Claude Code and agent-skill community, but adapted
for Codex's `SKILL.md` model rather than copied from Claude-specific agents,
slash commands, or hooks.

## Links

- Website: https://arcqian-bit.github.io/codex-real-engineer-skills/
- Install guide: https://arcqian-bit.github.io/codex-real-engineer-skills/install-codex-real-engineer-skill.html
- Examples: https://arcqian-bit.github.io/codex-real-engineer-skills/examples.html
- Comparison: https://arcqian-bit.github.io/codex-real-engineer-skills/codex-skills-comparison.html
- Promotion kit: [PROMOTION.md](PROMOTION.md)

## Quick Install

```bash
curl -fsSL https://raw.githubusercontent.com/ArcQian-bit/codex-real-engineer-skills/main/install.sh | bash
```

Restart Codex after installing so the new skills are discovered.

Manual install:

```bash
git clone https://github.com/ArcQian-bit/codex-real-engineer-skills.git
cp -R codex-real-engineer-skills/skills/* ~/.codex/skills/
```

Install only selected apps:

```bash
CODEX_COOL_CODEX_APPS_SKILLS=real-engineer,pr-reviewer,security-scout \
  bash install.sh
```

Install from a local checkout for development:

```bash
CODEX_COOL_CODEX_APPS_SOURCE_DIR="$PWD" CODEX_HOME="$(mktemp -d)" bash install.sh
```

## The 10 Apps

| App | Use it when |
| --- | --- |
| `real-engineer` | You need the general disciplined engineering router: diagnose, TDD, grill, prototype, architecture. |
| `repo-cartographer` | You need to understand a repo, find ownership, or choose the safest change path before coding. |
| `issue-sherpa` | You need to turn a fuzzy issue or bug report into repro steps, acceptance criteria, and a scoped slice. |
| `pr-reviewer` | You need a maintainer-style review of a PR, diff, commit, or local changes. |
| `security-scout` | You need a practical security scan for auth, data handling, secrets, injection, deps, or config. |
| `perf-lab` | You need to profile or optimize latency, memory, bundle size, queries, rendering, or throughput. |
| `release-captain` | You need release notes, changelog grouping, semantic versioning, publish checks, or rollback notes. |
| `docs-keeper` | You need docs, examples, install instructions, or config references kept aligned with code. |
| `frontend-polisher` | You need UI polish, responsive checks, accessibility pass, browser screenshots, or CSS/layout fixes. |
| `migration-pilot` | You need to upgrade, rename, move, codemod, or migrate APIs, dependencies, schemas, or config safely. |

## Development Approach

- Each app has a narrow trigger so duplicate skills do not fight each other.
- Each app starts with evidence: code, diff, issue, benchmark, screenshot, or release range.
- Each app asks only when the repo cannot answer the question.
- Each app finishes with verification and remaining risk.
- The broad `real-engineer` app stays as the fallback when no narrower app fits.

## Example Prompts

```text
Use repo-cartographer to map this repo before we touch checkout.
```

```text
Use pr-reviewer to review this branch for regressions.
```

```text
Use security-scout to audit this auth middleware change.
```

```text
Use migration-pilot to upgrade this package without breaking public imports.
```

## Attribution

The original `real-engineer` workflow was adapted from ideas and workflows in
Matt Pocock's MIT-licensed `mattpocock/skills` repository:

https://github.com/mattpocock/skills

The other apps are Codex-native rewrites. They borrow public workflow categories
from the Claude Code and agent-skill ecosystem, but they do not copy
Claude-specific prompts, hooks, slash commands, or subagent tool assumptions.

| App | Provenance |
| --- | --- |
| `repo-cartographer` | Original Codex skill, informed by Claude Code patterns for codebase research, architecture review, and specialist subagents. |
| `issue-sherpa` | Original Codex skill, informed by Claude Code issue-triage and task-to-implementation workflows such as `anthropics/claude-code-action`. |
| `pr-reviewer` | Original Codex skill, informed by Claude Code Review, community `code-reviewer` agents, and maintainer-style review practices. |
| `security-scout` | Original Codex skill, informed by community `security-auditor` agents and security skill collections such as Trail of Bits' skills. |
| `perf-lab` | Original Codex skill, informed by community `performance-engineer` agents and profiling/benchmarking workflows. |
| `release-captain` | Original Codex skill, informed by deployment/release agents and changelog automation skills in the Claude agent ecosystem. |
| `docs-keeper` | Original Codex skill, informed by community `documentation-engineer`, `api-documenter`, README, tutorial, and reference-builder agents. |
| `frontend-polisher` | Original Codex skill, informed by frontend, accessibility, UI/UX testing, and web-design agent skills. |
| `migration-pilot` | Original Codex skill, informed by legacy modernization, refactoring, dependency-management, and migration-strategy agents. |

Useful upstream references:

- Anthropic Claude Code subagents and skills documentation: https://code.claude.com/docs/en/sub-agents
- Anthropic Claude Code Review documentation: https://code.claude.com/docs/en/code-review
- Anthropic blog on subagents, CLAUDE.md, and skills: https://claude.com/blog/subagents-in-claude-code
- `wshobson/agents`: https://github.com/wshobson/agents
- `VoltAgent/awesome-claude-code-subagents`: https://github.com/VoltAgent/awesome-claude-code-subagents
- `rohitg00/awesome-claude-code-toolkit`: https://github.com/rohitg00/awesome-claude-code-toolkit
- `subinium/awesome-claude-code`: https://github.com/subinium/awesome-claude-code
- Trail of Bits security skills: https://github.com/trailofbits/skills
