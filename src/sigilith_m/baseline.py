from collections import Counter
import random

from sigilith_m.drift import recurrence_drift, normalized_recurrence_drift


def profile_tokens(tokens):
    total = len(tokens)
    unique = len(set(tokens))

    score = total + unique if total else 0

    if total:
        counts = Counter(tokens)
        most_common = counts.most_common(1)[0][1]
        stability = most_common / total
        repetition_ratio = (total - unique) / total
    else:
        stability = 0.0
        repetition_ratio = 0.0

    if total >= 2:
        transitions = list(zip(tokens, tokens[1:]))
        transition_diversity = len(set(transitions)) / len(transitions)
    else:
        transition_diversity = 0.0

    drift = recurrence_drift(tokens)
    normalized_drift = normalized_recurrence_drift(tokens)

    return {
        "tokens": tokens,
        "score": score,
        "stability": stability,
        "repetition_ratio": repetition_ratio,
        "transition_diversity": transition_diversity,
        "drift": drift,
        "normalized_drift": normalized_drift,
    }


def shuffled_tokens(tokens, seed=42):
    rng = random.Random(seed)
    result = list(tokens)
    rng.shuffle(result)
    return result


def compare_to_baseline(tokens, seed=42):
    base = profile_tokens(tokens)
    shuffled = shuffled_tokens(tokens, seed=seed)
    baseline = profile_tokens(shuffled)

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
        "deltas": deltas,
    }
