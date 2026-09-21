print("\n\n")

import os
from pathlib import Path

from definitions import *
from list_manager import *

STORAGE_DIR = Path(__file__).resolve().parent / "storage"  # A little help from AI

""" 
This functionis called in menus after the user enters an item index.
This method validates the input to match our rules.
Rules:
- Be integer
- Be less than the 'maximum' variable
"""
def get_valid_choice(choice, maximum):
    try:
        choice = int(choice)
    except (TypeError, ValueError):
        return None

    return choice if 1 <= choice <= maximum else None


# ======== Main run ========
task_lists = load_lists()

print("Welcome to your To-Do list app!")
while True:
    number_of_lists = len(task_lists)
    print(
        f"""You have {number_of_lists} lists. \ndefault list: "{task_lists[0].name}"\n"""
    )

    menu = "\n      1. Show lists" "\n      2. Save lists" "\n      3. Exit Program"

    print("==== Menu ====" "\n Actions:" f"{menu}")

    choice = get_valid_choice(input("Enter item index to continue: "), 3)
    if choice is None:
        print("\nError >>>> Invalid input\n\n")
        continue

    # ==== Show lists ====
    if choice == 1:
        print("\n\n ==== To-Do Lists ====")
        print("     ID   | Name")
        for i, task_list in enumerate(task_lists):
            print(f"      {i + 1}   | {task_list.name}")

        print(
            "==== List Actions ===="
            "\n     1. Create new list"
            "\n     2. Open list"
            "\n     3. Remove list"
            "\n     4. Back to main menu"
        )

        action = get_valid_choice(input("Enter item index to continue: "), 4)
        if action is None:
            print("\nError >>>> Invalid input\n\n")
            continue

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
            list_id = get_valid_choice(
                input("Enter list ID to open: "), len(task_lists)
            )
            if list_id is None:
                print("\nError >>>> Invalid list ID\n\n")
                continue
            list_id -= 1  # List IDs start at 1 for the user, but indexes start at 0.

            current_list = task_lists[list_id]
            current_list.show_all_tasks()

            print(
                "==== Task Actions ===="
                "\n     1. Create a task"
                "\n     2. Edit a task"
                "\n     3. Remove a task"
                "\n     4. Mark a task"
                "\n     5. Back to list menu"
            )
            action = get_valid_choice(input("Enter action index to continue: "), 5)
            if action is None:
                print("\nError >>>> Invalid input\n\n")
                continue

            # ==== Create a task ===
            if action == 1:
                name = input("Enter task name: ").strip()
                description = input("Enter description: ").strip()
                priority = input("Choose priority (1. Low, 2. Medium, 3. High): ")
                priorities = {"1": "Low", "2": "Medium", "3": "High"}
                # I used a dictinary instead of 'if-else' or 'match' syntax

                if not name or priority not in priorities:
                    print("\nError >>>> Task name and priority must be valid\n")
                    continue

                    # new tasks are marked as 'new' in their 'status' property
                current_list.add_task(
                    Task("New", name, description, priorities[priority])
                )
                print("\nTask created successfully.\n")

            # ==== Edit a task ====
            elif action == 2:
                if not current_list.tasks:
                    print("\nError >>>> This list has no tasks\n")
                    continue

                task_index = get_valid_choice(
                    input("Enter task ID to edit: "), len(current_list.tasks)
                )
                if task_index is None:
                    print("\nError >>>> Invalid task ID\n")
                    continue
                task_index -= 1

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

                task_index = get_valid_choice(
                    input("Enter task ID to remove: "), len(current_list.tasks)
                )
                if task_index is None:
                    print("\nError >>>> Invalid task ID\n")
                    continue
                task_index -= 1

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

            # ==== Mark a task ====
            elif action == 4:
                pass



        # ==== Remove list ====
        elif action == 3:
            list_id = get_valid_choice(
                input("Enter list ID to remove: "), len(task_lists)
            )
            if list_id is None:
                print("\nError >>>> Invalid list ID\n\n")
                continue
            list_id -= 1

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
