# List with user input
fruits = input("Enter a list of fruits separated by commas: ").split(",")

# Accessing elements
print(f"First fruit: {fruits[0]}")

# Adding and removing elements
fruits.append(input("Enter a fruit to add: "))
fruits.remove(input("Enter a fruit to remove: "))

# Iterating over a list
for fruit in fruits:
    print(fruit)
