# Simple functions calculator
# Adding 2 numbers
def add(n1, n2):
    return n1 + n2

# Subtracting
def subtract(n1, n2):
    return n1 - n2
# Multiplying 2 numbers
def multiply(n1, n2):
    return n1 * n2

# Division
def divide(n1, n2):
    return n1 / n2

def calculator(n1, n2, func):
    return func(n1, n2)


result = calculator(2, 3, subtract)
print(result)
