# What is an Exception?
# An exception is a Python object that represents an error.
# It occurs during program execution (run-time) and disrupts the normal flow.

# Types of Errors:
# Syntax Error – Occurs due to invalid code (caught by the interpreter before running).
# Runtime Error (Exception) – Occurs during program execution (like divide by zero, file not found).

# basic example
try:
    print(10 / 0)
except:
    print("Something went wrong")

print("--------------------------------------------------------------------------------------")

# Catching Specific Exceptions
# Always prefer specific exceptions over general ones.

try:
    x = int(input("Enter a number: "))
except ValueError:
    print("You entered an invalid number!")

print("--------------------------------------------------------------------------------------")

# Multiple except Blocks
try:
    a = int(input("Enter a number: "))
    b = 10 / a
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("--------------------------------------------------------------------------------------")

# Handling Multiple Exceptions in One Block
try:
    name = int("Mann")  # Will raise ValueError
except (ValueError, TypeError) as e:
    print("Caught exception:", e)

print("--------------------------------------------------------------------------------------")
# The else Clause/Block
# Runs only if no exception occurs.
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("You entered:", x)

print("--------------------------------------------------------------------------------------")

# The finally Clause/Block
# Runs no matter what (useful for cleanup operations like closing files).
try:
    f = open("demo.txt", "r")
    data = f.read()
    print(data)
except FileNotFoundError:
    print("File not found!")
finally:
    print("Closing file...")
    try:
        f.close()
    except:
        pass

print("--------------------------------------------------------------------------------------")

# Nested try-except
try:
    a = int(input("Enter a number: "))
    try:
        b = 10 / a
        print("Result:", b)
    except ZeroDivisionError:
        print("Inner error: Cannot divide by zero")
except ValueError:
    print("Outer error: Invalid number input")

print("--------------------------------------------------------------------------------------")

# Raising Exceptions Manually using raise
# age = -5

# if age < 0:
#     raise ValueError("Age cannot be negative")

# after the above code no any below code will execute so we have to wrap it in try-except so below codes can execute
# the wrapped version of above code 
# Raising Exceptions Manually using raise
try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print("Manually raised error:", e)

print("--------------------------------------------------------------------------------------")

# Using assert for Debugging
# x = 5
# assert x > 0  # Passes
# assert x < 0, "x must be negative!"  # Raises AssertionError

# after the above code no any below code will execute so we have to wrap it in try-except so below codes can execute
# the wrapped version of above code 

# Using assert for Debugging
x = 5
try:
    assert x < 0, "x must be negative!"
except AssertionError as e:
    print("Assertion failed:", e)

print("--------------------------------------------------------------------------------------")

# Custom Exceptions
# You can define your own exception types by subclassing Exception.
class TooYoungError(Exception):
    pass

try:
    age = 12
    if age < 18:
        raise TooYoungError("You must be at least 18 years old to register.")
except TooYoungError as e:
    print("Custom Exception Caught:", e)

print("--------------------------------------------------------------------------------------")

# Accessing the Exception Object (using as e)
try:
    result = 1 / 0
except ZeroDivisionError as e:
    print("Error occurred:", e)

print("--------------------------------------------------------------------------------------")

# Bonus: Full Example Covering All Concepts
class AgeError(Exception):
    pass

def validate_user(age):
    if age < 0:
        raise ValueError("Age can't be negative!")
    elif age < 18:
        raise AgeError("You must be at least 18.")
    else:
        print("Welcome!")

try:
    age = int(input("Enter your age: "))
    validate_user(age)
except ValueError as ve:
    print("Value Error:", ve)
except AgeError as ae:
    print("Custom Age Error:", ae)
else:
    print("No exceptions, all good!")
finally:
    print("Process complete.")
