"""Math functions for calculator."""
from arithmetic import *

#working copy, do not mess up!!
# def separate_user_input(s):
#     separated = expression.split()
#     operation = separated[0]

#     if len(separated)==1:
#         return [operation, 0, 0]
#     elif len(separated)==2:
#         try:
#             num1 = int(separated[1])
#             return [operation, num1, 0]
#         except ValueError:
#             return ['notNum', 0 ,0]
#     elif len(separated)==3:
#         try:
#             num1 = int(separated[1])
#             num2 = int(separated[2])
#             return [operation, num1, num2]
#         except ValueError:
#             return ['notNum', 0 ,0]
#     else:
#         print("Invalid number of arguments.")

def separate_user_input(s):
    separated = expression.split()
    operation = separated[0]

    if len(separated)==1:
        return [operation, 0, 0]
    elif len(separated)==2:
        num1 = int(separated[1])
        return [operation, num1, 0]
    elif len(separated)==3:
        num1 = int(separated[1])
        num2 = int(separated[2])
        return [operation, num1, num2]
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
    try:
        operation, num1, num2 = separate_user_input(expression)
        valid_ops = ['q', '+', '-', '*', '/', 'square', 'cube', 'pow', 'mod']
        if operation in valid_ops:
            if operation == 'q':
                break
            else:
                answer = evaluate(operation, num1, num2)
                print(answer)
        else:
            print("Not a valid operation")
    except:
        print("You fool!  You need to input valid numbers!")

# while loop function

#try separate user input

#except 
