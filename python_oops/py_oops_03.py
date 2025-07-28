# inheritence in python
# Inheritance allows a child class (subclass) to inherit methods and properties from a parent class (superclass). It supports code reuse and hierarchy.

#  Single Inheritance

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()   # Inherited
d.bark()    # Own method

print("---------------------------------------------------------------")
# Multilevel Inheritance

class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")

p = Puppy()
p.eat()    # From Animal
p.bark()   # From Dog
p.weep()   # Own method

print("---------------------------------------------------------------")

# Hierarchical Inheritance

class Animal:
    def move(self):
        print("Animal moves")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
c = Cat()
d.move()
d.bark()
c.move()
c.meow()

print("---------------------------------------------------------------")
# Multiple Inheritance

class Father:
    def skills(self):
        print("Gardening, Programming")

class Mother:
    def skills(self):
        print("Cooking, Painting")

class Child(Father, Mother):  # Inherits from both
    def skills(self):
        print("Child's skills:")
        Father.skills(self)
        Mother.skills(self)

c = Child()
c.skills()

print("---------------------------------------------------------------")
# Hybrid Inheritance

# Base class
class Person:
    def show(self):
        print("Person: I am a human.")

# Inheriting Person
class Student(Person):
    def study(self):
        print("Student: I study hard.")

# Another class inheriting Person
class Athlete(Person):
    def train(self):
        print("Athlete: I train daily.")

# Hybrid: Inheriting both Student and Athlete
class ScholarAthlete(Student, Athlete):
    def manage(self):
        print("ScholarAthlete: I balance study and sports.")

# Creating object
sa = ScholarAthlete()
sa.show()     # From Person
sa.study()    # From Student
sa.train()    # From Athlete
sa.manage()   # Own method

print("---------------------------------------------------------------")
# super()
# The super() function in Python is used to call methods (like __init__ or others) from the parent class inside the child class.

# It is especially useful when we are dealing with inheritance, and we want to reuse the parent class methods without explicitly naming the parent class.

# example 1
class Animal:
    def __init__(self):
        print("Animal created")

class Dog(Animal):
    def __init__(self):
        super().__init__()   # calling parent class constructor
        print("Dog created")

d = Dog()

print("---------------------------------------------------------------")
# example 2
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()    # call parent method
        print("Hello from Child")

c = Child()
c.greet()
