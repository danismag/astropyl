import unittest
from astrodatetime.datefromjulian import datefromjulian as jd2date


class TestJulianDate(unittest.TestCase):

    def test_result_type(self):
        self.assertIsInstance(jd2date(0), dict, 'Функция должна возвращать словарь')

    def test_result_value(self):
        self.assertEqual(jd2date(2446113.75), {"year": 1985, "month": 2, "day": 17.25})
        self.assertEqual(jd2date(2444238.5), {"year": 1979, "month": 12, "day": 31.0})
        self.assertEqual(jd2date(2400000.5), {"year": 1858, "month": 11, "day": 17.0})
        self.assertEqual(jd2date(0.0), {"year": -4713, "month": 1, "day": 1.5})
        self.assertEqual(jd2date(1721423.5), {"year": 1, "month": 1, "day": 1.0})
        self.assertEqual(jd2date(1721422.5), {"year": -1, "month": 12, "day": 31.0})
        self.assertEqual(jd2date(2299159.5), {"year": 1582, "month": 10, "day": 4.0})
        self.assertEqual(jd2date(2299160.5), {"year": 1582, "month": 10, "day": 15.0})

    def test_value_in_range(self):
        self.assertRaises(ValueError, jd2date, -2)
        self.assertRaises(TypeError, jd2date, '23')
