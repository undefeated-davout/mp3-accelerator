# -*- coding: utf-8

import argparse
import glob
import os
import subprocess
from concurrent.futures import ProcessPoolExecutor

INPUT_DIR = "./data/input/"
OUTPUT_DIR = "./data/output/"
MAX_WORKERS = 4


def conv_mp3(file_path, decibel):
    file_name = os.path.basename(file_path)
    output_path = OUTPUT_DIR + file_name
    subprocess.run(
        [
            "ffmpeg",
            "-i",
            file_path,
            "-af",
            "volume=" + str(decibel) + "dB",
            output_path,
        ]
    )


def main(decibel):
    file_paths = glob.glob(INPUT_DIR + "*.mp3")
    file_count = len(file_paths)
    print("ファイル数: " + str(file_count))

    with ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executor.map(conv_mp3, file_paths, [decibel] * file_count)
        print("タスクセット完了")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="mp3の音量を変更する")
    parser.add_argument(
        "decibel",
        type=float,
        help="デシベル",
    )
    args = parser.parse_args()
    print("デシベル: " + str(args.decibel))

    main(args.decibel)

    print("処理完了")
