# 2. Write a program using match case that simulates a simple calculator.
#     1. Ask the user for two numbers and an operation (+, -, *, /).
#     2. Perform the operation using match case .
a = int(input("Enter number 1: "))
b=  int(input("Enter number 2: "))
c= input("Enter operation: ")
match c:
    case "addition" :
        print(a+b)
    case "subtraction":
        print(a-b)
    case "multiplication":
        print(a*b)
    case "division":
        print(a/b)
    case _:
        print("invalid operation")