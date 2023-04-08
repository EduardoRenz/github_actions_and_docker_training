import unittest
from app import currency_format

class TestStringMethods(unittest.TestCase):

    def test_should_correct_format(self):
        self.assertEqual(currency_format('10'), 'R$ 10,00')
        self.assertEqual(currency_format('10.45'), 'R$ 10,45')
        self.assertEqual(currency_format('10,45'), 'R$ 10,45')

if __name__ == '__main__':
    unittest.main()