from sigilith_m.profile import build_profile_from_text
from sigilith_m.compare import compare_profiles


def test_compare_profiles_via_built_profiles():
    profile_a = build_profile_from_text("hello world hello")
    profile_b = build_profile_from_text("a b c d")

    result = compare_profiles(profile_a, profile_b)

    assert "euclidean_distance" in result
    assert "cosine_similarity" in result
    assert "metric_deltas" in result
    assert "score_delta" in result["metric_deltas"]
    assert "stability_index_delta" in result["metric_deltas"]
