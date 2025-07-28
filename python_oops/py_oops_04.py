# Polymorphism in Python
# Polymorphism means same function name can be used for different types or behaviors.

class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

def call_sound(animal):
    animal.sound()

call_sound(Dog())  # Dog barks
call_sound(Cat())  # Cat meows

print("--------------------------------------------------------------------------")

# Method Overriding in Python

# When a child class provides a specific implementation of a method that is already defined in the parent class.
# Allows child classes to customize or modify behavior.
# The method name and parameters must be the same.
# Use super() if you want to call the parent version as well.

class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):  # Overriding the parent method
        print("Dog barks")

d = Dog()
d.sound()  # Output: Dog barks

print("--------------------------------------------------------------------------")
# using self()
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        super().sound()  # call parent method
        print("Dog barks")

d = Dog()
d.sound()


# method overloading in python
# NO — Python does not support traditional method overloading like Java or C++.

# Python handles this differently using default arguments, *args, or manual logic.

# Default Arguments example for method overloading
class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add())           # ➤ 0
print(calc.add(10))         # ➤ 10
print(calc.add(10, 20))     # ➤ 30
print(calc.add(10, 20, 30)) # ➤ 60


# *args (Variable-Length Arguments)  example for method overloading
class Calculator:
    def add(self, *args):
        total = 0
        for num in args:
            total += num
        return total

calc = Calculator()
print(calc.add(5))                  # ➤ 5
print(calc.add(5, 10, 15))          # ➤ 30
print(calc.add(1, 2, 3, 4, 5, 6))   # ➤ 21


# Manual Logic Inside Method  example for method overloading

class Calculator:
    def add(self, a=None, b=None):
        if a is not None and b is not None:
            return a + b
        elif a is not None:
            return a + 10  # default addition
        else:
            return 0

calc = Calculator()
print(calc.add(5, 5))    # ➤ 10
print(calc.add(7))       # ➤ 17
print(calc.add())        # ➤ 0


# duck typing concept in polymorphism 
# Duck Typing means  type or class of an object is less important than the methods and properties it has.
# Python focuses on behavior, not on inheritance hierarchy or type checking.
# If an object implements the required method(s), Python will accept it — even if it's from a different class.

class Duck:
    def quack(self):
        print("Quack! Quack!")

class Person:
    def quack(self):
        print("I'm imitating a duck!")

def make_it_quack(thing):
    thing.quack()  # No type checking, just method call

make_it_quack(Duck())    # Quack! Quack!
make_it_quack(Person())  # I'm imitating a duck!



# abstraction in python 
# Abstraction is the process of hiding the implementation details and showing only the essential features to the user.

# In Python, abstraction is often achieved through:
# Abstract Classes
# Abstract Methods

# Python provides the abc module (abc = Abstract Base Class) to define abstract classes.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# animal = Animal()  ❌ Can't instantiate abstract class
dog = Dog()
dog.make_sound()     # Bark!



# Abstract Class with Concrete Method

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    def stop_engine(self):
        print("Engine stopped.")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

c = Car()
c.start_engine()   # Car engine started.
c.stop_engine()    # Engine stopped.


# Multiple Abstract Methods

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

    def perimeter(self):
        return 2 * (self.l + self.w)

r = Rectangle(5, 4)
print(r.area())        # 20
print(r.perimeter())   # 18
