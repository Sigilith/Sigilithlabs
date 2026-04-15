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
    """
    if len(tokens) < 2:
        return 0.0

    raw = recurrence_drift(tokens)
    denom = len(tokens) - 1
    if denom <= 0:
        return 0.0
    return raw / denom


def windowed_recurrence_drift(tokens, window_size=3):
    """
    Compute recurrence drift across sliding windows and return the average.
    """
    if len(tokens) < window_size or window_size < 2:
        return 0.0

    values = []
    for i in range(len(tokens) - window_size + 1):
        window = tokens[i:i + window_size]
        values.append(recurrence_drift(window))

    if not values:
        return 0.0
    return sum(values) / len(values)
