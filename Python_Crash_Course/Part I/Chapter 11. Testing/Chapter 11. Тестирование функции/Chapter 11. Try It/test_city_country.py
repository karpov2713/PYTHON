import unittest
from city_function import get_city_country_names


class NamesTestCase(unittest.TestCase):
    """Тест для 'get_city_country_names"""

    def test_city_country_names(self):
        full_city_country_name = get_city_country_names('moscow', 'russia')
        self.assertEqual(full_city_country_name, 'Moscow, Russia')


if __name__ == '__main__':
    unittest.main()
