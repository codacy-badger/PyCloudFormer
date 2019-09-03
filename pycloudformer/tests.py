import unittest

from pycloudformer.environment import *
from pycloudformer.cloudformation import *


class TestSum(unittest.TestCase):

    def test_find_dir(self):
        assert find_dir('../pycloudformer') is True, 'should return True'

    def test_load_yaml(self):
        assert isinstance(YamlBuilder.load_yaml('../pycloudformer/configs/StaticServices.yaml'),
                          dict) is True, 'should return True'


if __name__ == '__main__':
    unittest.main()
