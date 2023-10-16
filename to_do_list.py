# Create an empty list to store tasks
tasks = []


# Function to add a task
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")


# Function to view tasks
def view_tasks():
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks to display.")


# Function to mark a task as complete
def mark_complete():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            completed_task = tasks.pop(task_number - 1)
            print(f"Marked '{completed_task}' as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")


# Function to delete a task
def delete_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Deleted '{deleted_task}'.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")


# Main loop
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
