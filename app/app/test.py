from django.test import SimpleTestCase


class TestExample(SimpleTestCase):

    def test_addition(self):
        result = 10 + 20
        self.assertEqual(result, 30)

    def test_string(self):
        name = "Django"
        self.assertEqual(name, "Django")