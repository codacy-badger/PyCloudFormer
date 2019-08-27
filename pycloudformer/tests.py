import unittest

from pycloudformer.environment import *


class TestSum(unittest.TestCase):

    def test_find_dir(self):
        assert find_dir('../pycloudformer') is True, 'should return True'


if __name__ == '__main__':
    unittest.main()
