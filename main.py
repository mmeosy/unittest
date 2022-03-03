import datetime
import unittest
from agecalculation import calculate_age

class testagecalculation(unittest.TestCase)

    def test_calculated_age_day_before_today(self)
        birthday = datetime.datetime.strptime("22.05.2000", "%d.%m.%Y")
        result = calculate_age(birthday)
        self.assertEqual(result, 22)




    def test_calculated_age_day_after_today(self)
        birthday = datetime.datetime.strptime("22.05.2000", "%d.%m.%Y")
        result = calculate_age(birthday)
        self.assertEqual(result, 21)

if __name__ == '__main__':
    unittest.main