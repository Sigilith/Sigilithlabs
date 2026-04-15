import math


VECTOR_KEYS = [
    "score",
    "stability",
    "repetition_ratio",
    "transition_diversity",
    "drift",
    "normalized_drift",
    "windowed_drift",
    "stability_index",
]


def profile_vector(profile):
    """
    Extract a numeric comparison vector from a Sigilith-M profile.
    """
    metrics = profile.get("metrics", {})
    return [float(metrics.get(key, 0.0)) for key in VECTOR_KEYS]


def euclidean_distance(profile_a, profile_b):
    v1 = profile_vector(profile_a)
    v2 = profile_vector(profile_b)
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))


def cosine_similarity(profile_a, profile_b):
    v1 = profile_vector(profile_a)
    v2 = profile_vector(profile_b)

    dot = sum(a * b for a, b in zip(v1, v2))
    norm1 = math.sqrt(sum(a * a for a in v1))
    norm2 = math.sqrt(sum(b * b for b in v2))

    if norm1 == 0.0 or norm2 == 0.0:
        return 0.0

    return dot / (norm1 * norm2)


def metric_deltas(profile_a, profile_b):
    metrics_a = profile_a.get("metrics", {})
    metrics_b = profile_b.get("metrics", {})

    deltas = {}
    for key in VECTOR_KEYS:
        deltas[f"{key}_delta"] = float(metrics_a.get(key, 0.0)) - float(metrics_b.get(key, 0.0))
    return deltas


def compare_profiles(profile_a, profile_b):
    return {
        "euclidean_distance": euclidean_distance(profile_a, profile_b),
        "cosine_similarity": cosine_similarity(profile_a, profile_b),
        "metric_deltas": metric_deltas(profile_a, profile_b),
    }
