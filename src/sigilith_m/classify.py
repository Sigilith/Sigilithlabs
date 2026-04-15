def summary_label(
    stability,
    repetition_ratio,
    transition_diversity,
    stability_index_value=None,
):
    """
    Simple summary classifier for Sigilith-M outputs.

    If stability_index_value is provided, it can override weaker heuristics
    and identify strongly stable systems more directly.
    """
    if stability_index_value is not None and stability_index_value >= 0.75:
        return "high_structural_stability"

    if stability >= 0.7 and repetition_ratio >= 0.4:
        return "high_repetition_stable"
    if transition_diversity >= 0.8 and stability < 0.7:
        return "high_transition_variability"
    if stability >= 0.4 and transition_diversity >= 0.4:
        return "balanced_structure"
    return "low_structure"
