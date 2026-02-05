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

for operator in operations:
    print(operator)

operation_symbol = input("Pick an operation symbol from the line above: ")

num2 = int(input("What's the second number?: "))

calculation_function = operations[operation_symbol]
answer_1 = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer_1}")

continue_calculation = False
while not continue_calculation:
    check_continuation = input(f"Type 'y' to contine calculating with 8 or type 'n' to close")
    for operator in operations:
        print(operator)
    if check_continuation == "y":
        operation_symbol = input("Pick an operation symbol from the line above: ")

        num_n = int(input("What the next number?: "))

        calculation_function = operations[operation_symbol]
        answer_2 = calculation_function(calculation_function(num1, num2), num2)

        print(f"{answer_1} {operation_symbol} {num_n} = {answer_2}")
