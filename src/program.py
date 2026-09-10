print("\n\n")
import re

from definitions import *
from list_manager import *


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

    menu = (
        "\n      1. Show lists"
        "\n      2. Show default tasks"
        "\n      3. Save lists"
        "\n      4. Exit Program"
    )

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

        print("\n ==== List Actions ====")
        print(
              "     1. Create new list"
            "\n     2. Open list"
            "\n     3. remove list"
            "\n     4. Back to main menu"
        )

        action = input("Enter item index to continue: ")
        if is_invalid(action, 4):
            continue
        action = int(action)

        if action == 1:
            name = input("Enter the new list name: ").strip()
            if not name:
                print("\nError >>>> List name cannot be empty\n\n")
                continue
            new_id = str(max(int(task_list.id) for task_list in task_lists) + 1)
            task_lists.append(ToDoList(name, [], new_id))

        elif action == 2:
            try:
                list_id = (
                    int(input("Enter list ID to open: ")) - 1
                )  # -1 is used because lis IDs in Python begin from 0
            except (TypeError, ValueError):
                list_id = -1
            if not 0 <= list_id < len(task_lists):
                print("\nError >>>> Invalid list ID\n\n")
                continue
            task_lists[list_id].show_all_tasks()

        elif action == 3:
            try:
                list_id = int(input("Enter list ID to remove: ")) - 1
            except (TypeError, ValueError):
                list_id = -1
            if not 0 <= list_id < len(task_lists):
                print("\nError >>>> Invalid list ID\n\n")
                continue
            task_lists.pop(list_id)

    # Show default tasks
    elif choice == 2:
        task_lists[0].show_all_tasks()

    # Save lists
    elif choice == 3:
        save_lists(task_lists)

    # Exit the program
    elif choice == 4:
        print("\n\nExiting program...")
        break
