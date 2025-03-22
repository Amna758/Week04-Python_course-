from file_handler import read_tasks, write_tasks

def add_task(task):
    """Adds a new task to the file."""
    tasks = read_tasks()
    tasks.append(task)
    write_tasks(tasks)
    print("Task added successfully!")

def remove_task(task_number):
    """Removes a task by its number."""
    tasks = read_tasks()
    try:
        task_number = int(task_number) - 1
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            write_tasks(tasks)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def update_task(task_number, new_task):
    """Updates an existing task."""
    tasks = read_tasks()
    try:
        task_number = int(task_number) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number] = new_task
            write_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks():
    """Displays all tasks."""
    tasks = read_tasks()
    if tasks:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks found.")
