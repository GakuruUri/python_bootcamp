# Calc
#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# func = operations["*"]
# func(3, 4)

num1 = int(input("What's the first number?: "))
# num2 = int(input("What's the second number?: "))

for symbol in operations:
    print(symbol)
    
    
operation_symbol = input("Pick a symbol from the line above: ")

num2 = int(input("What's the second number?: "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)


#print(f"{num1} {operation_symbol} {num2} = {calculation_function(num1, num2)}")
print(f"{num1} {operation_symbol} {num2} = {answer}")


