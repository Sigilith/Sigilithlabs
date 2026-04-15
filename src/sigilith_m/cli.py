import argparse
from pathlib import Path

from sigilith_m.export import save_json
from sigilith_m.baseline import compare_to_baseline


def build_profile_from_text(text, seed=42):
    tokens = [t for t in text.strip().lower().split() if t]
    result = compare_to_baseline(tokens, seed=seed)

    observed = result["observed"]
    observed["normalized"] = " ".join(tokens)
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
    args = parser.parse_args()

    input_path = Path(args.input)
    text = input_path.read_text(encoding="utf-8")
    profile = build_profile_from_text(text, seed=args.seed)
    saved = save_json(profile, args.output)
    print(f"Saved profile to: {saved}")


if __name__ == "__main__":
    main()
