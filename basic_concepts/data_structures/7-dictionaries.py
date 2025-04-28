# A dictionary in Python: key-value pairs
person = {"name": "Alice", "age": 25, "city": "New York"}

# Accessing values by key
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Adding and updating values
person["age"] = 26
person["job"] = "Engineer"

# Iterating through dictionary keys and values
for key, value in person.items():
    print(f"{key}: {value}")
