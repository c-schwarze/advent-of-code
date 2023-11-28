import unittest

from year2022.day1 import part1


class TestPart1(unittest.TestCase):
    def test_empty_value(self):
        test_input = []
        actual = part1(test_input)
        expected = 0
        self.assertEqual(actual, expected)

    def test_single_value(self):
        test_input = [['100']]
        actual = part1(test_input)
        expected = 100
        self.assertEqual(actual, expected)

    def test_multiple_values(self):
        test_input = [['100', '200', '400'], ['5600']]
        actual = part1(test_input)
        expected = 5600
        self.assertEqual(actual, expected)

    def test_non_string_values(self):
        test_input = [[5600]]
        actual = part1(test_input)
        expected = 5600
        self.assertEqual(actual, expected)

    def test_non_numeric_values(self):
        with self.assertRaises(ValueError):
            test_input = [['a'], ['b', 'c']]
            part1(test_input)