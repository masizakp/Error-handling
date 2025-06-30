
# The calculation function performs all the calculations as per
# the user's choice and return the results
def calculateTotal(number1, number2, operation):
    """
    Performs a mathematical calculation based on two numbers and an operation.

    Args:
        number1: The first number (int or float).
        number2: The second number (int or float).
        operation: A string representing the operation to perform.
                   Valid operations are:
                   - "add" or "+" for addition
                   - "subtract" or "-" for subtraction
                   - "multiply" or "*" for multiplication
                   - "divide" or "/" for division

    Returns:
        The result of the calculation (int or float), or None if an invalid
        operation is provided or if division by zero is attempted."
    """
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    else:
        return number1 / number2


while True:
    # The menu will always appear for user to choose from
    menu = input('''Select one of the following options:
    C - Calculation
    P - Print
    : ''').lower()

    # If the user's choice is "c", the equations.txt will be opened and
    # user input will be appended and stored in the equations file as lines,
    # each user input will be separated by comma
    if menu == "c":
        try:
            value1 = float(input("Enter the first value: "))
            value2 = float(input("Enter the second value: "))
            while True:
                operations = input("Enter an operation (*,+,-,/): ")
                if operations in ("*", "+", "-", "/"):
                    result = calculateTotal(value1,value2,operations)
                    print(f"{value1} {operations} {value2} = {result}")
                    with open(
                    "equations.txt", "a", encoding='utf-8') as file:
                        file.write(
                        f"\n{value1},{operations},{value2} = {result}"
                        )
                    print("Equation successfully stored.")
                    break
                else:
                    print("operation does not exist")
                    continue
        except FileNotFoundError:
            print("equations.txt file not found.")
            break
        except ValueError:
            print("Please enter a valid number.")
            continue
        except ZeroDivisionError:
            print("You cannot divide by zero. Please try again!")
            continue

    # If the user's choice is "p", the equations.txt will be opened
    # and read as lines and the equations from the file will be displayed
    elif menu == "p":
        try:
            with open(
            "equations.txt", "r", encoding='utf-8') as file:
                lines = file.readlines()
            for line in lines:
                parts = line.strip().split(",")
                print(parts[0],parts[1],parts[2])
            break
        except FileNotFoundError:
            print("equations.txt file not found.")
