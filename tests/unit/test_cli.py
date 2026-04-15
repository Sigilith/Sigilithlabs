from sigilith_m.cli import build_profile_from_text


def test_build_profile_from_text():
    result = build_profile_from_text("HELLO world hello", seed=42, baseline_mode="shuffle")

    assert result["normalized"] == "hello world hello"
    assert result["tokens"] == ["hello", "world", "hello"]
    assert result["score"] == 5
    assert result["stability"] == 2 / 3
    assert result["repetition_ratio"] == 1 / 3
    assert result["transition_diversity"] == 1.0
    assert result["drift"] == 2.0
    assert result["normalized_drift"] == 1.0
    assert result["summary_label"] == "high_transition_variability"
    assert result["seed"] == 42
    assert result["baseline_mode"] == "shuffle"

    assert "baseline" in result
    assert "deltas" in result
    assert "score_delta" in result["deltas"]
    assert "drift_delta" in result["deltas"]


def test_build_profile_with_sorted_baseline():
    result = build_profile_from_text("b a c a", baseline_mode="sorted")

    assert result["baseline_mode"] == "sorted"
    assert result["baseline"]["tokens"] == ["a", "a", "b", "c"]
