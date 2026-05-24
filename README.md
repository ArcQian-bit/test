# Codex Real Engineer Skills

Codex-native adaptations inspired by Matt Pocock's `mattpocock/skills`.

These skills keep the useful engineering workflows while removing Claude Code
assumptions such as slash-command setup, Claude hooks, and Claude-specific
subagent wording. They are intentionally small and composable.

## Skills

- `real-engineer-diagnose` - disciplined debugging and performance diagnosis.
- `real-engineer-tdd` - red/green/refactor with vertical slices.
- `real-engineer-grill` - rigorous requirement and design clarification.
- `real-engineer-prototype` - throwaway logic or UI prototypes to answer one question.
- `real-engineer-architecture` - architecture review focused on deeper modules.

## Install

Copy the skill directories into your Codex skills folder:

```bash
cp -R skills/* ~/.codex/skills/
```

Restart Codex so the newly installed skills are discovered.

## Attribution

Adapted from ideas and workflows in Matt Pocock's MIT-licensed
`mattpocock/skills` repository:

https://github.com/mattpocock/skills
