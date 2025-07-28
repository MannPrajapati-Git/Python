# oops in python
# oops stands for object oriented programming



# A class is a blueprint for creating objects (instances). It defines what data (attributes) and what actions (methods) an object will have.
# An object is an instance of the class — a real entity that can access all the data and methods defined inside the class.
# simple syntax
class Student:   # class
    # Method
    def display(self,user):
        print("Hello, "+user)

# Creating object
student1 = Student()    # Object 1
student2 = Student()    # Object 2

# Calling method
student1.display("Mann")
student2.display("Heli")

print("------------------------------------------------------------------")

# Assigning Attributes Outside the Class
class Car:
    def show_details(self):
        print("Car Name:", self.name)
        print("Car Model:", self.model)

# Creating object
car1 = Car()

# Manually assigning attributes
car1.name = "Tesla"
car1.model = "Model S"

# calling method
car1.show_details()

print("------------------------------------------------------------------")


# What is self ?
# self is a reference to the current object.
# It allows each object to maintain its own data.
# It must be the first parameter in every instance method of a class (including __init__()).

class Person:
    def set_info(self, name, age):
        self.name = name      # this object's name
        self.age = age        # this object's age

    def show_info(self):
        print("Name:", self.name)
        print("Age :", self.age)

# Creating objects
p1 = Person()
p2 = Person()

# Setting data
p1.set_info("Mann", 21)
p2.set_info("Heli", 22)

# Showing data
p1.show_info()
p2.show_info()

print("------------------------------------------------------------------")

# __init__() method
# it is a Python’s constructor.
# It’s a special method in Python that is automatically called when an object is created.
# It's used to initialize (set up) the object with data.
# Think of it like a constructor in other languages (Java, C++, etc.)


class Car:
    def __init__(self):
        self.brand="Mahindra"
        self.model="Thar"
obj=Car()
print(obj.brand)
print(obj.model)

# from the above example we used init method so we dont have to write the obj.__init__().

print("-----------------------------------------------------------------")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Mahindra", "Thar")
car2 = Car("Toyota", "Fortuner")

print(car1.brand, "-", car1.model)
print(car2.brand, "-", car2.model)
