# Simple To-Do List

todo_list = []

while True:
    task = input("Enter a task (or 'quit' to stop): ")
    if task.lower() == "quit":
        break
    todo_list.append(task)

print("Your To-Do List:")
for task in todo_list:
    print(task)
