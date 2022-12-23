# -*- coding: utf-8

import glob
import os
import shutil

INPUT_DIR = "./data/input/"
OUTPUT_DIR = "./data/output/"


def main():
    file_paths = glob.glob(INPUT_DIR + "*.mp4")
    file_paths = sorted(file_paths)
    file_count = len(file_paths)
    print("num of files: " + str(file_count))

    count = 1
    tmp_head_name = ""
    for file_path in file_paths:
        org_file_name = os.path.basename(file_path)
        # retrieve the head name which is splitted by "_"
        head_name = org_file_name.split("_")[0]
        # reset on new head name
        if head_name != tmp_head_name:
            count = 1
        # ${HEADNAME}_${COUNT}
        output_path = (
            OUTPUT_DIR + head_name + "_" + format(count, "02") + ".mp4"
        )
        print(output_path)
        count += 1
        tmp_head_name = head_name
        # copy as new file name
        shutil.copy(file_path, output_path)


if __name__ == "__main__":
    main()
    print("process done")
