import os

TASK_FILE = "tasks.txt"

def ensure_file_exists():
    """Creates the tasks.txt file if it doesn't exist."""
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w") as file:
            pass  # Create an empty file

def read_tasks():
    """Reads all tasks from the file."""
    ensure_file_exists()
    with open(TASK_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def write_tasks(tasks):
    """Writes the list of tasks to the file."""
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")
