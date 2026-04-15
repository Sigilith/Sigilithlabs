def summary_label(stability, repetition_ratio, transition_diversity):
    """
    Simple summary classifier for Sigilith-M outputs.
    """
    if stability >= 0.7 and repetition_ratio >= 0.4:
        return "high_repetition_stable"
    if transition_diversity >= 0.8 and stability < 0.7:
        return "high_transition_variability"
    if stability >= 0.4 and transition_diversity >= 0.4:
        return "balanced_structure"
    return "low_structure"
