import re

class MathAI:
    def solve(self, text):
        # Extrahiert nur Zahlen und mathematische Symbole
        # Beispiel: "Was ist 10 + 5?" -> "10+5"
        expression = re.sub(r'[^0-9+\-*/.]', '', text)
        try:
            if expression:
                result = eval(expression)
                return f"The result is {result}."
            return "I couldn't find any numbers to calculate."
        except:
            return "Sorry, but I couldn't calculate that."