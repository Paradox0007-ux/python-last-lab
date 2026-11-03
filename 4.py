
tasks = []

while True:
    print("\n===== TASK SCHEDULER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Execute Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter task name: ")
        priority = input("Is this a high priority task? (yes/no): ")
        available = input("Is the system available? (yes/no): ")

        tasks.append({
            "name": task_name,
            "priority": priority == "yes",
            "available": available == "yes"
        })

        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nScheduled Tasks:")
            for i, task in enumerate(tasks, 1):
                print(i, task["name"])

    elif choice == "3":
        if not tasks:
            print("No tasks to execute.")
        else:
            for task in tasks:
                print("\nChecking:", task["name"])

                if task["priority"] and task["available"]:
                    print("Executing high priority task:", task["name"])

                elif task["priority"] or task["available"]:
                    print("Executing normal priority task:", task["name"])

                elif not task["priority"] and not task["available"]:
                    print("Task skipped:", task["name"])

                else:
                    print("Task condition not satisfied.")

    elif choice == "4":
        print("Exiting Task Scheduler...")
        break

    else:
        print("Invalid choice! Try again.")
