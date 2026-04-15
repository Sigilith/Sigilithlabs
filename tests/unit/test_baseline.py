from sigilith_m.baselines import (
    profile_tokens,
    shuffled_tokens,
    sorted_tokens,
    compare_to_baseline,
)


def test_profile_tokens_basic():
    result = profile_tokens(["a", "b", "a"])

    assert result["score"] == 5
    assert result["stability"] == 2 / 3
    assert result["repetition_ratio"] == 1 / 3
    assert result["transition_diversity"] == 1.0
    assert result["drift"] == 2.0
    assert result["normalized_drift"] == 1.0


def test_shuffled_tokens_preserves_members():
    tokens = ["a", "b", "a", "c"]
    result = shuffled_tokens(tokens, seed=42)

    assert sorted(result) == sorted(tokens)
    assert len(result) == len(tokens)


def test_sorted_tokens_groups_symbols():
    tokens = ["b", "a", "c", "a"]
    result = sorted_tokens(tokens)

    assert result == ["a", "a", "b", "c"]


def test_compare_to_baseline_structure():
    result = compare_to_baseline(["a", "b", "a", "c"], seed=42, mode="shuffle")

    assert "observed" in result
    assert "baseline" in result
    assert "deltas" in result
    assert result["baseline_mode"] == "shuffle"

    assert "score_delta" in result["deltas"]
    assert "stability_delta" in result["deltas"]
    assert "repetition_ratio_delta" in result["deltas"]
    assert "transition_diversity_delta" in result["deltas"]
    assert "drift_delta" in result["deltas"]
    assert "normalized_drift_delta" in result["deltas"]


def test_compare_to_sorted_baseline():
    result = compare_to_baseline(["b", "a", "c", "a"], mode="sorted")

    assert result["baseline_mode"] == "sorted"
    assert result["baseline"]["tokens"] == ["a", "a", "b", "c"]
