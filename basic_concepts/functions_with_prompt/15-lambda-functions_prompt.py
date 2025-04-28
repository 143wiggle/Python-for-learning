# Lambda function with user input
add = lambda x, y: x + y

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print(f"The sum is: {add(x, y)}")
