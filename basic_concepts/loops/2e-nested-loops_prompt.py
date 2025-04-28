# Nested loops with user input
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

grid = []
for i in range(rows):
    row = input(f"Enter items for row {i+1}, separated by commas: ").split(",")
    grid.append(row)

for row in grid:
    for cell in row:
        print(cell.strip())
