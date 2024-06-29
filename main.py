import os
import shutil
from time import ctime
from os.path import exists, getctime


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
        # TODO look for a more elegant solution
        file_creation_date = "_".join(str(ctime(getctime(download + "\\" + file))).split(" ")[:3])
        current_path_with_creation_date = current_path + "-" + file_creation_date

        if not is_folder_already_exists(current_path_with_creation_date):
            os.mkdir(current_path_with_creation_date)


def sort_files(download, sorted_download):
    files = os.listdir(download)

    for file in files:

        file_creation_date = "_".join(str(ctime(getctime(download + "\\" + file))).split(" ")[:3])
        shutil.move(download + "\\" + file, sorted_download + "\\" + file.split(".")[1] + "-" + file_creation_date)


def is_folder_already_exists(path):
    return exists(path)


if __name__ == "__main__":
    main()
