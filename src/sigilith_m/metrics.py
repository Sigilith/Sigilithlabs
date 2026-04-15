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
