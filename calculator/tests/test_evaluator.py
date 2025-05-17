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
        
    def test_division(self):
        self.assertEqual(evaluate_expression("10 / 2"), 5)

    def test_zero_division(self):
        self.assertEqual(evaluate_expression("5 / 0"), "Error")

    def test_power_operator(self):
        self.assertEqual(evaluate_expression("2 ^ 3"), 8)

