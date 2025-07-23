# dictionaries in python 
# Stores data in key: value pairs
# Ordered (Python 3.7+), changeable, and no duplicate keys
# Keys = unique identifiers ALWAYS UNIQUE
# Values = any data type (string, list, int, etc.)
# Fast access using keys (not index)

# there are two ways to declare dictionaries in python
# 1. Using dict() constructor (older method)
# 2. Using curly braces {} (most commonly used)
# both methods are valid but using curly braces is more common and preferred in modern Python code.

# Declaring Dictionaries in Python

# 1️⃣ Using dict() constructor (older method)
my_dict1 = dict(name="Mann", age=22, city="Ahmedabad")
print("Dictionary using dict() constructor:", my_dict1)

# 2️⃣ Using curly braces {} (most commonly used)
my_dict2 = {
    "name": "Prajapati",
    "age": 23,
    "city": "Ahmedabad"
}
print("Dictionary using curly braces:", my_dict2)

# 3️⃣ Declaring an empty dictionary (two ways)
empty_dict1 = dict()
empty_dict2 = {}
print("Empty dictionary 1:", empty_dict1)
print("Empty dictionary 2:", empty_dict2)

print("-----------------------------------------------")

students = {1: "Mann", 2: "Heli", 3: "Divyang" , 4: "Roshni"}
print("Students Dictionary:", students)

# Accessing values in a dictionary
print("Accessing value:", students[2]) # put key inside square brackets

# changing values in a dictionary
students[2] = "Heli Ma,am" # change value of key 2
print("changing value:", students[2]) 

# Adding new key-value pairs to a dictionary
students[5] = "vishvjit"  # Adding a new key-value pair


print("----------------------------------------------------")

for i in students:
    print("Key:", i, "Value:", students[i])

print("---------------------------------------------------")

#Dictionary methods

# get() method
# The get() method returns the value for the specified key if the key is in the dictionary
print("Value for key 1 using get():", students.get(1))  # Output: Mann

#keys() method
# The keys() method returns a view object that displays a list of all the keys in the dictionary
print("Keys in the dictionary:", students.keys())  # Output: dict_keys([1, 2, 3, 4, 5])

# values() method
# The values() method returns a view object that displays a list of all the values in the dictionary
print("Values in the dictionary:", students.values())  # Output: dict_values(['Mann', 'Heli Ma,am', 'Divyang', 'Roshni', 'vishvjit'])

#update() method
# The update() method updates the dictionary with the specified key-value pairs
students.update({2: "heli"}) # Update value for key 2
print("Students dictionary after update:", students)  # Output: {1: 'Mann', 2: 'heli', 3: 'Divyang', 4: 'Roshni', 5: 'vishvjit'}

# setdefault() method
# The setdefault() method returns the value of the specified key if it is in the dictionary
# If not, it inserts the key with a specified value
default_value = students.setdefault(6, "New Student")  # Key 6 does not exist, so it will be added with the value "New Student"
print("Default value for key 6:", default_value)  # Output: New Student
print("Students dictionary after setdefault:", students)  # Output: {1: 'Mann', 2: 'heli', 3: 'Divyang', 4: 'Roshni', 5: 'vishvjit', 6: 'New Student'}

# any() method
# The any() method returns True if any key in the dictionary evaluates to True  
print("Any key evaluates to True:", any(students))  # Output: True (since the dictionary is not empty)

# all() method
# The all() method returns True if all keys in the dictionary evaluate to True
print("All keys evaluate to True:", all(students))  # Output: True (since all keys are non-empty)


# items() method
# The items() method returns a view object that displays a list of a dictionary's key-value tuple pairs
print("Items in the dictionary:", students.items())  # Output: dict_items([(1, 'Mann'), (2, 'Heli Ma,am'), (3, 'Divyang'), (4, 'Roshni')])

# length of dictionary
# The len() function returns the number of items in a dictionary
print("Length of students dictionary:", len(students))  # Output: 4

# pop() method
# The pop() method removes the specified key and returns the corresponding value
removed_value = students.pop(3)  # Removes key 3 and returns its value
print("Removed value for key 3:", removed_value)  # Output: Divyang
print("Students dictionary after pop:", students)  # Output: {1: 'Mann', 2: 'Heli Ma,am', 4: 'Roshni'}

# popitem() method
# The popitem() method removes the last inserted key-value pair and returns it as a tuple
last_item = students.popitem()  # Removes the last item (key 4, value 'Roshni')
print("Last item removed:", last_item)  # Output: (4, 'Roshni')
print("Students dictionary after popitem:", students)  # Output: {1: 'Mann', 2: 'Heli Ma,am'}

# del keyword
# The del keyword removes the specified key-value pair from the dictionary
del students[2]  # Removes key 2
print("Students dictionary after del:", students)  # Output: {1: 'Mann'}

copy_students = students.copy()  # Creates a shallow copy of the dictionary
print("Copy of students dictionary:", copy_students)  # Output: {1: 'Mann'}

# clear() method
# The clear() method removes all items from the dictionary
students.clear()  # Clears the dictionary


# Example: dict.fromkeys() for students

# List of student names (as keys)
student_names = ["Mann", "Heli", "Roshni"]

# 1. Sabhi students ko ek hi default value dena
default_value = "Present"
attendance = dict.fromkeys(student_names, default_value)
print("Attendance dictionary with default value:", attendance)
# Output: {'Mann': 'Present', 'Heli': 'Present', 'Roshni': 'Present'}

# 2. Sabhi students ko ek hi list assign karna (for demo)
marks_list = [90, 85, 88]
marks = dict.fromkeys(student_names, marks_list)
print("Marks dictionary with same list for all:", marks)
# Output: {'Mann': [90, 85, 88], 'Heli': [90, 85, 88], 'Roshni': [90, 85, 88]}

print("---------------------------------------------------")

students = {1: "Mann", 2: "Heli", 3: "Divyang", 4: "Roshni"}
if 1 in students:
    print("Key 1 is present in the dictionary")
if "Mann" in students.values():
    print("Mann is present in the dictionary")

print("---------------------------------------------------")

# Dictionary Comprehensions
# Dictionary comprehensions provide a concise way to create dictionaries.
squared_numbers = {x: x**2 for x in range(1, 6)} 
print("Squared numbers dictionary:", squared_numbers)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

cubed_numbers = {x: x**3 for x in range(1, 6)}
print("Cubed numbers dictionary:", cubed_numbers)  # Output: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
