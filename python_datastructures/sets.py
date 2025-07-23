# sets in python
# Sets are unordered collections of unique elements in Python, typically used to store collections of homogeneous data
# They are defined by enclosing elements in curly braces or using the set() constructor.


#  Declaring Sets in Python

# 1️⃣ Using curly braces {} (common method)
my_set1 = {1, 2, 3, 4, 5}
print("Set using curly braces:", my_set1)

# 2️⃣ Using set() constructor (recommended for empty or from iterable)
my_set2 = set([3, 4, 5, 6])
print("Set using set() constructor:", my_set2)

# 3️⃣ Declaring an empty set (❗ important)
empty_set = set()
print("Empty set:", empty_set)

print("-----------------------------------------------")    

#  Set removes duplicates automatically
duplicate_set = {1, 2, 2, 3, 3, 4}
print("Set after removing duplicates:", duplicate_set)

#  Creating set from string
string_set = set("hello")
print("Set from string:", string_set)

#  Creating set from tuple
tuple_set = set((10, 20, 30, 30))
print("Set from tuple:", tuple_set)

print("-----------------------------------------------")    

#  Basic Set Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Set a:", a)
print("Set b:", b)

# Union
print("Union (a | b):", a | b)
print("Union (a.union(b)):", a.union(b))

# Intersection
print("Intersection (a & b):", a & b)
print("Intersection (a.intersection(b)):", a.intersection(b))

# Difference
print("Difference (a - b):", a - b)
print("Difference (a.difference(b)):", a.difference(b))
print("Difference (b - a):", b - a)
print("Difference (b.difference(a)):", b.difference(a))

# Symmetric Difference
print("Symmetric Difference (a ^ b):", a ^ b)
print("Symmetric Difference (a.symmetric_difference(b)):", a.symmetric_difference(b))

# Subset and Superset
print("Is a subset of b?", a.issubset(b))
print("Is a superset of b?", a.issuperset(b))
print("Is {3,4} subset of a?", {3,4}.issubset(a))
print("Is a disjoint with b?", a.isdisjoint(b))

# Copy
a_copy = a.copy()
print("Copy of set a:", a_copy)

# Add
a_copy.add(10)
print("After add(10):", a_copy)

# Remove (throws error if not present)
a_copy.remove(10)
print("After remove(10):", a_copy)

# Discard (no error if not present)
a_copy.discard(99)
print("After discard(99):", a_copy)

# Update (add multiple elements)
a_copy.update([20, 30])
print("After update([20, 30]):", a_copy)

# Pop (removes a random element)
popped = a_copy.pop()
print("After pop (removed item):", popped)
print("Set after pop:", a_copy)

# Clear (removes all elements)
a_copy.clear()
print("After clear:", a_copy)

# Membership
print("Is 2 in set a?", 2 in a)
print("Is 5 not in set a?", 5 not in a)

