import unittest

from main import say_hi, add, insult


class TestHi(unittest.TestCase):
    def test_hi(self):
        self.assertEqual(say_hi(), "Hi!")

    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add('py', 'thon'), 'python')
        self.assertEqual(add([1, 2, 3], [4, 5]), [1, 2, 3, 4, 5])

    def test_add_negative(self):
        with self.assertRaises(TypeError):
            add(2, 'str')
            add([2], 'str')
            add({2}, 'str')

    def test_insult(self):
        self.assertEqual(insult('Igor'), 'You are such a faggot, Igor!')


if __name__ == "__main__":
    unittest.main()
