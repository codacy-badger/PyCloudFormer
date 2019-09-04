import unittest

from pycloudformer.environment import *


class TestSum(unittest.TestCase):

    def test_find_dir(self):
        if find_dir('../pycloudformer') is not True:
            raise AssertionError('test_find_dir should return True')

    def test_load_yaml(self):
        if isinstance(YamlBuilder.load_yaml('../pycloudformer/configs/StaticServices.yaml'), dict) is not True:
            raise AssertionError('test_load_yaml should return True')


if __name__ == '__main__':
    unittest.main()
