# calculator/evaluator.py

import math

def evaluate_expression(expression):
    expression = expression.replace("^", "**")
    expression = expression.replace("√", "math.sqrt")
    expression = expression.replace("log", "math.log10")
    expression = expression.replace("ln", "math.log")
    expression = expression.replace("e^", "math.exp")
    expression = expression.replace("π", str(math.pi))
    expression = expression.replace("e", str(math.e))

    try:
        result = eval(expression)
        return result
    except Exception:
        return "Error"
