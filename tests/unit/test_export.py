from pathlib import Path
import json

from src.sigilith_m.export import to_dict, save_json


def test_to_dict_basic():
    profile = {
        "name": "seq1",
        "score": 5,
        "phase_space": [(0.5, 0.4), (0.7, 0.3)],
        "terrain": {"basins": 0.4},
    }

    result = to_dict(profile)

    assert result["name"] == "seq1"
    assert result["score"] == 5
    assert result["phase_space"] == [[0.5, 0.4], [0.7, 0.3]]
    assert result["terrain"]["basins"] == 0.4


def test_save_json(tmp_path):
    profile = {
        "name": "seq2",
        "score": 7,
        "phase_space": [(1.0, 0.2)],
    }

    output_path = tmp_path / "profile.json"
    saved = save_json(profile, output_path)

    assert Path(saved).exists()

    data = json.loads(Path(saved).read_text(encoding="utf-8"))
    assert data["name"] == "seq2"
    assert data["score"] == 7
    assert data["phase_space"] == [[1.0, 0.2]]
