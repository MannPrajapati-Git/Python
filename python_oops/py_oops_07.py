# static and class method in python

# static method 
# Belongs to the class, but doesn’t have access to self or cls.

# Cannot modify class or instance state.

# Used for utility/helper functions.


# example : You have a class MathTools that provides utility functions like checking if a number is even, odd, or calculating square — these don’t depend on any object or class state.

class MathTools:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @staticmethod
    def is_odd(number):
        return number % 2 != 0

    @staticmethod
    def square(number):
        return number * number

# ✅ No need to create object!
print("Is 10 even?", MathTools.is_even(10))     # Output: True
print("Is 7 odd?", MathTools.is_odd(7))         # Output: True
print("Square of 5:", MathTools.square(5))      # Output: 25

# ⚠️ But you can still call using object (not recommended)
tool = MathTools()
print(tool.is_even(100))  # Output: True



# class method
# Takes cls as the first argument (instead of self)

# Can access and modify class variables.

# Used to create factory methods or alternative constructors.

class Student:
    total_students = 0  # ✅ Class variable

    def __init__(self, name):
        self.name = name
        Student.total_students += 1

    @classmethod
    def get_total_students(cls):
        return cls.total_students

# ✅ Create students
s1 = Student("Mann")
s2 = Student("Heli")

# ✅ Call class method
print("Total Students:", Student.get_total_students())  # Output: 2


# combined example 

class Car:
    total_cars = 0

    def __init__(self, brand):
        self.brand = brand
        Car.total_cars += 1

    @staticmethod
    def is_valid_brand(brand):
        return brand in ["Toyota", "Honda", "Tesla"]

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

# ✅ Static method check
print(Car.is_valid_brand("Tesla"))   # True
print(Car.is_valid_brand("Ford"))    # False

# ✅ Create objects
c1 = Car("Tesla")
c2 = Car("Honda")

# ✅ Class method
print("Total cars created:", Car.get_total_cars())  # Output: 2
