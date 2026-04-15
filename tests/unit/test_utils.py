from sigilith_m.utils import normalize_text, tokenize


def test_normalize_text():
    assert normalize_text("  HELLO   world  ") == "hello world"


def test_tokenize():
    assert tokenize("  HELLO   world hello ") == ["hello", "world", "hello"]
