# calculator


def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2 

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number?: "))



continue_calculation = True
while not continue_calculation:
    operation_symbol = input("Pick an operation symbol from the line above: ")

    num2 = int(input("What's the next number?: "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to contine calculating with {answer}, or type 'n' to exit: ") == "y":
        num1 = answer
    else:
        continue_calculation = False
