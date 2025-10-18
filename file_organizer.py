"""A Python script that automatically sorts and moves files in a directory 
into organized folders based on their file types (e.g., images, documents, videos, etc.).
"""

import os
import sys
import shutil


def filter_by_ext(file_list, target_ext) -> bool:
    """filter the list based on target ext"""
    result = []
    for file in file_list:
        for ext in target_ext:
            if file.endswith(ext):
                result.append(file)
    return result


def create_dir(file_list, file_path):
    """create directory based on file extension of each file"""
    for file in file_list:
        try:
            ext = file.split('.')[-1]
            os.mkdir(f'{file_path}\\{ext}')
        except FileExistsError:
            # File already exist, skipping the file creation
            continue


def arrange_files(file_list, file_path):
    """sort the files and move them to the corresponding locations"""
    for file in file_list:
        ext = file.split('.')[-1]
        src = f'{file_path}\\{file}'
        dst = f'{file_path}\\{ext}'
        shutil.move(src, dst)


def file_organizer(file_path: str, target_ext):
    """ Start point of program """
    file_list = os.listdir(file_path)
    filtered_list = filter_by_ext(file_list, target_ext)

    create_dir(filtered_list, file_path)
    arrange_files(filtered_list, file_path)


if __name__ == "__main__":
    if (len(sys.argv) > 1):
        path = sys.argv[1]
        exts = sys.argv[2:]
        file_organizer(path, exts)
    else:
        print(
            "Invalid argument; file_organizer.py {path} {...target extension}")
