import os

from pycloudformer.cloudformation import *

__supported_services__ = [
    'GlueJob',
    'GlueClassifier',
    'GlueDatabase',
    'GlueCrawler',
    'S3Bucket',
    'LambdaFunction',
    'EventRule'
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


class Environment:
    def __init__(self, directory):
        self.directory = directory

    def stack_analyzer(self):
        """
        analyses the stack to check if the suggested service is supported
        :return: value error
        """
        tmp = YamlBuilder.load_yaml(self.directory)
        for v in tmp.values():
            for k in v:
                if k not in __supported_services__:
                    raise ValueError(
                        '{} is either not a supported service or the service was not specified in the stack'.format(k))
