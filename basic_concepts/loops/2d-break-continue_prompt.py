# Break and continue with user-defined conditions
items = input("Enter a list of items separated by commas: ").split(",")
skip_item = input("Enter an item to skip: ").strip()

for item in items:
    if item.strip() == skip_item:
        continue  # Skip the user-defined item
    print(f"Processing item: {item.strip()}")
