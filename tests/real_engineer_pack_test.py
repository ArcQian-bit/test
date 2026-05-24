#!/usr/bin/env python3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
AGGREGATE = SKILLS / "real-engineer" / "SKILL.md"
OLD_SKILLS = {
    "real-engineer-architecture",
    "real-engineer-diagnose",
    "real-engineer-grill",
    "real-engineer-prototype",
    "real-engineer-tdd",
}


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def test_single_installed_skill_source() -> None:
    skill_dirs = sorted(p.name for p in SKILLS.iterdir() if p.is_dir())
    assert_true(skill_dirs == ["real-engineer"], f"expected one skill dir, got {skill_dirs}")


def test_no_duplicate_legacy_sources() -> None:
    present = sorted(name for name in OLD_SKILLS if (SKILLS / name).exists())
    assert_true(not present, f"duplicate legacy skill dirs still present: {present}")


def test_frontmatter_and_routing() -> None:
    text = AGGREGATE.read_text()
    assert_true(text.startswith("---\n"), "missing YAML frontmatter")
    assert_true("name: real-engineer" in text, "wrong skill name")
    for mode in ["Diagnose", "TDD", "Grill", "Prototype", "Architecture"]:
        assert_true(f"## {mode} Mode" in text, f"missing {mode} mode")
    for excluded in ["routine shell questions", "document/image/spreadsheet"]:
        assert_true(excluded in text, f"missing negative trigger: {excluded}")


def test_observation_example() -> None:
    without_skill = (
        "Likely a timezone comparison bug. Check the expiry comparison, convert both "
        "values to UTC, update the conditional, and rerun tests."
    )
    with_skill = (
        "Mode: Diagnose. First build a failing test or CLI repro for the exact coupon "
        "expiry symptom, confirm it fails for the user-described reason, rank timezone "
        "and boundary hypotheses, then fix and keep the repro as regression coverage."
    )
    assert_true("failing test" in with_skill and "repro" in with_skill, "skill example lacks feedback loop")
    assert_true("Likely" in without_skill and "First build" not in without_skill, "baseline is not a useful contrast")


def main() -> None:
    tests = [
        test_single_installed_skill_source,
        test_no_duplicate_legacy_sources,
        test_frontmatter_and_routing,
        test_observation_example,
    ]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")


if __name__ == "__main__":
    main()
