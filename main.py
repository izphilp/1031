"""Import calculator file with function"""
import calculator

print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")

"""Validiate first number"""

while True:

    first_input = input("Enter in first number: ")
    second_input = input("Enter second number: ")
    operation = input("Would you like to add/subtract/multiply/divide: ")
    list_operation = ["add", "substract", "multiply", "divide"]
    if first_input.isnumeric() and second_input.isnumeric() and operation.lower() in list_operation:
        first_number = float(first_input)
        second_number = float(second_input)
        calculator.calculator(first_number, second_number, operation)
        break
    
    else:
        print("Invalid Input!")
        continue