import os
import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=2)

def show_tasks(tasks):
    print("\nTask List:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. [{task['status']}] {task['description']}")

def add_task(tasks, description):
    task = {"description": description, "status": "Incomplete"}
    tasks.append(task)
    save_tasks(tasks)
    print(f"\nTask added: {description}")

def delete_task(tasks, index):
    try:
        description = tasks.pop(index - 1)['description']
        save_tasks(tasks)
        print(f"\nTask deleted: {description}")
    except IndexError:
        print("\nInvalid task index.")

def mark_complete(tasks, index):
    try:
        tasks[index - 1]['status'] = "Complete"
        save_tasks(tasks)
        print("\nTask marked as complete.")
    except IndexError:
        print("\nInvalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nOptions:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == '3':
            index = int(input("Enter the task index to delete: "))
            delete_task(tasks, index)
        elif choice == '4':
            index = int(input("Enter the task index to mark as complete: "))
            mark_complete(tasks, index)
        elif choice == '5':
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()