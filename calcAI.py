import re

def plus_ai(text):
    numbers = re.findall(r'\d+', text)
    if "plus" in text or "+" in text:
        result = int(numbers[0]) + int(numbers[1])
        return f"The sum is {result}"
    return "No calculation performed"

def minus_ai(text):
    numbers = re.findall(r'\d+', text)
    if "minus" in text or "-" in text:
        result = int(numbers[0]) - int(numbers[1])
        return f"The difference is {result}"
    return "No calculation performed"

def calc_ai(text):
    text = text.lower()
    if "plus" in text or "+" in text:
        return plus_ai(text)
    elif "minus" in text or "-" in text:
        return minus_ai(text)
    else:
        return "No calculation performed"

print(calc_ai("What is 5 plus 3?"))
print(calc_ai("Calculate 12 Plus 7"))
print(calc_ai("What is 10 minus 4?"))
print(calc_ai("What is 7 Minus 2???"))

text = input("\n\nEnter your calculation: ")
print(calc_ai(text))