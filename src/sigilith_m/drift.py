from collections import defaultdict


def recurrence_drift(tokens):
    """
    Average spacing between repeated occurrences of the same token.
    Higher = repeated symbols are more spread out.
    Lower = repeated symbols are more locally clustered.
    """
    positions = defaultdict(list)
    for i, token in enumerate(tokens):
        positions[token].append(i)

    gaps = []
    for pos_list in positions.values():
        if len(pos_list) < 2:
            continue
        for a, b in zip(pos_list, pos_list[1:]):
            gaps.append(b - a)

    if not gaps:
        return 0.0

    return sum(gaps) / len(gaps)


def normalized_recurrence_drift(tokens):
    """
    Normalize recurrence drift by sequence length - 1.
    Returns a value between 0 and 1 for non-empty repeated sequences.
    """
    if len(tokens) < 2:
        return 0.0

    raw = recurrence_drift(tokens)
    denom = len(tokens) - 1
    if denom <= 0:
        return 0.0
    return raw / denom
