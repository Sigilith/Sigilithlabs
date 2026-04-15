import argparse
from pathlib import Path

from sigilith_m.export import save_json


def build_profile_from_text(text):
    tokens = [t for t in text.strip().lower().split() if t]

    total = len(tokens)
    unique = len(set(tokens))
    score = total + unique if total else 0

    if total:
        counts = {}
        for token in tokens:
            counts[token] = counts.get(token, 0) + 1
        most_common = max(counts.values())
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

    if stability >= 0.7 and repetition_ratio >= 0.4:
        summary_label = "high_repetition_stable"
    elif transition_diversity >= 0.8 and stability < 0.7:
        summary_label = "high_transition_variability"
    elif stability >= 0.4 and transition_diversity >= 0.4:
        summary_label = "balanced_structure"
    else:
        summary_label = "low_structure"

    return {
        "normalized": " ".join(tokens),
        "tokens": tokens,
        "score": score,
        "stability": stability,
        "repetition_ratio": repetition_ratio,
        "transition_diversity": transition_diversity,
        "summary_label": summary_label,
    }


def main():
    parser = argparse.ArgumentParser(description="Sigilith-M CLI")
    parser.add_argument("input", help="Path to input text file")
    parser.add_argument("output", help="Path to output JSON file")
    args = parser.parse_args()

    input_path = Path(args.input)
    text = input_path.read_text(encoding="utf-8")
    profile = build_profile_from_text(text)
    saved = save_json(profile, args.output)
    print(f"Saved profile to: {saved}")


if __name__ == "__main__":
    main()
