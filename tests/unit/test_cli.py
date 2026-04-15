from sigilith_m.cli import build_profile_from_text


def test_build_profile_from_text():
    result = build_profile_from_text("HELLO world hello")

    assert result["normalized"] == "hello world hello"
    assert result["tokens"] == ["hello", "world", "hello"]
    assert result["score"] == 5
    assert result["stability"] == 2 / 3
    assert result["repetition_ratio"] == 1 / 3
    assert result["transition_diversity"] == 1.0
    assert result["summary_label"] == "high_transition_variability"
