# What is a Module?
# A module is simply a Python file (.py) that contains functions, variables, or classes that you can reuse in another file using import.


# user defined modules
# import file 
import mod_file_01

print(mod_file_01.greet("Mann"))
print(mod_file_01.square(5))


# import modules for the file

from mod_file_01 import greet,square

print(greet("Heli"))
print(square(7))

# built in modules
# there are thousands of modules in python here i will just show two modules


# math module
import math

# Square Root
print("squareroot of 25 =", math.sqrt(25))       # 5.0

# Ceiling (smallest integer ≥ x)
print("Ceil of 4.2 =", math.ceil(4.2))   # 5

# Floor (largest integer ≤ x)
print("Floor of 4.8 =", math.floor(4.8)) # 4

# Power
print("2^3 =", math.pow(2, 3))       # 8.0

# Pi constant
print("Value of pi =", math.pi)     # 3.14159...


# random module
import random

# Random number between 0 and 1
print("Random float 0-1:", random.random())

# Random integer between 1 and 10
print("Random int 1-10:", random.randint(1, 10))

# Random choice from list
colors = ["red", "blue", "green"]
print("Random choice:", random.choice(colors))

# Shuffle list
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print("Shuffled list:", nums)
