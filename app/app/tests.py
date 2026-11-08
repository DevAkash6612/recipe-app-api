from django.test import SimpleTestCase
from app.calc import add, subtract


class TestCalc(SimpleTestCase):
    def test_add_numbers(self):
        result = add(5, 10)
        self.assertEqual(result, 15)

    def test_add_negative_numbers(self):
        result = add(-5, -10)
        self.assertEqual(result, -15)

    def test_add_zero(self):
        result = add(0, 0)
        self.assertEqual(result, 0)

    def test_subtract_numbers(self):
        result = subtract(10, 5)
        self.assertEqual(result, 5)

    def test_subtract_negative_numbers(self):
        result = subtract(-10, -5)
        self.assertEqual(result, -5)
