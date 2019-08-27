from pycloudformer.cloudformation import YamlBuilder
from pycloudformer.environment import *


def compiler():
    """
    handles the yaml builder class to generate the templates
    :return: none
    """
    YamlBuilder('pycloudformer/configs/StaticServices.yaml', 'pycloudformer/templates/template.j2',
                'pycloudformer/output/CloudFormationStack.yaml').build_yaml()


def main():
    environment()
    compiler()


if __name__ == '__main__':
    main()
