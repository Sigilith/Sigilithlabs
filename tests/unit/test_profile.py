from sigilith_m.profile import build_profile_from_text


def test_build_profile_from_text():
    result = build_profile_from_text("HELLO world hello", seed=42, baseline_mode="shuffle")

    assert result["normalized"] == "hello world hello"
    assert result["tokens"] == ["hello", "world", "hello"]

    assert result["metrics"]["score"] == 5
    assert result["metrics"]["stability"] == 2 / 3
    assert result["metrics"]["repetition_ratio"] == 1 / 3
    assert result["metrics"]["transition_diversity"] == 1.0
    assert result["metrics"]["drift"] == 2.0
    assert result["metrics"]["normalized_drift"] == 1.0
    assert "windowed_drift" in result["metrics"]

    assert result["classification"]["summary_label"] == "high_transition_variability"
    assert result["metadata"]["seed"] == 42
    assert result["metadata"]["baseline_mode"] == "shuffle"

    assert "baseline" in result
    assert "deltas" in result
