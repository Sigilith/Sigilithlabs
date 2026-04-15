from pathlib import Path

from sigilith_m.io import read_text_file, write_text_file


def test_write_and_read_text_file(tmp_path):
    output_path = tmp_path / "example.txt"
    saved = write_text_file(output_path, "hello sigilith")

    assert Path(saved).exists()
    assert read_text_file(output_path) == "hello sigilith"
