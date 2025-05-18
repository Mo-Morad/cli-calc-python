import unittest
from calculator.evaluator_logic import evaluate_expression


class TestEvaluator(unittest.TestCase):

    def test_simple_add(self):
        self.assertEqual(evaluate_expression("2 + 3"), 5)

    def test_operator_precedence(self):
        self.assertEqual(evaluate_expression("2 + 3 * 4"), 14)

    def test_parentheses(self):
        self.assertEqual(evaluate_expression("2 * (3 + 4)"), 14)

    def test_negative_numbers(self):
        self.assertEqual(evaluate_expression("-5 + 10"), 5)

    def test_decimal_numbers(self):
        self.assertEqual(evaluate_expression("3.5 + 1.2"), 4.7)

    def test_power_operator(self):
        self.assertEqual(evaluate_expression("2 ^ 3"), 8)

    def test_logarithm(self):
    self.assertEqual(evaluate_expression("log(1000)"), 3)

