import argparse
import os

from kaggle.api.kaggle_api_extended import KaggleApi
from logger_custom import app_logger


def get_kaggle_csv(path="./dbt/kaggle_files") -> None:
    """
    The function `get_kaggle_csv` downloads files from a Kaggle dataset to a specified path.

    :param path: The `path` parameter in the `get_kaggle_csv` function is the directory path where the
    Kaggle dataset files will be downloaded. By default, it is set to "./kaggle_files", which means that
    the files will be downloaded to a directory named "kaggle_files", defaults to ./kaggle_files
    (optional)
    """

    app_logger.info(f"Working dir is => {os.getcwd()}")
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(
        "bhanupratapbiswas/superstore-sales", path=path, unzip=True
    )
    return app_logger.info("Files downloaded successfully")


def main_kaggle(rename, src, dst) -> None:
    """
    The function `main_kaggle` checks if a file exists, renames it if specified, and prints a completion
    message.
    
    :param rename: The `rename` parameter in the `main_kaggle` function is a boolean flag that
    determines whether the file should be renamed or not. If `rename` is `True`, the function will
    attempt to rename the file from the source path (`src`) to the destination path (`dst`). If
    :param src: The `src` parameter in the `main_kaggle` function is typically used to specify the
    source file path or location. It is the file that you want to rename or perform operations on within
    the function
    :param dst: The `dst` parameter in the `main_kaggle` function represents the destination path where
    the file will be moved or renamed to. It is the new path or name that you want the file to have
    after the renaming operation
    :return: The function `main_kaggle` is returning a print statement indicating that the file rename
    operation has been completed successfully.
    """
    if src is None or not isinstance(src, (str, bytes, os.PathLike)):
        app_logger.error("The 'src' parameter is None or not a valid path type.")
        raise ValueError("The 'src' parameter must be a valid path.")
    
    if dst is None or not isinstance(src, (str, bytes, os.PathLike)):
        app_logger.error("The 'dst' parameter is None or not a valid path type.")
        raise ValueError("The 'dst' parameter must be a valid path.")

    if os.path.exists(src):
        app_logger.info(f"The source file {src} exist.")
    else:
        app_logger.info(f"The source file {src} does not exist.")
        raise FileNotFoundError
    
    if os.path.exists(dst):
        app_logger.info(f"The destination file {dst} exist.")
    else:
        app_logger.info(f"The destination file {dst} does not exist.")
        raise FileNotFoundError

    if rename and src and dst:
        os.rename(src=src, dst=dst)
    return app_logger.info("File rename completed successfully")


def parse_args() -> argparse.Namespace:
    """
    The function `parse_args` defines a command-line argument parser with options for renaming a file.
    :return: The `parse_args()` function returns an `argparse.Namespace` object containing the parsed
    arguments from the command line.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--rename", action="store_true")
    parser.add_argument("--src", type=str, help="The name of the file to rename")
    parser.add_argument("--dst", type=str, help="The name of the file after rename")
    return parser.parse_args()


if __name__ == "__main__":
    app_logger.info(f"Working dir is => {os.getcwd()}")
    args = parse_args()
    main_kaggle(args.rename, args.src, args.dst)
