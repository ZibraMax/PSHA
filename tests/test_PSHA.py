import unittest

from PSHA.PSHA import A


class TestA(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(5, 5)


if __name__ == '__main__':
    unittest.main()