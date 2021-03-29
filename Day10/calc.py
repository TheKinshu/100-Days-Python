import art

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operation:
        print(symbol)

    operation_symbol = input("Pick an operation from the line above: ")

    num2 = float(input("What's the second number?: "))


    calculate = operation[operation_symbol]
    firstAnswer = calculate(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {firstAnswer}")

    on_going = 'y'

    while on_going == 'y':
        operation_symbol = input("Pick another operation: ")
        num3 = int(input("What's the next number?: "))

        calculate = operation[operation_symbol]
        secondAnswer = calculate(firstAnswer, num3)

        print(f"{firstAnswer} {operation_symbol} {num3} = {secondAnswer}")

        on_going = input(f"Type 'y' tp continue calculating with {secondAnswer}, or type 'n' to exit.: ")
        
        if on_going == 'y':
            firstAnswer = secondAnswer
        else:
            calculator()



calculator()