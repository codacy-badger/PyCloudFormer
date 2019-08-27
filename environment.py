import os

__environment__ = [
    'templates/',
    'configs/',
    'output/',
]


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


def environment(env=None):
    """
    generates environment for pycloudformer
    :param env: environment variables
    :return: none
    """
    if env is None:
        env = __environment__
    for e in env:
        if not find_dir(e):
            make_dir(e)
