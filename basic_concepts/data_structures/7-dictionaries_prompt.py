# Dictionary with user input
person = {
    "name": input("Enter your name: "),
    "age": int(input("Enter your age: ")),
    "city": input("Enter your city: ")
}

# Accessing values by key
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Adding and updating values
person["age"] = int(input("Enter your updated age: "))
person["job"] = input("Enter your job: ")

# Iterating through dictionary keys and values
for key, value in person.items():
    print(f"{key}: {value}")
