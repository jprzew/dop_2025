import sys
import unittest
from calculator import add, product, divide

# assertEqual, assertNotEqual
# assertTrue, assertFalse
# assertIs, assertIsNot
# assertIsNone, assertIsNotNone
# assertIn, asertNotIn
# assertRaises
# assertGreater, assertLess, assertLessEqual, assertGreaterEqual

class TestAddition(unittest.TestCase):
    def test_add_two_positive_numbers(self):
        cases = [((2, 3), 5),
                 ((1, 7), 8),
                 ((3, 6), 9),
                 ((1, 1), 2)]

        for args, result in cases:
            with self.subTest(x=args):
                self.assertEqual(add(*args), result)

    def test_two_negative_numbers(self):
        self.assertEqual(add(-4, -5), -9)

class TestProduct(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        self.assertEqual(product(3, 4), 12)
        self.assertGreater(product(2, 3), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(product(-3, -4), 12)
        self.assertGreater(product(-2, -3), 0)

    def test_mutiply_different_signs(self):
        self.assertEqual(product(-3, 5), -15)
        self.assertLess(product(-3, 5), 0)\


class TestDivision(unittest.TestCase):

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(1, 4), 0.25)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide(4, 0)

# @unittest.skip
# @unittest.skipIf
# @unittest.skipUnless

class SkipTestExample(unittest.TestCase):

    @unittest.skip('This test is not important')
    def test_unimportant(self):
        self.fail('This test should be skipped')

    @unittest.skipIf(sys.version_info < (3, 12), 'Requires Python >= 3.12.')
    def test_using_calendar_constants(self):
        import calendar

        self.assertEqual(calendar.Month(10), calendar.OCTOBER)


if __name__ == '__main__':
    unittest.main(verbosity=2)

