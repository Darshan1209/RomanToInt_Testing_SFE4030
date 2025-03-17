import unittest
from RomanToInt import Solution

class TestRomanToInt(unittest.TestCase):
    
    def test_single_digit(self):
        self.assertEqual(Solution.romanToInt("I"), 1)
        self.assertEqual(Solution.romanToInt("V"), 5)
        self.assertEqual(Solution.romanToInt("X"), 10)
        self.assertEqual(Solution.romanToInt("L"), 50)
        self.assertEqual(Solution.romanToInt("C"), 100)
        self.assertEqual(Solution.romanToInt("D"), 500)
        self.assertEqual(Solution.romanToInt("M"), 1000)
    
    def test_multiple_digits(self):
        self.assertEqual(Solution.romanToInt("II"), 2)
        self.assertEqual(Solution.romanToInt("IV"), 4)
        self.assertEqual(Solution.romanToInt("IX"), 9)
        self.assertEqual(Solution.romanToInt("XL"), 40)
        self.assertEqual(Solution.romanToInt("XC"), 90)
        self.assertEqual(Solution.romanToInt("CD"), 400)
        self.assertEqual(Solution.romanToInt("CM"), 900)

    def test_subtractive_notation(self):
        self.assertEqual(Solution.romanToInt("XLII"), 42)
        self.assertEqual(Solution.romanToInt("XCIX"), 99)
        self.assertEqual(Solution.romanToInt("CDXLIV"), 444)
        self.assertEqual(Solution.romanToInt("CMXCIX"), 999)

    def test_with_and_without_subtractive_notation(self):
        self.assertEqual(Solution.romanToInt("XIV"), 14)
        with self.assertRaises(ValueError):
            Solution.romanToInt("XIIII")
        self.assertEqual(Solution.romanToInt("LIX"), 59)
        with self.assertRaises(ValueError):
            Solution.romanToInt("LVIIII")

    def test_repetition(self):
        self.assertEqual(Solution.romanToInt("III"), 3)
        self.assertEqual(Solution.romanToInt("XXX"), 30)
        self.assertEqual(Solution.romanToInt("CCC"), 300)
        self.assertEqual(Solution.romanToInt("MMM"), 3000)

    def test_first_number(self):
        self.assertEqual(Solution.romanToInt("I"), 1)

    def test_invalid_letter(self):
        with self.assertRaises(TypeError):
            Solution.romanToInt("A")

    def test_invalid_and_valid_letter(self):
        with self.assertRaises(TypeError):
            Solution.romanToInt("IXA")

    def test_not_valid(self):
        with self.assertRaises(ValueError):
            Solution.romanToInt("VV")

    def test_null(self):
        self.assertEqual(Solution.romanToInt(""), 0)

if __name__ == '__main__':
    unittest.main()