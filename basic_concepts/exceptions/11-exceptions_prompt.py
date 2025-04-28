# Exception handling with user input

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
finally:
    print("Execution completed.")
