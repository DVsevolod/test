import unittest

from .hi import say_hi


class TestHi(unittest.TestCase):
    def test_hi(self):
        self.assertEqual(say_hi(), "Hi!")


if __name__ == "__main__":
    unittest.main()