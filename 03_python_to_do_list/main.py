import json
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks():
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, indent=2), encoding="utf-8")


def show_tasks(tasks):
    print("\\n=== YOUR TASKS ===")
    if not tasks:
        print("No tasks yet.")
        return
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{index}. [{status}] {task['title']}")


def main():
    tasks = load_tasks()
    while True:
        print("\\n--- Python To-Do List ---")
        print("1. View tasks\\n2. Add task\\n3. Mark task complete\\n4. Delete task\\n5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Enter task: ").strip()
            if title:
                tasks.append({"title": title, "done": False})
                save_tasks(tasks)
                print("Task added.")
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            show_tasks(tasks)
            try:
                number = int(input("Task number to complete: "))
                if 1 <= number <= len(tasks):
                    tasks[number - 1]["done"] = True
                    save_tasks(tasks)
                    print("Task marked complete.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Enter a valid number.")
        elif choice == "4":
            show_tasks(tasks)
            try:
                number = int(input("Task number to delete: "))
                if 1 <= number <= len(tasks):
                    removed = tasks.pop(number - 1)
                    save_tasks(tasks)
                    print(f"Deleted: {removed['title']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Enter a valid number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose 1 to 5.")


if __name__ == "__main__":
    main()
