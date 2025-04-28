# Direct iteration with user input for custom list
items = input("Enter items separated by commas: ").split(",")
for item in items:
    print(f"You entered: {item.strip()}")
