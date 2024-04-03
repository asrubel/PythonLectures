import unittest


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / b


class TestCalculator(unittest.TestCase):

    def test_general(self):
        self.assertEqual(add(2, 5), 7, "Wrong answer")
        self.assertEqual(multiply(2, 5), 10, "Wrong answer")
        self.assertEqual(subtract(2, 5), -3, "Wrong answer")
        self.assertEqual(divide(2, 5), 0.4, "Wrong answer")

    def test_add(self):
        self.assertEqual(add(2, 5), 7, "Wrong answer")
        self.assertEqual(add(7, 5), 12, "Wrong answer")
        self.assertEqual(add(5, 5), 10, "Wrong answer")
        self.assertEqual(add(1, 5), 6, "Wrong answer")
