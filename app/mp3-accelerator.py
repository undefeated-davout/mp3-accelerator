# -*- coding: utf-8

import argparse
import glob
import os
import subprocess

input_dir = "./data/input/"
output_dir = "./data/output/"


def main(speed):
    file_paths = glob.glob(input_dir + "*.mp3")
    print("ファイル数: " + str(len(file_paths)))
    count = 1
    for file_path in file_paths:
        print(str(count) + "個目処理中: " + file_path)
        file_name = os.path.basename(file_path)
        output_path = output_dir + file_name
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
        count += 1


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
