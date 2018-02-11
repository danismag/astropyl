import unittest
from astrodatetime.dayoftheweek import dayoftheweek as dow


class TestJulianDate(unittest.TestCase):

    def test_result_type(self):
        self.assertIsInstance(dow(1,1,1), list, 'Функция должна возвращать список')