import csv
from pathlib import Path

from definitions import *


STORAGE_DIR = Path(__file__).resolve().parent / "storage"


def load_lists():
    lists = []  # To save all to-do lists in a list of ToDoList objects

    with open(STORAGE_DIR / "Lists.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:  # read all to-do lists from csv
            tasks = []  # To save all tasks within a to-do list
            current_list = ToDoList(row["name"], tasks, row["ID"])
            lists.append(current_list)

            with open(STORAGE_DIR / f"L-{current_list.id}.csv") as file:
                task_reader = csv.DictReader(file)

                for row in task_reader:  # read all tasks witing a specific to-do list
                    task = Task(row["name"], row["description"], row["pirority"])
                    current_list.tasks.append(task)

    return lists


def save_lists(lists):
    with open(STORAGE_DIR / "Lists.csv", "w", newline="") as lists_file:
        list_writer = csv.writer(lists_file)
        list_writer.writerow(["ID", "name"])  # Write headers

        for current_list in lists:
            list_writer.writerow([current_list.id, current_list.name])
            with open(
                STORAGE_DIR / f"L-{current_list.id}.csv", "w", newline=""
            ) as list_tasks_file:
                task_writer = csv.writer(list_tasks_file)
                task_writer.writerow(
                    ["name", "description", "pirority"]
                )  # Write headers

                for task in current_list.tasks:
                    task_writer.writerow([task.name, task.description, task.pirority])
    print("Done!")

if __name__ == "__main__":
    print("This module is not meant to be run directly. Please run main.py instead.")