print("\n\n")

import os
from pathlib import Path

from definitions import *
from list_manager import *

STORAGE_DIR = Path(__file__).resolve().parent / "storage"  # A little help from AI


def is_invalid(choice, maximum):
    try:
        choice = int(choice)
    except (TypeError, ValueError):
        choice = None

    if choice is None or choice < 1 or choice > maximum:
        print("\nError >>>> Invalid input\n\n")
        return True
    else:
        return False


# ======== Main run ========
task_lists = load_lists()

print("Welcome to your To-Do list app!")
while True:
    number_of_lists = len(task_lists)
    print(
        f"""You have {number_of_lists} lists. \ndefault list: "{task_lists[0].name}"\n"""
    )

    menu =  "\n      1. Show lists" \
            "\n      3. Save lists" \
            "\n      4. Exit Program"

    print("==== Menu ====" "\n Actions:" f"{menu}")

    choice = input("Enter item index to continue: ")
    if is_invalid(choice, 4):
        continue
    choice = int(choice)

    # ==== Show lists ====
    if choice == 1:
        print("\n\n ==== To-Do Lists ====")
        print("     ID   | Name")
        for i, task_list in enumerate(task_lists):
            print(f"      {i + 1}   | {task_list.name}")

        print( "==== List Actions ===="
            "\n     1. Create new list"
            "\n     2. Open list"
            "\n     3. Remove list"
            "\n     4. Back to main menu"
        )

        action = input("Enter item index to continue: ")
        if is_invalid(action, 4):
            continue
        action = int(action)

        # ==== Create new list ====
        if action == 1:
            name = input("Enter the new list name: ").strip()
            if not name:
                print("\nError >>>> List name cannot be empty\n\n")
                continue

            # New IDs are 1 number more than the highest existing ID in task_list
            new_id = str(max(int(task_list.id) for task_list in task_lists) + 1)
            task_lists.append(ToDoList(name, [], new_id))

        # ==== Open list ====
        elif action == 2:
            try:
                list_id = (
                    int(input("Enter list ID to open: ")) - 1
                )  # -1 is used because list IDs in Python begin from 0
            except (TypeError, ValueError):
                list_id = -1
            if not 0 <= list_id < len(task_lists):
                print("\nError >>>> Invalid list ID\n\n")
                continue

            current_list = task_lists[list_id]
            current_list.show_all_tasks()

            print(
                "==== Choose an action ===="
                "\n     1. Create a task"
                "\n     2. Edit a task"
                "\n     3. Remove a task"
                "\n     4. Back to list menu"
            )
            action = input("Enter action index to continue: ")
            if is_invalid(action, 4):
                continue
            action = int(action)

            # ==== Create a task ===
            if action == 1:
                name = input("Enter task name: ").strip()
                description = input("Enter description: ").strip()
                priority = input("Choose priority (1. Low, 2. Medium, 3. High): ")
                priorities = {"1": "Low", "2": "Medium", "3": "High"}

                if not name or priority not in priorities:
                    print("\nError >>>> Task name and priority must be valid\n")
                    continue

                current_list.add_task(
                    Task("New", name, description, priorities[priority])
                )
                print("\nTask created successfully.\n")

            # ==== Edit a task ====
            elif action == 2:
                if not current_list.tasks:
                    print("\nError >>>> This list has no tasks\n")
                    continue

                try:
                    task_index = int(input("Enter task ID to edit: ")) - 1
                except ValueError:
                    task_index = -1
                if not 0 <= task_index < len(current_list.tasks):
                    print("\nError >>>> Invalid task ID\n")
                    continue

                task = current_list.tasks[task_index]
                name = input(f"Enter task name [{task.name}]: ").strip()
                description = input(f"Enter description [{task.description}]: ").strip()
                priority = input(
                    f"Choose priority (1. Low, 2. Medium, 3. High) [{task.pirority}]: "
                ).strip()
                status = input(f"Enter status (New/Done) [{task.status}]: ").strip()
                priorities = {"1": "Low", "2": "Medium", "3": "High"}

                if priority and priority not in priorities:
                    print("\nError >>>> Invalid priority\n")
                    continue
                if status and status not in ("New", "Done"):
                    print("\nError >>>> Status must be New or Done\n")
                    continue

                task.name = name or task.name
                task.description = description or task.description
                task.pirority = priorities.get(priority, task.pirority)
                task.status = status or task.status
                print("\nTask updated successfully.\n")

            # ==== Remove a task ====
            elif action == 3:
                if not current_list.tasks:
                    print("\nError >>>> This list has no tasks\n")
                    continue

                try:
                    task_index = int(input("Enter task ID to remove: ")) - 1
                except ValueError:
                    task_index = -1
                if not 0 <= task_index < len(current_list.tasks):
                    print("\nError >>>> Invalid task ID\n")
                    continue

                task = current_list.tasks[task_index]
                confirmation = (
                    input(f"Are you sure you want to remove '{task.name}'? (y/n): ")
                    .strip()
                    .lower()
                )
                if confirmation == "y":
                    current_list.remove_task(task)
                    print("\nTask removed successfully.\n")
                else:
                    print("\nTask removal canceled.\n")

        # ==== Remove list ====
        elif action == 3:
            try:
                list_id = int(input("Enter list ID to remove: ")) - 1
            except (TypeError, ValueError):
                list_id = -1  # To match the index in task_lists

            if not 0 <= list_id < len(task_lists):
                print("\nError >>>> Invalid list ID\n\n")
                continue

            input_confirmation = (
                input(
                    f"Are you sure you want to remove the list '{task_lists[list_id].name}'? (y/n): "
                )
                .strip()
                .lower()
            )

            if input_confirmation == "y":
                removed_list = task_lists.pop(list_id)
                os.remove(
                    STORAGE_DIR / f"L-{list_id + 1}.csv"
                )  # +1 to match the original ID
                save_lists(task_lists)  # Save the updated list of to-do lists

                print(f"\nList '{removed_list.name}' removed successfully.\n")
            else:
                print("\nList removal canceled.\n")

    # ==== Save lists ====
    elif choice == 2:
        save_lists(task_lists)

    # ==== Exit the program ====
    elif choice == 3:
        print("\n\nExiting program...")
        break
