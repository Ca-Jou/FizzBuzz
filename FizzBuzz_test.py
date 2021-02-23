import unittest

class FizzBuzzTest(unittest.TestCase):

    def test_should_raise_error_when_zero(self):
        with self.assertRaises(ValueError):
            FizzBuzz.answer(0)
