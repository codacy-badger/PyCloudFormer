from pycloudformer.environment import *


def compiler():
    """
    handles the yaml builder class to generate the templates
    :return: none
    """
    Environment('../pycloudformer/configs/StaticServices.yaml').stack_analyzer()
    YamlBuilder('configs/StaticServices.yaml', 'templates/template.j2',
                'output/CloudFormationStack.yaml').build_yaml()


def main():
    compiler()


if __name__ == '__main__':
    main()
