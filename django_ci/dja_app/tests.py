from django.test import TestCase
from .utils import add_numbers

class CalculationTest(TestCase):

    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 6)

    def test_add_negative_numbers(self):
        result = add_numbers(-1, -4)
        self.assertEqual(result, -5)

