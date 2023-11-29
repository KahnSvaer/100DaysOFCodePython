from art import logo


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide
              }

Head_logo = logo



def calculator():
    print(Head_logo)
    num1 = float(input("What's the first number? "))
    for sign in operations:
        print(sign)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation?: ")
        num2 = float(input("What's the next number? "))
        function = operations[operation_symbol]
        answer = function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        num1 = answer

        to_continue = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n to start a new calculation: ").strip().lower()
        if to_continue == 'n':
            should_continue = False
            calculator()