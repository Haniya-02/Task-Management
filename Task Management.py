def task_management():
    tasks = []
    print('Welcome to the Task Management System!')

    # Get the number of tasks to add
    total_task = int(input("Enter how many tasks you want to add: "))

    # Add tasks
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append({"task": task_name, "done": False})

    # Display tasks
    def display_tasks():
        print("\nYour tasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{idx}. {task['task']} - {status}")
        print()

    display_tasks()

    # Options for task management
    while True:
        print("Options:")
        print("1. Add a new task")
        print("2. Mark a task as done")
        print("3. Remove a task")
        print("4. View all tasks")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            new_task = input("Enter the new task: ")
            tasks.append({"task": new_task, "done": False})
            print("Task added successfully!")

        elif choice == 2:
            task_number = int(input("Enter the task number to mark as done: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == 3:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)
                print("Task removed successfully!")
            else:
                print("Invalid task number.")

        elif choice == 4:
            display_tasks()

        elif choice == 5:
            print("Exiting the Task Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

        # Display tasks after each operation
        display_tasks()

    if __name__ == "__main__":
    task_management()