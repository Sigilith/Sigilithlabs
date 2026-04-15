import random

from sigilith_m.drift import recurrence_drift, normalized_recurrence_drift
from sigilith_m.metrics import (
    score_tokens,
    stability,
    repetition_ratio,
    transition_diversity,
)


def profile_tokens(tokens):
    return {
        "tokens": tokens,
        "score": score_tokens(tokens),
        "stability": stability(tokens),
        "repetition_ratio": repetition_ratio(tokens),
        "transition_diversity": transition_diversity(tokens),
        "drift": recurrence_drift(tokens),
        "normalized_drift": normalized_recurrence_drift(tokens),
    }


def shuffled_tokens(tokens, seed=42):
    rng = random.Random(seed)
    result = list(tokens)
    rng.shuffle(result)
    return result


def sorted_tokens(tokens):
    return sorted(tokens)


def build_baseline(tokens, mode="shuffle", seed=42):
    if mode == "shuffle":
        return shuffled_tokens(tokens, seed=seed)
    if mode == "sorted":
        return sorted_tokens(tokens)
    raise ValueError(f"Unknown baseline mode: {mode}")


def compare_to_baseline(tokens, seed=42, mode="shuffle"):
    base = profile_tokens(tokens)
    baseline_tokens = build_baseline(tokens, mode=mode, seed=seed)
    baseline = profile_tokens(baseline_tokens)

    deltas = {
        "score_delta": base["score"] - baseline["score"],
        "stability_delta": base["stability"] - baseline["stability"],
        "repetition_ratio_delta": base["repetition_ratio"] - baseline["repetition_ratio"],
        "transition_diversity_delta": base["transition_diversity"] - baseline["transition_diversity"],
        "drift_delta": base["drift"] - baseline["drift"],
        "normalized_drift_delta": base["normalized_drift"] - baseline["normalized_drift"],
    }

    return {
        "observed": base,
        "baseline": baseline,
        "baseline_mode": mode,
        "deltas": deltas,
    }
