# A for loop with user input
items = input("Enter some items, separated by commas: ").split(",")
for item in items:
    print(f"I have a {item.strip()}")
