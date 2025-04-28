# File parser

def parse_file(filename):
    with open(filename, "r") as file:
        content = file.readlines()
    return content

def process_file(filename):
    content = parse_file(filename)
    for line in content:
        print(line.strip())

filename = input("Enter the file name to parse: ")
process_file(filename)
