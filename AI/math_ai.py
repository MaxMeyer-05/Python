import re

class MathAI:
    def solve(self, text):
        expression = re.sub(r'[^0-9+\-*/.]', '', text)
        try:
            if expression:
                result = eval(expression)
                return f"The result is {result}."
            return "I couldn't find any numbers to calculate."
        except:
            return "Sorry, but I couldn't calculate that."