import os
import shutil
from os.path import exists


def main():
    download_folder_path = "C:\\Users\\jenes\\Downloads"
    sorted_files_path = "C:\\Users\\jenes\\Sorted Downloads"
    files = os.listdir(download_folder_path)
    extensions = set()

    if not exists(sorted_files_path):
        os.mkdir(sorted_files_path)

    for file in files:
        extensions.add(file.split(".")[-1])

    for extension in extensions:
        os.mkdir(sorted_files_path + "\\" + extension)

    for file in files:
        shutil.move(download_folder_path + "\\" + file, sorted_files_path + "\\" + file.split(".")[-1])


if __name__ == "__main__":
    main()
