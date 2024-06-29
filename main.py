from os import listdir


def main():
    download_folder_path = "C:\\Users\\jenes\\Downloads"
    files = listdir(download_folder_path)
    extensions = set()

    for file in files:
        extensions.add(file.split(".")[-1])

    print(extensions)


if __name__ == "__main__":
    main()
