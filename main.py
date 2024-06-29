import os
import shutil
from os.path import exists


def main():
    download_folder_path = "C:\\Users\\jenes\\Downloads"
    sorted_files_path = "C:\\Users\\jenes\\Sorted Downloads"
    create_folders(download_folder_path, sorted_files_path)
    sort_files(download_folder_path, sorted_files_path)


def create_folders(download, sorted_download):
    files = os.listdir(download)

    if not exists(sorted_download):
        os.mkdir(sorted_download)

    for file in files:
        current_path = sorted_download + "\\" + file.split(".")[-1]
        if not exists(current_path):
            os.mkdir(current_path)


def sort_files(download, sorted_download):
    files = os.listdir(download)

    for file in files:
        shutil.move(download + "\\" + file, sorted_download + "\\" + file.split(".")[1])


if __name__ == "__main__":
    main()
