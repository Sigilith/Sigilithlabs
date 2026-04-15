from sigilith_m.profile import build_profile_from_text
from sigilith_m.compare import compare_profiles
from sigilith_m.report import generate_comparison_report


def test_generate_comparison_report():
    profile_a = build_profile_from_text("hello world hello")
    profile_b = build_profile_from_text("a b c d")
    comparison = compare_profiles(profile_a, profile_b)

    payload = {
        "profile_a": profile_a,
        "profile_b": profile_b,
        "comparison": comparison,
        "metadata": {
            "seed": 42,
            "baseline_mode": "shuffle",
            "window_size": 3,
            "block_size": 3,
        },
    }

    report = generate_comparison_report(payload)

    assert "# Sigilith-M Comparative Report" in report
    assert "## Profile A" in report
    assert "## Profile B" in report
    assert "## Comparison" in report
    assert "Euclidean distance" in report
    assert "Cosine similarity" in report
