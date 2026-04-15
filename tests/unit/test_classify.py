from sigilith_m.classify import summary_label


def test_summary_label_high_structural_stability():
    assert summary_label(0.7, 0.5, 0.3, 0.8) == "high_structural_stability"


def test_summary_label_high_repetition_stable():
    assert summary_label(0.8, 0.5, 0.3, 0.6) == "high_repetition_stable"


def test_summary_label_high_transition_variability():
    assert summary_label(0.6, 0.2, 0.9, 0.4) == "high_transition_variability"


def test_summary_label_balanced_structure():
    assert summary_label(0.5, 0.2, 0.5, 0.4) == "balanced_structure"


def test_summary_label_low_structure():
    assert summary_label(0.2, 0.1, 0.2, 0.2) == "low_structure"
