def normalize_text(text):
    return " ".join(text.strip().lower().split())


def tokenize(text):
    return [t for t in normalize_text(text).split(" ") if t]
