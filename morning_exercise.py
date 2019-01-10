"""Math functions for calculator."""
from arithmetic import *


def separate_user_input(s):
    separated = expression.split()
    operation = expression.split()[0]

    if len(separated)==1:
        return [operation, 0, 0]
    elif len(separated)==2:
        try:
            num1 = int(separated[1])
            return [operation, num1, 0]
        except ValueError:
            return ['notNum', 0 ,0]
    elif len(separated)==3:
        try:
            num1 = int(separated[1])
            num2 = int(separated[2])
            return [operation, num1, num2]
        except ValueError:
            return ['notNum', 0 ,0]
    else:
        print("Invalid number of arguments.")
        

def evaluate(operation, num1, num2):
    if operation =='+':
        answer = add(num1, num2)
    elif operation == '-':
        answer = subtract(num1, num2)
    elif operation == '*':
        answer = multiply(num1, num2)
    elif operation == '/':
        answer = divide(num1, num2)
    elif operation == 'square':
        answer = square(num1)
    elif operation == 'cube':
        answer = cube(num1)
    elif operation == 'pow':
        answer = power(num1, num2)
    elif operation == 'mod':
        answer = mod(num1, num2)

    return answer


while True:
    expression = input(">")
    
    operation, num1, num2 = separate_user_input(expression)
    valid_ops = ['q', '+', '-', '*', '/', 'square', 'cube', 'pow', 'mod', 'notNum']

    #check for valid operation
    if operation in valid_ops:
        if operation == 'q':
            break
        elif operation == 'notNum':
            print("Must enter valid numbers")
        else:
            answer = evaluate(operation, num1, num2)
            print(answer)

    else:
        print ("Not a valid operation")


