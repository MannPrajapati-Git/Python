# Access Modifiers in Python
# Python has three types of access modifiers used to control access to class members (variables/methods):

# Public : (no prefix) or normal name :	Accessible from anywhere
# Protected	: _var : Accessible within class and subclasses
# Private :	__var :	Accessible only within the class (name mangled)


# Public Members

class Car:
    def __init__(self):
        self.color = "Red"  # public

c = Car()
print(c.color)  # ✅ Allowed


# Protected Members (_var)
class Vehicle:
    def __init__(self):
        self._engine = "Diesel"  # protected

class Truck(Vehicle):
    def show_engine(self):
        print("Engine type:", self._engine)

t = Truck()
t.show_engine()         # ✅ Allowed (subclass)
print(t._engine)        # ⚠️ Technically allowed, but discouraged

# Private Members (__var)

class Bank:
    def __init__(self):
        self.__balance = 5000  # private

    def show_balance(self):
        print("Balance is:", self.__balance)

b = Bank()
b.show_balance()       # ✅ Allowed

# print(b.__balance)   ❌ AttributeError
# Accessed internally as: _Bank__balance
print(b._Bank__balance)  # ⚠️ Hack (Not recommended)




# interview example : access control using getter and setter

class Student:
    def __init__(self):
        self.__marks = 90

    def get_marks(self):
        return self.__marks

    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid marks")

s = Student()
print(s.get_marks())  # ✅ 90
s.set_marks(95)
print(s.get_marks())  # ✅ 95
