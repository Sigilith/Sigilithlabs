from src.sigilith.new_feature.components.utils import normalize

def test_normalize_strips_and_lowercases():
    assert normalize("  WORLD  ") == "world"

def test_normalize_non_string_passthrough():
    assert normalize(123) == 123
