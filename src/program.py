print("\n\n")
from definitions import ToDoList
from definitions import Task

import csv


def load_lists():
    lists = []  # To save all to-do lists in a list of ToDoList objects

    with open("storage/Lists.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:  # read all to-do lists from csv
            tasks = []  # To save all tasks within a to-do list
            current_list = ToDoList(row["name"], tasks, row["ID"])
            lists.append(current_list)

            with open(f"storage/L-{current_list.id}.csv") as file:
                task_reader = csv.DictReader(file)

                for row in task_reader:  # read all tasks witing a specific to-do list
                    task = Task(row["name"], row["description"], row["pirority"])
                    current_list.tasks.append(task)

    return lists


def save_lists(lists):
    with open("storage/Lists.csv", "w", newline="") as lists_file:
        list_writer = csv.writer(lists_file)
        list_writer.writerow(["ID", "name"])  # Write headers

        for current_list in lists:
            list_writer.writerow([current_list.id, current_list.name])
            with open(
                f"storage/L-{current_list.id}.csv", "w", newline=""
            ) as list_tasks_file:
                task_writer = csv.writer(list_tasks_file)
                task_writer.writerow(
                    ["name", "description", "pirority"]
                )  # Write headers

                for task in current_list.tasks:
                    task_writer.writerow([task.name, task.description, task.pirority])
    print("Done!")


to_do_lists = load_lists()
# print(to_do_lists[0].tasks[0].description)
test_tasks = [
    Task("Physics", "Do 100 tests", "high"),
    Task("Chemistry", "Finish a self-exam", "medium"),
    Task("Math", "Watch the online course", "low"),
]

to_do_lists.append(ToDoList("Konkour Study", test_tasks, 2))

save_lists(to_do_lists)
