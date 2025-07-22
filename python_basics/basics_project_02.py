# Project : simple calculator

n1=int(input("enter first number : "))
n2=int(input("enter second number : "))

print("choose 1 operation from below :")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")
operation = input("enter your operation to perform from above : ")

if operation == "+":
    print("Result of addition is : ", n1 + n2)
elif operation == "-":  
    print("Result of subtraction is : ", n1 - n2)
elif operation == "*":
    print("Result of multiplication is : ", n1 * n2)
elif operation == "/":
    if n2 != 0:
        print("Result of division is : ", n1 / n2)
    else:
        print("Error: Division by zero is not allowed.")