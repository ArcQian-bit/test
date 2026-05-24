#!/usr/bin/env python3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED_SKILLS = {
    "docs-keeper",
    "frontend-polisher",
    "issue-sherpa",
    "migration-pilot",
    "perf-lab",
    "pr-reviewer",
    "real-engineer",
    "release-captain",
    "repo-cartographer",
    "security-scout",
}


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def skill_text(name: str) -> str:
    return (SKILLS / name / "SKILL.md").read_text()


def test_collection_has_ten_apps() -> None:
    skill_dirs = {p.name for p in SKILLS.iterdir() if p.is_dir()}
    assert_true(skill_dirs == EXPECTED_SKILLS, f"unexpected skill dirs: {sorted(skill_dirs)}")


def test_frontmatter_names_match_folders() -> None:
    for name in EXPECTED_SKILLS:
        text = skill_text(name)
        assert_true(text.startswith("---\n"), f"{name} missing YAML frontmatter")
        assert_true(f"name: {name}" in text, f"{name} frontmatter name mismatch")
        assert_true("description:" in text, f"{name} missing description")


def test_no_template_leftovers() -> None:
    forbidden = ["TODO", "Replace with", "Complete and informative", "Structuring This Skill"]
    for path in SKILLS.glob("*/SKILL.md"):
        text = path.read_text()
        for token in forbidden:
            assert_true(token not in text, f"{path} still contains template token {token!r}")


def test_trigger_boundaries_are_distinct() -> None:
    checks = {
        "repo-cartographer": ["unfamiliar repositories", "safest change path"],
        "issue-sherpa": ["Triage GitHub issues", "acceptance criteria"],
        "pr-reviewer": ["pull requests", "diff review"],
        "security-scout": ["security review", "injection risk"],
        "perf-lab": ["performance", "benchmarking"],
        "release-captain": ["releases", "semantic version"],
        "docs-keeper": ["documentation", "README"],
        "frontend-polisher": ["frontend UI", "responsive layout"],
        "migration-pilot": ["migrations", "codemods"],
    }
    for name, phrases in checks.items():
        text = skill_text(name)
        for phrase in phrases:
            assert_true(phrase in text, f"{name} missing boundary phrase {phrase!r}")


def test_real_engineer_is_fallback_not_duplicate() -> None:
    text = skill_text("real-engineer")
    for mode in ["Diagnose", "TDD", "Grill", "Prototype", "Architecture"]:
        assert_true(f"## {mode} Mode" in text, f"missing {mode} mode")
    for excluded in ["PR review", "issue triage", "release prep", "security review", "repo onboarding"]:
        assert_true(excluded in text, f"real-engineer missing specific exclusion {excluded!r}")


def test_installer_defaults_to_collection() -> None:
    text = (ROOT / "install.sh").read_text()
    assert_true("CODEX_COOL_CODEX_APPS_SKILLS:-all" in text, "installer does not default to all apps")
    assert_true("CODEX_COOL_CODEX_APPS_SOURCE_DIR" in text, "installer lacks local source override")
    assert_true("find \"$skills_root\"" in text, "installer does not discover skill directories")
    assert_true("Restart Codex" in text, "installer missing restart instruction")


def test_public_docs_use_collection_install_url() -> None:
    new_url = "install-coolest-codex-apps.html"
    old_url = "install-codex-real-engineer-skill.html"
    public_docs = [
        ROOT / "README.md",
        ROOT / "docs" / "index.html",
        ROOT / "docs" / "codex-skills-comparison.html",
        ROOT / "docs" / "llms.txt",
        ROOT / "docs" / "sitemap.xml",
    ]
    for path in public_docs:
        text = path.read_text()
        assert_true(new_url in text, f"{path} does not link to the Coolest Codex Apps install page")
        assert_true(old_url not in text, f"{path} still links to the legacy Real Engineer install page")
    redirect = (ROOT / "docs" / old_url).read_text()
    assert_true("noindex" in redirect, "legacy install page should not be indexed")
    assert_true(new_url in redirect, "legacy install page should redirect to the collection install page")


def main() -> None:
    tests = [
        test_collection_has_ten_apps,
        test_frontmatter_names_match_folders,
        test_no_template_leftovers,
        test_trigger_boundaries_are_distinct,
        test_real_engineer_is_fallback_not_duplicate,
        test_installer_defaults_to_collection,
        test_public_docs_use_collection_install_url,
    ]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")


if __name__ == "__main__":
    main()
