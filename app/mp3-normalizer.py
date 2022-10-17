# -*- coding: utf-8

import argparse
import glob
import os
import subprocess
from concurrent.futures import ProcessPoolExecutor

INPUT_DIR = "./data/input/"
OUTPUT_DIR = "./data/output/"
MAX_WORKERS = 4


def conv_mp3(file_path):
    file_name = os.path.basename(file_path)
    output_path = OUTPUT_DIR + file_name
    subprocess.run(
        [
            "ffmpeg-normalize",
            file_path,
            "-c:a",
            "libmp3lame",
            "-o",
            output_path,
        ]
    )


def main():
    file_paths = glob.glob(INPUT_DIR + "*.mp3")
    file_count = len(file_paths)
    print("ファイル数: " + str(file_count))

    with ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executor.map(conv_mp3, file_paths)
        print("タスクセット完了")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="mp3の音量を正規化する")
    args = parser.parse_args()

    main()

    print("処理完了")
