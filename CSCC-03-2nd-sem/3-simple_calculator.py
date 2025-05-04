def add(x, y):
    return x + y 
    
def subtract(x, y):
    return x - y
    
def multiply(x, y):
    return x * y
    
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
    
def calculator():
    print("\n--- Simple Calculator ---")
    while True:
        try:
            print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
            choice = input("Enter your choice: ")

            if choice == '5':
                print("Exiting the calculator. Goodbye!")
                break
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Invalid choice! Please select a valid operation.")       
        except ValueError:
            print("Invalid input! Please enter numeric values.") 
if __name__ == "__main__":
    calculator()
