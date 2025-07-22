# loops in python
# also known as iteration statements


# while loop: executes a block of code as long as a condition is true

n=0
while n < 5:
    print("n is currently:", n)
    n += 1  # increment n by 1  

print("-------------------------------------------------------------")

# for loop: iterates over a sequence (like a list, tuple, or string)

# using range() function to generate a sequence of numbers
for i in range(5):  
    print("i is currently:", i)

print("-------------------------------------------------------------")

for j in range(1, 6):  # range(start, stop) generates numbers from start to stop-1
    print("i is currently:", j)

print("-------------------------------------------------------------")  

# for loop with a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Current fruit:", fruit)

print("-------------------------------------------------------------")

# for loop with a string
# it iterates each character from the string 1 at a row
for char in "MannSir":
    print("Current character:", char)

0