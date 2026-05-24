#!/usr/bin/env bash
set -euo pipefail

REPO="${CODEX_REAL_ENGINEER_REPO:-ArcQian-bit/codex-real-engineer-skills}"
REF="${CODEX_REAL_ENGINEER_REF:-main}"
DEST="${CODEX_HOME:-$HOME/.codex}/skills"
SKILL_NAME="real-engineer"

tmp="$(mktemp -d)"
cleanup() {
  rm -rf "$tmp"
}
trap cleanup EXIT

mkdir -p "$DEST"

curl -fsSL "https://codeload.github.com/${REPO}/tar.gz/${REF}" -o "$tmp/repo.tar.gz"
tar -xzf "$tmp/repo.tar.gz" -C "$tmp"

root="$(find "$tmp" -maxdepth 1 -type d -name '*-*' | head -n 1)"
src="$root/skills/$SKILL_NAME"
if [[ ! -f "$src/SKILL.md" ]]; then
  echo "Could not find $SKILL_NAME in ${REPO}@${REF}" >&2
  exit 1
fi

rm -rf "$DEST/$SKILL_NAME"
cp -R "$src" "$DEST/"
echo "Installed $SKILL_NAME"

echo
echo "Installed Real Engineer for Codex to $DEST/$SKILL_NAME"
echo "Restart Codex to pick up the new skills."
