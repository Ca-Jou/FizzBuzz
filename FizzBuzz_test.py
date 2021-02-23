import unittest
from FizzBuzz import FizzBuzz


class FizzBuzzTest(unittest.TestCase):

    def test_should_raise_error_when_zero(self):
        with self.assertRaises(ValueError):
            FizzBuzz.answer(0)

    def test_should_raise_error_when_negative(self):
        with self.assertRaises(ValueError):
            FizzBuzz.answer(-2)

    def test_should_return_fizz_when_3_is_multiple(self):
        actual = FizzBuzz.answer(6)
        expected = 'Fizz'
        self.assertEqual(expected, actual, 'Should be Fizz GROSSE POMPE ! ')

    def test_should_be_buzz_when_5_is_multiple(self):
        actual = FizzBuzz.answer(10)
        expected = 'Buzz'
        self.assertEqual(expected, actual, 'Should be Buzz, GROSSE POMPE !')