# File handling with user input

# Writing to a file
filename = input("Enter the file name to write to: ")
with open(filename, "w") as file:
    file.write(input("Enter some text: "))

# Reading from a file
filename = input("Enter the file name to read from: ")
with open(filename, "r") as file:
    content = file.read()
    print(content)
