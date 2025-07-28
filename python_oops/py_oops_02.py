#  Instance & Class Variables	
#  self.variable, ClassName.variable

# Instance Variable
# Declared inside the class using self, typically in __init__().
# Each object gets its own separate copy.
# Changing it in one object does not affect others.

class Student:
    def __init__(self, name, roll_no):
        self.name = name              # Instance Variable
        self.roll_no = roll_no        # Instance Variable

# Creating objects (each has unique data)
student1 = Student("Mann", 101)
student2 = Student("Heli", 102)

# Accessing instance variables
print("Student 1:", student1.name, "-", student1.roll_no)
print("Student 2:", student2.name, "-", student2.roll_no)

print("---------------------------------------------------------------------")

class BankAccount:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name      # Instance Variable
        self.balance = balance              # Instance Variable

    def display_account(self):
        print(f"Account Holder: {self.holder_name}")
        print(f"Balance: {self.balance}")

# Creating two accounts
acc1 = BankAccount("Heli", 10000)
acc2 = BankAccount("Mann", 5000)

acc1.display_account()
acc2.display_account()

print("---------------------------------------------------------------")

# Class Variable
# Declared outside any method but inside the class.
# Shared across all objects of the class.
# Changing it affects all objects (unless overridden by instance variable).

class Student:
    # Class variable (shared by all instances)
    college_name = "Indus University"

    def __init__(self, name, grade):
        self.name = name          # Instance variable
        self.grade = grade        # Instance variable

    def display(self):
        print(f"{self.name} grade {self.grade} at {Student.college_name}")

# Creating objects
student1 = Student("Mann", 9)
student2 = Student("Heli", 9)

student1.display()
student2.display()


print("---------------------------------------------------------------")

class Employee:
    #  Class Variables (shared among all instances)
    company = "CoffeeAurCode"
    total_employees = 0

    def __init__(self, name):
        #  Instance Variable
        self.name = name

        #  Updating the shared class variable
        Employee.total_employees += 1

    def display(self):
        #  Show employee details
        print(f"{self.name} works at {Employee.company}")

# Creating first employee
emp1 = Employee("Mann")
emp1.display()
#  Creating second employee
emp2 = Employee("Heli")
emp2.display()
#  After creating employees
print(f" Total Employees : {Employee.total_employees}") 
