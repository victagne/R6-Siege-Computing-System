import os
import shutil
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def clear_folder(dir_path: str) -> None:
    """
    Clear a specified folder.

    Args:
        dir_path (str): the folder to be cleared.

    Returns:
        None
    """
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        shutil.rmtree(dir_path)
        os.mkdir(dir_path)
        logging.info(f"Folder {dir_path} is cleaned.")
    else:
        logging.warning(f"Folder {dir_path} doesn't exist.")


def prepare_folder(dir_path: str) -> None:
    """
    Create a folder if it does not exist
    Args:
        dir_path (str): the path of the folder to be created
    Returns:
        None
    """
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        logging.info(f"Folder {dir_path} is created.")


def sort_file_by_operator_id(file_path: str) -> None:
    """
    Sort a file's content by operator ID in ascending order
    Args:
        file_path (str): the path of the file containing operator data
    Returns:
        None
    """
    operator_data = []

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                operator_id, matches = line.split('|')
                operator_data.append((int(operator_id), matches))

    sorted_data = sorted(operator_data, key=lambda x: x[0])

    with open(file_path, 'w') as f:
        for operator_id, matches in sorted_data:
            f.write(f"{operator_id}|{matches}\n")
