from pycloudformer.environment import *

cd = os.getcwd() + '\\output\\CloudFormationStack.yaml'


def compiler():
    """
    handles the yaml builder class to generate the templates
    :return: none
    """
    Environment('../pycloudformer/configs/StaticServices.yaml').stack_analyzer()
    YamlBuilder('configs/StaticServices.yaml', 'templates/template.j2',
                'output/CloudFormationStack.yaml').build_yaml()
    print('Output saved at: {}'.format(cd))


def main():
    compiler()


if __name__ == '__main__':
    main()
