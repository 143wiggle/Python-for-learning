# File handling: Writing and Reading files

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, world!\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
