import unittest


class Calculator:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def subtract(self):
        return self.first - self.second


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator(10, 5)
        print('setUp method')

    def tearDown(self):
        print('tearDown method')

    def test_add(self):
        self.assertEqual(self.calc.add(), 15)
        self.calc.first = 15
        self.assertEqual(self.calc.add(), 20)
        print('Test_add')

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(), 5)
        self.calc.first = 15
        self.assertEqual(self.calc.subtract(), 10)
        print('Test_subtract')
