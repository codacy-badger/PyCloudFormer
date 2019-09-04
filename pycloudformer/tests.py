from pycloudformer.environment import *


def test():
    if find_dir('../pycloudformer') is not True:
        raise AssertionError('test_find_dir should return True')

    if isinstance(YamlBuilder.load_yaml('../pycloudformer/configs/StaticServices.yaml'), dict) is not True:
        raise AssertionError('test_load_yaml should return True')

    print('All tests passed!')


if __name__ == '__main__':
    test()
