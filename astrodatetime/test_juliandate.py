import unittest
from astrodatetime.juliandate import juliandate as jd


class TestJulianDate(unittest.TestCase):

    def test_result(self):
        self.assertAlmostEqual(jd(17.25, 2, 1985), 2446113.75)
        self.assertAlmostEqual(jd(0.0, 1, 1980), 2444238.5)
        self.assertAlmostEqual(jd(31.0, 12, 1979), jd(0.0, 1, 1980))
        self.assertAlmostEqual(jd(17.0, 11, 1858), 2400000.5)
        self.assertAlmostEqual(jd(1.5, 1, -4713), 0.0)
        self.assertAlmostEqual(jd(5, 10, 1582), jd(15, 10, 1582))

    def test_value_in_range(self):
        self.assertRaises(ValueError, jd, 17.25, -2, 1985)
        self.assertRaises(ValueError, jd, 17, 2, 1985.12)
        self.assertRaises(ValueError, jd, 32, 2, 1985)
        self.assertRaises(ValueError, jd, -1, 2, 1985)


if __name__ == '__main__':
    unittest.main()
