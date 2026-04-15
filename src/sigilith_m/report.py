def format_float(value, digits=4):
    if isinstance(value, (int, float)):
        return f"{value:.{digits}f}"
    return str(value)


def profile_metrics_table(name, profile):
    metrics = profile.get("metrics", {})
    lines = [
        f"## {name}",
        "",
        f"- **Normalized:** `{profile.get('normalized', '')}`",
        f"- **Summary label:** `{profile.get('classification', {}).get('summary_label', '')}`",
        "",
        "| Metric | Value |",
        "|---|---:|",
    ]

    for key, value in metrics.items():
        lines.append(f"| {key} | {format_float(value)} |")

    return "\n".join(lines)


def comparison_table(comparison):
    lines = [
        "## Comparison",
        "",
        f"- **Euclidean distance:** {format_float(comparison.get('euclidean_distance', 0.0))}",
        f"- **Cosine similarity:** {format_float(comparison.get('cosine_similarity', 0.0))}",
        "",
        "| Delta Metric | Value |",
        "|---|---:|",
    ]

    for key, value in comparison.get("metric_deltas", {}).items():
        lines.append(f"| {key} | {format_float(value)} |")

    return "\n".join(lines)


def generate_comparison_report(payload):
    profile_a = payload.get("profile_a", {})
    profile_b = payload.get("profile_b", {})
    comparison = payload.get("comparison", {})
    metadata = payload.get("metadata", {})

    parts = [
        "# Sigilith-M Comparative Report",
        "",
        "## Metadata",
        "",
        f"- **Seed:** `{metadata.get('seed', '')}`",
        f"- **Baseline mode:** `{metadata.get('baseline_mode', '')}`",
        f"- **Window size:** `{metadata.get('window_size', '')}`",
        f"- **Block size:** `{metadata.get('block_size', '')}`",
        "",
        profile_metrics_table("Profile A", profile_a),
        "",
        profile_metrics_table("Profile B", profile_b),
        "",
        comparison_table(comparison),
        "",
    ]

    return "\n".join(parts)
