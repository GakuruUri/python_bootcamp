# Calculator code reuse 2

# Add
def add(n1, n2):
  return n1 + n2


# Subtract
def subtract(n1, n2):
  return n1 - n2


# Multiply
def multiply(n1, n2):
  return n1 * n2


# Division
def divide(n1, n2):
  return n1 / n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
             }

# func = operations["*"]
# func(3, 4)


num1 = int(input("What's the first number?: "))


for symbol in operations:
    print(symbol)
    
should_continue = True

while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = int(input("What's the second number? "))
    
    print(f"{num1} {operation_symbol} = {answer}")
    
    if input(f"Type 'y' to continue with {answer}, or type 'n' to exit: ") == "y":
        num1 = answer
    else:
        should_continue = False