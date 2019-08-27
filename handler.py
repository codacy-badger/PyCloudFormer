from cloudformation import YamlBuilder
from environment import *


def compiler():
    """
    handles the yaml builder class to generate the templates
    :return: none
    """
    YamlBuilder('configs/root.yaml', 'templates/template.j2',
                'output/CloudFormationStack.yaml').build_yaml()


def main():
    environment()
    compiler()


if __name__ == '__main__':
    main()
