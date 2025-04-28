# Exercise: File handling with user input
filename = input("Enter the filename: ")
text = input("Enter the text to write to the file: ")

with open(filename, "w") as file:
    file.write(text)
