from collections import Counter


def score_tokens(tokens):
    """
    Basic score = total token count + unique token count.
    """
    total = len(tokens)
    unique = len(set(tokens))
    return total + unique if total else 0


def stability(tokens):
    """
    Stability = frequency of the most common token divided by total tokens.
    Returns a value between 0 and 1.
    """
    total = len(tokens)
    if total == 0:
        return 0.0
    counts = Counter(tokens)
    most_common = counts.most_common(1)[0][1]
    return most_common / total


def repetition_ratio(tokens):
    """
    Repetition ratio = repeated tokens / total tokens.
    """
    total = len(tokens)
    if total == 0:
        return 0.0
    unique = len(set(tokens))
    repeated = total - unique
    return repeated / total


def transition_diversity(tokens):
    """
    Transition diversity = unique adjacent transitions / total adjacent transitions.
    Returns a value between 0 and 1.
    """
    if len(tokens) < 2:
        return 0.0
    transitions = list(zip(tokens, tokens[1:]))
    return len(set(transitions)) / len(transitions)


def stability_index(stability_value, repetition_ratio_value, transition_diversity_value, normalized_drift_value):
    """
    Composite stability index in [0, 1].

    Higher means:
    - stronger dominant structure
    - more repetition
    - lower transition diversity
    - lower drift
    """
    value = (
        0.35 * stability_value
        + 0.25 * repetition_ratio_value
        + 0.20 * (1.0 - transition_diversity_value)
        + 0.20 * (1.0 - normalized_drift_value)
    )

    if value < 0.0:
        return 0.0
    if value > 1.0:
        return 1.0
    return value
