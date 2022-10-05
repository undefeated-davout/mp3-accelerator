# -*- coding: utf-8

import argparse
import glob
import os
import subprocess
from concurrent.futures import ProcessPoolExecutor

INPUT_DIR = "./data/input/"
OUTPUT_DIR = "./data/output/"
MAX_WORKERS = 4


def conv_mp3(file_path, speed):
    file_name = os.path.basename(file_path)
    output_path = OUTPUT_DIR + file_name
    subprocess.run(
        [
            "ffmpeg",
            "-i",
            file_path,
            "-af",
            "atempo=" + str(speed),
            output_path,
        ]
    )


def main(speed):
    file_paths = glob.glob(INPUT_DIR + "*.mp3")
    file_count = len(file_paths)
    print("ファイル数: " + str(file_count))

    with ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executor.map(conv_mp3, file_paths, [speed] * file_count)
        print("タスクセット完了")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="mp3の速度を変更する")
    parser.add_argument(
        "speed",
        type=float,
        help="変換倍率",
    )
    args = parser.parse_args()
    print("倍率: " + str(args.speed))

    main(args.speed)

    print("処理完了")
