import argparse

from sigilith_m.export import save_json
from sigilith_m.io import read_text_file
from sigilith_m.profile import build_profile_from_text


def main():
    parser = argparse.ArgumentParser(description="Sigilith-M CLI")
    parser.add_argument("input", help="Path to input text file")
    parser.add_argument("output", help="Path to output JSON file")
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for baseline comparison",
    )
    parser.add_argument(
        "--baseline-mode",
        choices=["shuffle", "sorted", "local_shuffle", "block_shuffle"],
        default="shuffle",
        help="Baseline mode to compare against",
    )
    parser.add_argument(
        "--window-size",
        type=int,
        default=3,
        help="Window size for local shuffle baseline",
    )
    parser.add_argument(
        "--block-size",
        type=int,
        default=3,
        help="Block size for block-preserving shuffle baseline",
    )
    args = parser.parse_args()

    text = read_text_file(args.input)
    profile = build_profile_from_text(
        text,
        seed=args.seed,
        baseline_mode=args.baseline_mode,
        window_size=args.window_size,
        block_size=args.block_size,
    )
    saved = save_json(profile, args.output)
    print(f"Saved profile to: {saved}")


if __name__ == "__main__":
    main()
