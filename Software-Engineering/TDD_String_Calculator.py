import unittest
from String_Calculator import add

class TestStringCalculator(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_two_numbers(self):
        self.assertEqual(add("1,2"), 3)

    def test_unknown_amount_of_numbers(self):
        self.assertEqual(add("1,2,3,4,5,6"), 21)

    def test_new_line_between_numbers(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)

    def test_negative_numbers_exception(self):
        with self.assertRaisesRegex(ValueError, "negatives not allowed: -2,-4"):
            add("1,-2,3,-4")

    def test_ignore_numbers_greater_than_1000(self):
        self.assertEqual(add("2,1001"), 2)

    def test_long_delimiters(self):
        # Support for //[***]\n1***2***3
        self.assertEqual(add("//[***]\n1***2***3"), 6)

    def test_multiple_delimiters(self):
        # Support for //[*][%]\n1*2%3
        self.assertEqual(add("//[*][%]\n1*2%3"), 6)

    def test_multiple_long_delimiters(self):
        # Support for //[abc][def]\n1abc2def3
        self.assertEqual(add("//[abc][def]\n1abc2def3"), 6)

if __name__ == "__main__":
    unittest.main()