#Encapsulation in Python
# Encapsulation is the practice of restricting access to certain components of an object and protecting the internal state from unintended interference.

# We use:

# _var : Protected variable (convention only, not enforced)

# __var : Private variable (name mangled)

# Getter & Setter methods to access/update private data safely


# Protected Variable Example (_var)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks  # protected variable

    def show(self):
        print(f"{self.name}'s marks: {self._marks}")

obj = Student("Mann", 85)
obj.show()
print(obj._marks)  # Still accessible, but not recommended


# Private Variable Example (__var)

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def show_balance(self):
        print("Balance:", self.__balance)

obj = BankAccount(10000)
obj.show_balance()
# print(obj.__balance) ❌ Error
print(obj._BankAccount__balance)  # ✅ Access using name mangling (not recommended)



# Getter and Setter Methods (Safe Access)

class Employee:
    def __init__(self):
        self.__salary = 50000  # private variable

    # Getter
    def get_salary(self):
        return self.__salary

    # Setter
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary!")

emp = Employee()
print(emp.get_salary())     # ➜ 50000
emp.set_salary(60000)       
print(emp.get_salary())     # ➜ 60000
emp.set_salary(-10000)      # ➜ Invalid salary!
