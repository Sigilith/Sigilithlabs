from pathlib import Path


def normalize_text(text):
    return " ".join(text.strip().lower().split())


def tokenize(text):
    return [t for t in normalize_text(text).split(" ") if t]


def read_text_file(path):
    return Path(path).read_text(encoding="utf-8")
