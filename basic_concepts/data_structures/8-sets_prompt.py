# Set with user input
fruits = set(input("Enter a list of fruits separated by commas: ").split(","))

# Adding and removing items
fruits.add(input("Enter a fruit to add: "))
fruits.remove(input("Enter a fruit to remove: "))

# Iterating through a set
for fruit in fruits:
    print(fruit)

# Set operations with user input
other_fruits = set(input("Enter another set of fruits separated by commas: ").split(","))
print(f"Common fruits: {fruits & other_fruits}")  # Intersection
print(f"All fruits: {fruits | other_fruits}")     # Union
