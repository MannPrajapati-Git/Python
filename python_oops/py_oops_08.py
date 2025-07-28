# type cheking in OOP


# isinstance() and issubclass()
#  isinstance(object, class)
# Checks if an object is an instance of a class or its subclass.

# issubclass(child, parent)
# Checks if a class is a subclass of another class.


class Animal:
    pass

class Dog(Animal):
    pass

class Car:
    pass

tommy = Dog()

# isinstance()
print(isinstance(tommy, Dog))        # ✅ True
print(isinstance(tommy, Animal))     # ✅ True
print(isinstance(tommy, Car))        # ❌ False

# issubclass()
print(issubclass(Dog, Animal))       # ✅ True
print(issubclass(Dog, Car))          # ❌ False
print(issubclass(Dog, object))       # ✅ True (All classes inherit from object)
