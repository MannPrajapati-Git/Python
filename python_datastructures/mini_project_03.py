# duplicate finder


items = ["apple", "banana", "orange", "apple", "mango", "banana", "grape", "apple"]

seen = []
duplicates = []

for item in items:
    if item not in seen:
        seen.append(item)
    elif item not in duplicates:
        duplicates.append(item)

unique_items = seen

print(" Duplicates:")
print(duplicates)

print("\n Unique Items:")
print(unique_items)
