def calculator(first_number, second_number, operation):
    """ Use selected operation"""

    if operation == "add":
        result = first_number + second_number
        print(f"Result: {result}")
    elif operation == "subtract":
        result = first_number - second_number
        print(f"Result: {result}")
    elif operation == "multiply":
        result = first_number * second_number
        print(f"Result: {result}")
    elif operation == "divide":
        result = first_number / second_number
        print(f"Result: {result}")