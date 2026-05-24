#!/usr/bin/env bash
set -euo pipefail

REPO="${CODEX_REAL_ENGINEER_REPO:-ArcQian-bit/test}"
REF="${CODEX_REAL_ENGINEER_REF:-main}"
DEST="${CODEX_HOME:-$HOME/.codex}/skills"

tmp="$(mktemp -d)"
cleanup() {
  rm -rf "$tmp"
}
trap cleanup EXIT

mkdir -p "$DEST"

curl -fsSL "https://codeload.github.com/${REPO}/tar.gz/${REF}" -o "$tmp/repo.tar.gz"
tar -xzf "$tmp/repo.tar.gz" -C "$tmp"

src="$(find "$tmp" -maxdepth 1 -type d -name '*-*' | head -n 1)/skills"
if [[ ! -d "$src" ]]; then
  echo "Could not find skills directory in ${REPO}@${REF}" >&2
  exit 1
fi

for skill in "$src"/*; do
  [[ -d "$skill" ]] || continue
  [[ -f "$skill/SKILL.md" ]] || continue
  cp -R "$skill" "$DEST/"
  echo "Installed $(basename "$skill")"
done

echo
echo "Installed Codex Real Engineer Skills to $DEST"
echo "Restart Codex to pick up the new skills."
