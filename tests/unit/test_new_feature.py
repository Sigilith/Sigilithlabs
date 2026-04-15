from sigilith.new_feature.components.core import CoreEngine


def test_core_engine_process():
    engine = CoreEngine()
    assert engine.process("  HELLO  ") == "hello"
