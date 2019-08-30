import os


def make_dir(e):
    """
    ensures all necessary directories are present in the environment
    :param e: directory
    :return: none
    """
    os.makedirs(os.path.dirname(e), exist_ok=True)


def find_dir(e):
    """
    tests to see if a directory exists
    :param e: directory
    :return: boolean
    """
    return os.path.exists(os.path.dirname(e))
