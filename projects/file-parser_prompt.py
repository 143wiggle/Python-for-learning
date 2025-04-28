# Advanced File Parser with exception handling

def parse_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.readlines()
        return content
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

def process_file(filename):
    content = parse_file(filename)
    if content:
        for line in content:
            print(line.strip())
    else:
        print("No content to display.")

filename = input("Enter the file name to parse: ")
process_file(filename)
