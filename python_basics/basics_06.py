# conditional/control flow statements in Python 

# if statement
a = 10
if a > 5:
    print("a is greater than 5")


# if-else statement
b = 3
if b > 5:
    print("b is greater than 5")
else:
    print("b is not greater than 5")

# if-elif-else statement
c=15
if c > 5:
    print("c is greater than 5")
elif c < 5:
    print("c is less than 5")
else:
    print("c is equal to 5")

# nested if statement
d = 15
if d > 10:
    print("d is greater than 10")
    if d > 20:
        print("d is also greater than 20")
    else:
        print("d is not greater than 20")