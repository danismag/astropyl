import unittest
from astrodatetime.juliandate import *


class TestJulianDate(unittest.TestCase):

    def test_result(self):
        self.assertAlmostEqual(juliandate(1985, 2, 17.25), 2446113.75)
        self.assertAlmostEqual(juliandate(1980, 1, 0.0), 2444238.5)
        self.assertAlmostEqual(juliandate(1979, 12, 31.0), 2444238.5)
        self.assertAlmostEqual(juliandate(1858, 11, 17.0), 2400000.5)


if __name__ == '__main__':
    unittest.main()
