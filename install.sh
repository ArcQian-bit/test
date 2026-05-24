#!/usr/bin/env bash
set -euo pipefail

REPO="${CODEX_COOL_CODEX_APPS_REPO:-${CODEX_REAL_ENGINEER_REPO:-ArcQian-bit/codex-real-engineer-skills}}"
REF="${CODEX_COOL_CODEX_APPS_REF:-${CODEX_REAL_ENGINEER_REF:-main}}"
DEST="${CODEX_HOME:-$HOME/.codex}/skills"
REQUESTED="${CODEX_COOL_CODEX_APPS_SKILLS:-all}"
SOURCE_DIR="${CODEX_COOL_CODEX_APPS_SOURCE_DIR:-}"

tmp="$(mktemp -d)"
cleanup() {
  rm -rf "$tmp"
}
trap cleanup EXIT

mkdir -p "$DEST"

if [[ -n "$SOURCE_DIR" ]]; then
  root="$SOURCE_DIR"
else
  curl -fsSL "https://codeload.github.com/${REPO}/tar.gz/${REF}" -o "$tmp/repo.tar.gz"
  tar -xzf "$tmp/repo.tar.gz" -C "$tmp"
  root="$(find "$tmp" -maxdepth 1 -type d -name '*-*' | head -n 1)"
fi
skills_root="$root/skills"
if [[ ! -d "$skills_root" ]]; then
  echo "Could not find skills directory in ${REPO}@${REF}" >&2
  exit 1
fi

if [[ "$REQUESTED" == "all" ]]; then
  skills=()
  while IFS= read -r skill_dir; do
    skills+=("$skill_dir")
  done < <(find "$skills_root" -mindepth 1 -maxdepth 1 -type d -exec test -f '{}/SKILL.md' ';' -print | sort)
else
  IFS=',' read -r -a names <<< "$REQUESTED"
  skills=()
  for name in "${names[@]}"; do
    name="${name#"${name%%[![:space:]]*}"}"
    name="${name%"${name##*[![:space:]]}"}"
    src="$skills_root/$name"
    if [[ ! -f "$src/SKILL.md" ]]; then
      echo "Could not find skill '$name' in ${REPO}@${REF}" >&2
      exit 1
    fi
    skills+=("$src")
  done
fi

installed=()
for src in "${skills[@]}"; do
  name="$(basename "$src")"
  rm -rf "$DEST/$name"
  cp -R "$src" "$DEST/"
  installed+=("$name")
done

printf 'Installed %s Codex apps to %s:\n' "${#installed[@]}" "$DEST"
printf ' - %s\n' "${installed[@]}"
echo
echo "Restart Codex to pick up the new skills."
