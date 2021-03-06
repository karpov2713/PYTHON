import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Тесты для 'name_function.py'"""

    def test_first_last_name(self):
        """Имена вида 'Dima Karpov' работают правильно?"""
        formatted_name = get_formatted_name('dima', 'karpov')
        self.assertEqual(formatted_name, 'Dima Karpov')

    def test_first_last_middle_name(self):
        """Работают ли такие имена, как 'Карпов Дмитрий Александрович'?"""
        formatted_name = get_formatted_name(
            'dima', 'karpov', 'alexandrovich')
        self.assertEqual(formatted_name, 'Dima Alexandrovich Karpov')


if __name__ == '__main__':
    unittest.main()
