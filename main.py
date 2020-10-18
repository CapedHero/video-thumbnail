import argparse
import os
import platform
import tempfile
from pathlib import Path
from typing import Optional

import numpy as np
from cv2 import cv2


BLACKNESS_THRESHOLD = 20


def save_first_non_black_frame(input_file_path: str) -> Path:
    last_non_black_frame = _get_first_non_black_frame(input_file_path)
    output_file_path = _get_output_file_path(input_file_path)
    cv2.imwrite(str(output_file_path), last_non_black_frame)
    return output_file_path


def _get_first_non_black_frame(input_file_path: str) -> Optional[np.ndarray]:
    """
    A serious optimization could result from processing video backward so that
    we short-circuit looping over frames as soon as we find the first non-black
    frame. However, an initial investigation revealed that it might be impossible
    (see https://stackoverflow.com/a/11260842/7483239). To finally determine, it
    would require more thorough research.
    """
    video_capture = cv2.VideoCapture(input_file_path)
    frames_num = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    current_frame_num = 1
    last_non_black_frame = None

    while video_capture.isOpened():
        _, frame = video_capture.read()

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if np.average(gray_frame) > BLACKNESS_THRESHOLD:
            last_non_black_frame = frame

        if current_frame_num >= frames_num:
            video_capture.release()
            break

        current_frame_num += 1

    return last_non_black_frame


def _get_output_file_path(input_file_path: str) -> Path:
    root_temp_dir = Path("/tmp" if platform.system() == "Darwin" else tempfile.gettempdir())
    temp_dir = root_temp_dir / "videos-thumbnails"
    temp_dir.mkdir(parents=True, exist_ok=True)
    input_file_basename = os.path.basename(input_file_path)
    input_file_path_root, _ = os.path.splitext(input_file_basename)
    output_file_path = temp_dir / f"{input_file_path_root}.jpg"
    return output_file_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-file-path", dest="input_file_path", required=True)
    args = parser.parse_args()

    output_file_path = save_first_non_black_frame(args.input_file_path)
    print(f"Video thumbnail saved in: {output_file_path}")
