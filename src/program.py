print("\n\n")
from definitions import ToDoList
from definitions import Task

import csv


def load_lists():
    lists = []  # To save all to-do lists in a list of ToDoList objects
    
    with open("storage/Lists.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader: # read all to-do lists from csv
            tasks = []  # To save all tasks within a to-do list
            current_list = ToDoList(row["name"], tasks, row["ID"])
            lists.append(current_list)

            with open(f"storage/L-{current_list.id}.csv") as file:
                task_reader = csv.DictReader(file)

                for row in task_reader: # read all tasks witing a specific to-do list
                    task = Task(row["name"], row["description"], row["pirority"])
                    current_list.tasks.append(task)

    return lists
        


to_do_lists = load_lists()
print(to_do_lists[0].tasks[0].description)
