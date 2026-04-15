import argparse

from sigilith_m.export import save_json
from sigilith_m.io import read_text_file, write_text_file
from sigilith_m.profile import build_profile_from_text
from sigilith_m.compare import compare_profiles
from sigilith_m.report import generate_comparison_report


def add_common_options(parser):
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


def build_single_profile(input_path, seed, baseline_mode, window_size, block_size):
    text = read_text_file(input_path)
    return build_profile_from_text(
        text,
        seed=seed,
        baseline_mode=baseline_mode,
        window_size=window_size,
        block_size=block_size,
    )


def main():
    parser = argparse.ArgumentParser(description="Sigilith-M CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    profile_parser = subparsers.add_parser("profile", help="Build a profile from one input file")
    profile_parser.add_argument("input", help="Path to input text file")
    profile_parser.add_argument("output", help="Path to output JSON file")
    add_common_options(profile_parser)

    compare_parser = subparsers.add_parser("compare", help="Compare two input files")
    compare_parser.add_argument("input_a", help="Path to first input text file")
    compare_parser.add_argument("input_b", help="Path to second input text file")
    compare_parser.add_argument("output", help="Path to output JSON file")
    add_common_options(compare_parser)

    report_parser = subparsers.add_parser("report", help="Generate a Markdown comparison report")
    report_parser.add_argument("input_a", help="Path to first input text file")
    report_parser.add_argument("input_b", help="Path to second input text file")
    report_parser.add_argument("output", help="Path to output Markdown file")
    add_common_options(report_parser)

    args = parser.parse_args()

    if args.command == "profile":
        profile = build_single_profile(
            args.input,
            seed=args.seed,
            baseline_mode=args.baseline_mode,
            window_size=args.window_size,
            block_size=args.block_size,
        )
        saved = save_json(profile, args.output)
        print(f"Saved profile to: {saved}")
        return

    if args.command == "compare":
        profile_a = build_single_profile(
            args.input_a,
            seed=args.seed,
            baseline_mode=args.baseline_mode,
            window_size=args.window_size,
            block_size=args.block_size,
        )
        profile_b = build_single_profile(
            args.input_b,
            seed=args.seed,
            baseline_mode=args.baseline_mode,
            window_size=args.window_size,
            block_size=args.block_size,
        )

        comparison = compare_profiles(profile_a, profile_b)

        payload = {
            "profile_a": profile_a,
            "profile_b": profile_b,
            "comparison": comparison,
            "metadata": {
                "seed": args.seed,
                "baseline_mode": args.baseline_mode,
                "window_size": args.window_size,
                "block_size": args.block_size,
            },
        }

        saved = save_json(payload, args.output)
        print(f"Saved comparison to: {saved}")
        return

    if args.command == "report":
        profile_a = build_single_profile(
            args.input_a,
            seed=args.seed,
            baseline_mode=args.baseline_mode,
            window_size=args.window_size,
            block_size=args.block_size,
        )
        profile_b = build_single_profile(
            args.input_b,
            seed=args.seed,
            baseline_mode=args.baseline_mode,
            window_size=args.window_size,
            block_size=args.block_size,
        )

        comparison = compare_profiles(profile_a, profile_b)

        payload = {
            "profile_a": profile_a,
            "profile_b": profile_b,
            "comparison": comparison,
            "metadata": {
                "seed": args.seed,
                "baseline_mode": args.baseline_mode,
                "window_size": args.window_size,
                "block_size": args.block_size,
            },
        }

        report = generate_comparison_report(payload)
        saved = write_text_file(args.output, report)
        print(f"Saved report to: {saved}")
        return


if __name__ == "__main__":
    main()
