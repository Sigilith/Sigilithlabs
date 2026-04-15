from pathlib import Path


def read_text_file(path):
    return Path(path).read_text(encoding="utf-8")


def write_text_file(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return str(path)
