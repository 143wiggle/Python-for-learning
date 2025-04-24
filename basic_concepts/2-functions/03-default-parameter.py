def greet(name="Guest"):
    print(f"Hi {name}")

prompt_name = input("Enter name: ")

print("This is the default parameter.")
greet()

print("\nThis is what you entered:")
greet(prompt_name)
