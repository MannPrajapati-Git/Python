# Compositions vs inheritence in python 

#  Inheritance: “Is-A”
# Dog is a type of Animal.

#  Composition: “Has-A”
# Car has a Engine. It’s about including other objects as attributes instead of extending classes.

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition (Car *has-a* Engine)

    def drive(self):
        self.engine.start()
        print("Car is driving")

# Usage
my_car = Car()
my_car.drive()
