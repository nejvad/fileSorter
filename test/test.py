import os
import pathlib
import unittest

from src.main import create_folders


class TestFileSorter(unittest.TestCase):
    @staticmethod
    def AssertIfDirectory(path):
        if not pathlib.Path(path).resolve().is_dir():
            raise AssertionError("Directory does not exist: %s" % str(path))

    def test_if_sorted_download_folder_exists_on_path(self):
        create_folders(os.environ.get("DOWNLOAD_DIR_PATH"), os.environ.get("SORTED_DOWNLOAD_DIR_PATH"))
        self.AssertIfDirectory(os.environ["SORTED_DOWNLOAD_DIR_PATH"])
