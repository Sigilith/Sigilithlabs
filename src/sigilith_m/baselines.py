import random

from sigilith_m.drift import (
    recurrence_drift,
    normalized_recurrence_drift,
    windowed_recurrence_drift,
)
from sigilith_m.metrics import (
    score_tokens,
    stability,
    repetition_ratio,
    transition_diversity,
    stability_index,
)


def profile_tokens(tokens):
    score = score_tokens(tokens)
    stability_value = stability(tokens)
    repetition_ratio_value = repetition_ratio(tokens)
    transition_diversity_value = transition_diversity(tokens)
    drift = recurrence_drift(tokens)
    normalized_drift = normalized_recurrence_drift(tokens)
    windowed_drift = windowed_recurrence_drift(tokens, window_size=3)

    return {
        "tokens": tokens,
        "score": score,
        "stability": stability_value,
        "repetition_ratio": repetition_ratio_value,
        "transition_diversity": transition_diversity_value,
        "drift": drift,
        "normalized_drift": normalized_drift,
        "windowed_drift": windowed_drift,
        "stability_index": stability_index(
            stability_value,
            repetition_ratio_value,
            transition_diversity_value,
            normalized_drift,
        ),
    }


def shuffled_tokens(tokens, seed=42):
    rng = random.Random(seed)
    result = list(tokens)
    rng.shuffle(result)
    return result


def sorted_tokens(tokens):
    return sorted(tokens)


def local_shuffled_tokens(tokens, window_size=3, seed=42):
    rng = random.Random(seed)
    result = list(tokens)

    if window_size < 2:
        return result

    for i in range(0, len(result), window_size):
        window = result[i:i + window_size]
        rng.shuffle(window)
        result[i:i + window_size] = window

    return result


def block_preserving_shuffled_tokens(tokens, block_size=3, seed=42):
    """
    Split tokens into contiguous blocks, preserve each block internally,
    but shuffle the order of the blocks.
    """
    if block_size < 1:
        return list(tokens)

    blocks = [tokens[i:i + block_size] for i in range(0, len(tokens), block_size)]
    rng = random.Random(seed)
    rng.shuffle(blocks)

    result = []
    for block in blocks:
        result.extend(block)
    return result


def build_baseline(tokens, mode="shuffle", seed=42, window_size=3, block_size=3):
    if mode == "shuffle":
        return shuffled_tokens(tokens, seed=seed)
    if mode == "sorted":
        return sorted_tokens(tokens)
    if mode == "local_shuffle":
        return local_shuffled_tokens(tokens, window_size=window_size, seed=seed)
    if mode == "block_shuffle":
        return block_preserving_shuffled_tokens(tokens, block_size=block_size, seed=seed)
    raise ValueError(f"Unknown baseline mode: {mode}")


def compare_to_baseline(tokens, seed=42, mode="shuffle", window_size=3, block_size=3):
    base = profile_tokens(tokens)
    baseline_tokens = build_baseline(
        tokens,
        mode=mode,
        seed=seed,
        window_size=window_size,
        block_size=block_size,
    )
    baseline = profile_tokens(baseline_tokens)

    deltas = {
        "score_delta": base["score"] - baseline["score"],
        "stability_delta": base["stability"] - baseline["stability"],
        "repetition_ratio_delta": base["repetition_ratio"] - baseline["repetition_ratio"],
        "transition_diversity_delta": base["transition_diversity"] - baseline["transition_diversity"],
        "drift_delta": base["drift"] - baseline["drift"],
        "normalized_drift_delta": base["normalized_drift"] - baseline["normalized_drift"],
        "windowed_drift_delta": base["windowed_drift"] - baseline["windowed_drift"],
        "stability_index_delta": base["stability_index"] - baseline["stability_index"],
    }

    return {
        "observed": base,
        "baseline": baseline,
        "baseline_mode": mode,
        "deltas": deltas,
    }
