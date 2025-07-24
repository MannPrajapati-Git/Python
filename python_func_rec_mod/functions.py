# functions in python
# A function is a reusable block of code that performs a specific task.
# It helps you:

# Break code into smaller, manageable chunks

# Avoid repetition (DRY principle)

# Improve readability and debugging


# Types of Functions
# Built-in Functions – e.g. print(), len(), type(), etc.

# User-defined Functions – You define these using def



# syntax 

# function without parameters and return keyword
def greet():
    print("hello, i am your coding mentor")
greet() 

# function with parameters and without return keyword
def greet(name):
    print("hello my name is "+name)
greet("MANN")

# function with return and parameters
# when you use return, the print statement is required to print the function
def add(a,b):
    return a+b
result=add(10,20)
print("the addition :",result)

# function with return without parameters

def add():
    a=20
    b=20
    return a+b
print("the addition :",add())   

# function returning multiple values 

def add(a,b):
    return a+b , a-b
addition,subtraction=add(10,20)
print("the addition is :",addition)
print("the subtraction is :",subtraction)   


# lambda function

cube = lambda x:x**3
print(cube(3))


# function arguments 
# Types:
# Positional Arguments
# Keyword Arguments
# Default Arguments
# Variable-length Arguments: *args and **kwargs


# function with positional arguments
# in this values are passed in order to parameters

def student(name,age):
    print(f"Name: {name} , Age: {age}")
student("Mann",21)

# function with keyword arguments 
# you have to specify the paramater name while passing the value

def student(name,age):
    print(f"Name: {name}")
    print(f"Age: {age}")
student(name="Mann", age=21)

# function with default arguments

def greet(name="Sir"):
    return "hello," + name + "!"

print(greet("Mann"))
print(greet())



# function with *args (Variable-length Arguments)
# You can pass any number of values. Inside function
# for tuple like
def add(*args):

    return sum(args)

print(add(1,2,3))
print(add(1,2,3,4,5))

def total_marks(*marks):
    print("Marks:", marks)
    print("Total:", sum(marks))

total_marks(70, 85, 90)


# function with **kwargs (multiple keyword Arguments)
# for dictunary like
def movie(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
movie(name="shaktiman")
movie(name="shaktiman", power="laser")
movie(name="shaktiman", power="laser", enemy="dr")
print("\n")
def student_profile(**details):
    print("Profile:")
    for key, value in details.items():
        print(f"{key}: {value}")

student_profile(name="Mann", age=21, branch="CSE")

# combining all the argument types example 

def demo(a, b=2, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 3, 4, 5, x=10, y=20)


# variable scope in function
# scope : Where a variable is accessible (visible) in your code.
# global variable and local variable 

# Local Variable
# Variable defined inside a function — only accessible within that function.

def greet():
    message = "Hello, Mann!"  # local variable
    print(message)

greet()
# print(message)  # if you use this message variable outside the function it will raise the error

# global variable
# Variable defined outside all functions — accessible everywhere in the file.


greeting = "Welcome!"  # global variable
def greet():
    print(greeting + " Mann")

greet()  
print(greeting + " Mann")  


# global keyword
# when you want to modify the global variable value you have to use global keyword
count=0
def modify():
    global count  # if you comment this statement and run the program it will raise the error
    count += 1
modify()
print(count)


# Variable Shadowing
# When a local variable has the same name as a global variable, it shadows (hides) the global one inside that function.
# What Does "Shadowing" Mean?
# When you declare a local variable inside a function with the same name as a global variable,
# then the local variable hides (shadows) the global one within that function.

# there is no global keyword require to override/shadowing

name = "Mann"  # global
def show():
    name = "Heli"  # local (shadows global)
    print("Inside:", name)

show()           # Inside: Heli
print("Outside:", name)  # Outside: Mann



# yield in python function
# yield is used in a function to turn it into a generator — a special type of function that remembers its state and can pause and resume.

def even_generator(last):
    for i in range(2, last+1, 2):
        yield i
for num in even_generator(10):
    print(num)


# Built-in Functions?
# Built-in functions are pre-defined in Python — you can use them anywhere, anytime without writing your own logic.

# Print Output
print(" Hello, Mann!")

#  Length
name = "Prajapati"
print("Length of name:", len(name))

#  Type Check
num = 3.14
print("Type of num:", type(num))

#  Type Conversion
int_val = int("10")
str_val = str(123)
print("int('10'):", int_val)
print("str(123):", str_val)

#  User Input (commented for auto-run)
# user_input = input("Enter something: ")
# print("You entered:", user_input)

#  max(), min(), sum()
numbers = [4, 2, 9, 5]
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))

#  sorted()
unsorted = [3, 1, 4, 2]
print("Sorted list:", sorted(unsorted))

#  range()
print("Numbers from 1 to 4:")
for i in range(1, 5):
    print(i, end=' ')
print()

#  abs(), round()
print("Absolute of -10:", abs(-10))
print("Round of 3.1415:", round(3.1415, 2))

#  enumerate()
items = ["apple", "banana", "mango"]
print("Enumerate list:")
for index, value in enumerate(items):
    print(f"{index} → {value}")

#  zip()
names = ["Mann", "Rahul"]
scores = [85, 92]
print("Zipped list:")
for name, score in zip(names, scores):
    print(f"{name}: {score}")

#  reversed()
rev = list(reversed("MANN"))
print("Reversed:", rev)

#  eval() - ⚠️ Use with caution
expression = "2 + 3 * 4"
result = eval(expression)
print("Result of eval('2 + 3 * 4'):", result)


# functional programming tools 
# map()
# Applies a function to each item of iterable (like list).
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, numbers))
print("Squares:", squares)

# filter()
# Keeps only items where the function returns True
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", evens)

# reduce()
# Reduces list to a single value by applying function cumulatively.
# you have to import reduce from the functools 
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print("Product:", product)


