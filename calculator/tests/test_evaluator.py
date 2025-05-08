import unittest
from calculator.evaluator import evaluate_expression

class TestEvaluator(unittest.TestCase):
    def test_simple_add(self):
        self.assertEqual(float(evaluate_expression("2 + 3")), 5.0)

    def test_operator_precedence(self):
        self.assertEqual(float(evaluate_expression("2 + 3 * 4")), 14.0)

    def test_parentheses(self):
        self.assertEqual(float(evaluate_expression("2 * (3 + 4)")), 14.0)

    def test_negative_numbers(self):
        self.assertEqual(float(evaluate_expression("-5 + 10")), 5.0)

if __name__ == '__main__':
    unittest.main()
