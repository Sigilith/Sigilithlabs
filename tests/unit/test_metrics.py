from sigilith_m.metrics import (
    score_tokens,
    stability,
    repetition_ratio,
    transition_diversity,
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
