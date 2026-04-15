from sigilith_m.profile import build_profile_from_text
from sigilith_m.compare import (
    profile_vector,
    euclidean_distance,
    cosine_similarity,
    compare_profiles,
)


def test_profile_vector_length():
    profile = build_profile_from_text("hello world hello")
    vector = profile_vector(profile)

    assert len(vector) == 8


def test_euclidean_distance_zero_for_same_profile():
    profile = build_profile_from_text("hello world hello")
    assert euclidean_distance(profile, profile) == 0.0


def test_cosine_similarity_one_for_same_profile():
    profile = build_profile_from_text("hello world hello")
    value = cosine_similarity(profile, profile)
    assert abs(value - 1.0) < 1e-9


def test_compare_profiles_structure():
    profile_a = build_profile_from_text("hello world hello")
    profile_b = build_profile_from_text("a b c d")

    result = compare_profiles(profile_a, profile_b)

    assert "euclidean_distance" in result
    assert "cosine_similarity" in result
    assert "metric_deltas" in result
    assert "score_delta" in result["metric_deltas"]
    assert "stability_index_delta" in result["metric_deltas"]
