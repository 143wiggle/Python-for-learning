# A set in Python: unordered collection with no duplicates
fruits = {"apple", "banana", "cherry"}

# Adding and removing items
fruits.add("date")
fruits.remove("banana")

# Iterating through a set
for fruit in fruits:
    print(fruit)

# Set operations
other_fruits = {"grape", "cherry", "orange"}
print(f"Common fruits: {fruits & other_fruits}")  # Intersection
print(f"All fruits: {fruits | other_fruits}")     # Union
