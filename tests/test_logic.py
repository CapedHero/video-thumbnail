from pathlib import Path

from main import save_first_non_black_frame


def test_save_first_non_black_frame():
    # GIVEN
    input_file_path = str(Path(".") / "tests" / "test-video.mp4")

    # WHEN
    output_file_path = save_first_non_black_frame(input_file_path)

    # THEN
    actual_thumbnail = output_file_path.read_bytes()
    expected_thumbnail = (Path(".") / "tests" / "test-video-thumbnail.jpg").read_bytes()
    assert actual_thumbnail == expected_thumbnail
