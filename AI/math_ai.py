import re

class MathAI:
    """
    A simple AI that extracts mathematical expressions from natural language
    and evaluates them.
    """
    def __init__(self):
        # Mapping English words to mathematical operators
        self.word_to_operator = {
            "plus": "+",
            "minus": "-",
            "times": "*",
            "divided": "/"
        }

    def solve(self, text):
        """
        Translates words to symbols, extracts the expression and calculates it.
        Args:
            text (str): The input string containing the math problem in natural language.
        Returns:
            str: The result of the calculation or an error message.
        """
        # 1. Standardize text
        expr = text.lower().strip()

        # 2. Replace words with math-readable characters
        for word, replacement in self.word_to_operator.items():
            expr = expr.replace(word, replacement)

        # 3. Filter: Keep only numbers, operators, dots, and parentheses
        expr = re.sub(r'[^0-9+\-*/.()]', '', expr)

        try:
            if expr:
                # Calculate the result
                result = eval(expr)
                
                # Format: remove .0 if it's an integer
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                
                return f"The result is {result}."
            return "I couldn't find any numbers or operators to calculate."
        except ZeroDivisionError:
            return "I can't divide by zero. That's illegal!"
        except Exception:
            return "I found the numbers, but the math is too confusing for me."