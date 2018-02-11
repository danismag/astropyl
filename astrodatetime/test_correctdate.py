import unittest
from astrodatetime.correctdate import *


class TestJulianDate(unittest.TestCase):

    def test_negative_month(self):
        self.assertRaises(ValueError, correctdate, 17.25, -2, 1985)

    def test_fractional_year(self):
        self.assertRaises(ValueError, correctdate, 17, 2, 1985.12)

    def test_more_month(self):
        self.assertRaises(ValueError, correctdate, 32, 2, 1985)

    def test_negative_days(self):
        self.assertRaises(ValueError, correctdate, -1, 2, 1985)