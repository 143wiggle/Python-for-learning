# List comprehension with user input
numbers = list(map(int, input("Enter numbers separated by commas: ").split(",")))
squares = [x ** 2 for x in numbers]

print(f"The squares of the numbers are: {squares}")
