from sigilith_m.metrics import (
    score_tokens,
    stability,
    repetition_ratio,
    transition_diversity,
    stability_index,
)


def test_score_tokens():
    assert score_tokens(["a", "b", "a"]) == 5
    assert score_tokens([]) == 0


def test_stability():
    assert stability(["a", "b", "a"]) == 2 / 3
    assert stability([]) == 0.0


def test_repetition_ratio():
    assert repetition_ratio(["a", "b", "a"]) == 1 / 3
    assert repetition_ratio([]) == 0.0


def test_transition_diversity():
    assert transition_diversity(["a", "b", "a"]) == 1.0
    assert transition_diversity(["a", "a", "a"]) == 0.5
    assert transition_diversity(["a"]) == 0.0


def test_stability_index_bounds():
    value = stability_index(0.7, 0.5, 0.2, 0.1)
    assert 0.0 <= value <= 1.0


def test_stability_index_higher_for_more_stable_pattern():
    stable_value = stability_index(0.9, 0.7, 0.2, 0.1)
    unstable_value = stability_index(0.3, 0.1, 0.9, 0.9)
    assert stable_value > unstable_value
