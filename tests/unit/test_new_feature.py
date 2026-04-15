from sigilith.new_feature.components.core import CoreEngine


def test_core_engine_process_structure():
    engine = CoreEngine()
    result = engine.process("  HELLO world hello  ")

    assert result["normalized"] == "hello world hello"
    assert result["tokens"] == ["hello", "world", "hello"]
    assert result["score"] == 5


def test_core_engine_rejects_none():
    engine = CoreEngine()
    import pytest
    with pytest.raises(ValueError):
        engine.process(None)
