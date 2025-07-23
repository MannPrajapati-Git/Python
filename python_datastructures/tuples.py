# tuples in python
# Tuples are immutable sequences in Python, typically used to store collections of heterogeneous data.
# They are defined by enclosing elements in parentheses.

# 📘 Declaring Tuples in Python

# 1️⃣ Using parentheses () — Most common method
my_tuple1 = ("Mann", "Heli", "Roshni")
print("Tuple using parentheses:", my_tuple1)


# 2️⃣ Using tuple() constructor — Alternate method
my_tuple2 = tuple(["Prajapati", "Divyang", "Kanho"])
print("Tuple using tuple() constructor:", my_tuple2)
# 3️⃣ Using tuple() with a single element — Note the comma
my_tuple3 = ("SingleElement",)  # Comma is necessary to define a single-element tuple
print("Single-element tuple:", my_tuple3)


names = ("Mann", "Heli", "Divyang", "Roshni")
print(names)

# Accessing elements in a tuple
print(names[3])  # Accessing the element
print(names[-1]) # Accessing the last element
print(names[1:3])  # Slicing a tuple

# this accessing and all slicing works same as in lists so i m not repeating it here

# in tuples we can not change the value of the element
# names[0] = "MannSir"  # This will raise a TypeError

# Tuples can be concatenated and repeated
new_names = names + ("Vishvjit", "Kanho")
print(new_names)  # Concatenation of tuples

if "Mann" in names:
    print("Mann is present in the tuple")   

# Tuples can be unpacked into variables
a, b, c, d = names
print(a)  # Output: Mann
print(b)  # Output: Heli
print(c)  # Output: Divyang
print(d)  # Output: Roshni

print("---------------------------------------------------")

# Tuple methods and functions

# count() – kisi element ka count batata hai
print("Count of 'Mann':", names.count("Mann"))

# index() – kisi element ka first index batata hai
print("Index of 'Divyang':", names.index("Divyang"))

# len() – length of tuple
print("Length of tuple:", len(names))

numbers= (1, 2, 3, 4, 5)
# max() – max element 
print("Max element:", max(numbers))

# min() – min element
print("Min element:", min(numbers))

# sum() – sum of elements (agar numbers hain)
numbers = (10, 20, 30, 40)
print("Sum of numbers tuple:", sum(numbers))

# sorted() – tuple ko sorted list bana deta hai
print("Sorted names:", sorted(names))

# tuple() – convert from list to tuple
list1 = ["A", "B", "C"]
tuple1 = tuple(list1)
print("Converted tuple:", tuple1)