# lists in python
# lists are mutable
# lists can contain different data types like integers, float, strings, and even other lists

# Declaring Lists in Python there are two ways to declare a list
# 1. Using the list() constructor
# 2. Using square brackets []
# Both methods are valid, but using square brackets is more common and preferred in practice.

# 1️⃣ Using list() constructor (older method)
my_list1 = list((1, 2, 3, 4, 5))
print("List using list() constructor:", my_list1)

# 2️⃣ Using square brackets [] (most commonly used)
my_list2 = [10, 20, 30, 40, 50]
print("List using square brackets:", my_list2)

# 3️⃣ Declaring an empty list (two ways)
empty_list1 = list()
empty_list2 = []
print("Empty list 1:", empty_list1)
print("Empty list 2:", empty_list2)
print("----------------------------------------------------")   

names=["Mann", "Heli", "Roshni", "Divyang"]
print("Names list:", names)
print("First name:", names[1])  # Accessing  element using index and index starts from 0
print("Last name:", names[-1])  # Accessing last element using negative index

# List slicing examples
print("slicing the list:", names[:2])  # Slicing the list to get first two elements
print("Slicing the list:", names[1:])  # Slicing from the second element to the end
print("Slicing names:", names[1:3])  # Slicing the list
print("Slicing names with step:", names[0:4:2])  # Slicing with step
print("----------------------------------------------------")

# changing list elements
names[0] = "Mann Sir"
print("Updated names list:", names)  # Updated list after changing the first element

print("----------------------------------------------------")
# interview question 
# example 1
print("interview question example:")
names = ["Mann", "Heli", "Roshni", "Divyang"]
print("get a element using slice",names[1:2])
# now change that element using slice
names[1:2] ="Heli Ma,am"
print("Updated names list after slice change:", names)  # Updated list after changing the second element using slice

# output -> Updated names list after slice change: ['Mann', 'H', 'e', 'l', 'i', ' ', 'M', 'a', ',', 'a', 'm', 'Roshni', 'Divyang']

# after seeing the output my reaction is like i dont want this type of name 

# so solve this problem you should do it like below 
names = ["Mann", "Heli", "Roshni", "Divyang"]
names[1:2] = ["Heli Ma,am"]
print("Updated names list after correct slice change:", names)  # Updated list after changing the second element using slice 

# output -> Updated names list after correct slice change: ['Mann', 'Heli Ma,am', 'Roshni', 'Divyang']
print("----------------------------------------------------")
# example 2

# List for demonstration
names = ["Mann", "Heli", "Roshni", "Divyang"]
print("Original list:", names)

# 1. Add elements using slicing (insert at index 1)
names[1:1] = ["Test1", "Test2"]
print("After inserting ['Test1', 'Test2'] at index 1:", names)

# 2. Delete elements using slicing (remove index 2 and 3)
names[2:4] = []
print("After deleting elements at index 2 and 3:", names)

# 3. Replace elements using slicing (replace index 1 and 2)
names[1:3] = ["NewName1", "NewName2"]
print("After replacing index 1 and 2 with ['NewName1', 'NewName2']:", names)

# 4. Add element at the end using slicing
names[len(names):] = ["LastOne"]
print("After adding 'LastOne' at the end:", names)

# 5. Remove all elements except the first using slicing
names[1:] = []
print("After keeping only the first element:", names)


print("----------------------------------------------------")

names = ["Mann", "Heli", "Roshni", "Divyang"]
for i in names:
    print(i ,end=" ") # printing elements in the same line

print("\n-----------------------------------------------------")

# List methods 
names = ["Mann", "Heli", "Roshni", "Divyang"]
names.append("Vishvjit") # Adds an element to the end of the list
print("After append:", names)

names.pop()
print("After pop:",names) # Removes the last element from the list

names.remove("Roshni") # Removes the first occurrence of the specified element
print("After remove:", names) # Removes "Roshni" from the list

names.insert(1, "kanho") # Inserts an element at the specified index
print("After insert:", names) # Inserts "kanho" at index 1

names_copy=names.copy() # Creates a shallow copy of the list
print("Copy of names:", names_copy) # Prints the copied list 
names_copy.append("Roshni")
print(names_copy) 
print(names)
# so from the above copy example we can say that each have different memory 

names = ["Mann", "Heli", "Roshni", "Divyang"]
names.extend(["Vishvjit", "Kanho"]) # Extends the list by appending elements from another iterable
print("After extend:", names) # Appends "Vishvjit" and "Kanho" to the list

numbers=[1,5,2,9,5]
numbers.sort() # Sorts the list in ascending order
print("Sorted numbers:", numbers) # Prints the sorted list
# if there is strings inside the list then it will sort the list in alphabetical order

names.reverse() # Reverses the order of the list
print("Reversed names:", names) # Prints the reversed list

index=names.index("Heli") # Returns the index of the first occurrence of the specified element
print("Index of 'Heli':", index) # Prints the index of "Heli

count=names.count("Mann") # Returns the number of occurrences of the specified element
print("Count of 'Mann':", count) # Prints the count of "Mann

names.clear() # Removes all elements from the list
print("After clear:", names) # Prints the empty list




print("-----------------------------------------------------")

# List comprehensions
# the list comprehension is a concise way to create lists in Python
# It consists of brackets containing an expression followed by a for clause, and can also include additional for or if clauses.
# Example: Create a list of squared numbers from 0 to 9
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)

# Example: Create a list of even numbers from 0 to 9
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]