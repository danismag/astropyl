import unittest
from astrodatetime.juliandate import juliandate as jd


class TestJulianDate(unittest.TestCase):

    def test_result(self):
        self.assertAlmostEqual(jd(1985, 2, 17.25), 2446113.75)
        self.assertAlmostEqual(jd(1980, 1, 0.0), 2444238.5)
        self.assertAlmostEqual(jd(1979, 12, 31.0), jd(1980, 1, 0.0))
        self.assertAlmostEqual(jd(1858, 11, 17.0), 2400000.5)
        self.assertAlmostEqual(jd(-4713, 1, 1.5), 0.0)
        self.assertAlmostEqual(jd(1582, 10, 5), jd(1582, 10, 15))

    def test_value_in_range(self):
        self.assertRaises(ValueError, jd, 1985, -2, 17.25)
        self.assertRaises(ValueError, jd, 1985.12, 2, 17)
        self.assertRaises(ValueError, jd, 1985, 2, 32)
        self.assertRaises(ValueError, jd, 1985, 2, -1)


if __name__ == '__main__':
    unittest.main()
