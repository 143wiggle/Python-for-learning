# To-Do List with user interaction and functions

def add_task(todo_list, task):
    todo_list.append(task)

def display_tasks(todo_list):
    print("Your To-Do List:")
    for task in todo_list:
        print(task)

def todo_list_app():
    todo_list = []

    while True:
        task = input("Enter a task (or 'quit' to stop): ")
        if task.lower() == "quit":
            break
        add_task(todo_list, task)

    display_tasks(todo_list)

todo_list_app()
