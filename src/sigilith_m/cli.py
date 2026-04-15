import argparse
from pathlib import Path

from sigilith_m.export import save_json
from sigilith_m.baselines import compare_to_baseline
from sigilith_m.utils import tokenize, normalize_text, read_text_file


def build_profile_from_text(text, seed=42, baseline_mode="shuffle"):
    normalized = normalize_text(text)
    tokens = tokenize(text)
    result = compare_to_baseline(tokens, seed=seed, mode=baseline_mode)

    observed = result["observed"]
    observed["normalized"] = normalized
    observed["summary_label"] = classify_summary(
        observed["stability"],
        observed["repetition_ratio"],
        observed["transition_diversity"],
    )

    return {
        "normalized": observed["normalized"],
        "tokens": observed["tokens"],
        "score": observed["score"],
        "stability": observed["stability"],
        "repetition_ratio": observed["repetition_ratio"],
        "transition_diversity": observed["transition_diversity"],
        "drift": observed["drift"],
        "normalized_drift": observed["normalized_drift"],
        "summary_label": observed["summary_label"],
        "seed": seed,
        "baseline_mode": baseline_mode,
        "baseline": result["baseline"],
        "deltas": result["deltas"],
    }


def classify_summary(stability, repetition_ratio, transition_diversity):
    if stability >= 0.7 and repetition_ratio >= 0.4:
        return "high_repetition_stable"
    if transition_diversity >= 0.8 and stability < 0.7:
        return "high_transition_variability"
    if stability >= 0.4 and transition_diversity >= 0.4:
        return "balanced_structure"
    return "low_structure"


def main():
    parser = argparse.ArgumentParser(description="Sigilith-M CLI")
    parser.add_argument("input", help="Path to input text file")
    parser.add_argument("output", help="Path to output JSON file")
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for shuffled baseline comparison",
    )
    parser.add_argument(
        "--baseline-mode",
        choices=["shuffle", "sorted"],
        default="shuffle",
        help="Baseline mode to compare against",
    )
    args = parser.parse_args()

    text = read_text_file(args.input)
    profile = build_profile_from_text(
        text,
        seed=args.seed,
        baseline_mode=args.baseline_mode,
    )
    saved = save_json(profile, args.output)
    print(f"Saved profile to: {saved}")


if __name__ == "__main__":
    main()
