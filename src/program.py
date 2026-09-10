print("\n\n")
from definitions import *
from list_manager import *

task_lists = load_lists()
number_of_lists = len(task_lists)

print("Welcome to your To-Do list app!")
while True:
    print(
        f"""You have {number_of_lists} lists. \ndefault list: "{task_lists[0].name}"\n"""
    )

    menu = (
        "\n      1. Show lists"
        "\n      2. Show default tasks"
        "\n      3. Save lists"
        "\n      4. Exit Program"
    )

    menu_lines = menu.count("\n")

    print("==== Menu ====" "\n Actions:" f"{menu}")

    user_input = input("Enter item index to continue: ")

    try:
        choice = int(user_input)
    except (TypeError, ValueError):
        choice = None

    if choice is None or choice < 1 or choice > menu_lines:
        print("\nError >>>> Invalid input\n\n")
        continue
    elif choice == 1:
        print("\n\n")
        for i, task_list in enumerate(task_lists):
            print(f"{i + 1}. {task_list.name}")
        print("\n\n")

    elif choice == 2:
        task_lists[0].show_all()

    elif choice == 3:
        save_lists(task_lists)

    elif choice == 4:
        print("\n\nExiting program...")

    exit()
