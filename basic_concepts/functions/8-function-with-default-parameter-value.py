# 'name' has a default value of "Guest"
def greet(name="Guest"):
    print("Welcome,", name)

# One with input ("Wiggle"), one with default ("Guest")
greet("Wiggle")
greet()
