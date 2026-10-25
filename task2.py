tasks = []

while True:
    print("\n--- TO-DO LIST APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append({"task": task, "done": False})
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["done"] else "Pending"
                print(f"{i}. {task['task']} - {status}")

    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["done"] else "Pending"
                print(f"{i}. {task['task']} - {status}")

            try:
                number = int(input("Enter task number: "))

                if 1 <= number <= len(tasks):
                    tasks[number - 1]["done"] = True
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        if not tasks:
            print("No tasks available to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["done"] else "Pending"
                print(f"{i}. {task['task']} - {status}")

            try:
                number = int(input("Enter task number to delete: "))

                if 1 <= number <= len(tasks):
                    deleted_task = tasks.pop(number - 1)
                    print(f"Deleted task: {deleted_task['task']}")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        print("Thank you for using the To-Do List App!")
        break

    else:
        print("Invalid choice. Please try again.")