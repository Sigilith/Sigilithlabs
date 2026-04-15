from sigilith_m.drift import (
    recurrence_drift,
    normalized_recurrence_drift,
    windowed_recurrence_drift,
)


def test_recurrence_drift_clustered():
    tokens = ["a", "a", "b", "c"]
    assert recurrence_drift(tokens) == 1.0
    assert normalized_recurrence_drift(tokens) == 1 / 3


def test_recurrence_drift_spread():
    tokens = ["a", "b", "c", "a"]
    assert recurrence_drift(tokens) == 3.0
    assert normalized_recurrence_drift(tokens) == 1.0


def test_recurrence_drift_no_repeats():
    tokens = ["a", "b", "c"]
    assert recurrence_drift(tokens) == 0.0
    assert normalized_recurrence_drift(tokens) == 0.0


def test_windowed_recurrence_drift():
    tokens = ["a", "b", "a", "c"]
    assert windowed_recurrence_drift(tokens, window_size=3) >= 0.0
