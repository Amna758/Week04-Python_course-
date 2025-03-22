from task_operations import add_task, remove_task, update_task, view_tasks

def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task description: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
            task_number = input("Enter task number to remove: ")
            remove_task(task_number)
        elif choice == "3":
            view_tasks()
            task_number = input("Enter task number to update: ")
            new_task = input("Enter new task description: ")
            update_task(task_number, new_task)
        elif choice == "4":
            view_tasks()
        elif choice == "5":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
