from datetime import datetime, timezone

from sigilith_m.baselines import compare_to_baseline
from sigilith_m.classify import summary_label
from sigilith_m.utils import normalize_text, tokenize


def build_profile_from_text(
    text,
    seed=42,
    baseline_mode="shuffle",
    window_size=3,
    block_size=3,
):
    normalized = normalize_text(text)
    tokens = tokenize(text)

    result = compare_to_baseline(
        tokens,
        seed=seed,
        mode=baseline_mode,
        window_size=window_size,
        block_size=block_size,
    )
    observed = result["observed"]

    metrics = {
        "score": observed["score"],
        "stability": observed["stability"],
        "repetition_ratio": observed["repetition_ratio"],
        "transition_diversity": observed["transition_diversity"],
        "drift": observed["drift"],
        "normalized_drift": observed["normalized_drift"],
        "windowed_drift": observed["windowed_drift"],
        "stability_index": observed["stability_index"],
    }

    classification = {
        "summary_label": summary_label(
            metrics["stability"],
            metrics["repetition_ratio"],
            metrics["transition_diversity"],
        )
    }

    metadata = {
        "seed": seed,
        "baseline_mode": baseline_mode,
        "window_size": window_size,
        "block_size": block_size,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    return {
        "input_text": text,
        "normalized": normalized,
        "tokens": tokens,
        "metrics": metrics,
        "baseline": result["baseline"],
        "deltas": result["deltas"],
        "classification": classification,
        "metadata": metadata,
    }
