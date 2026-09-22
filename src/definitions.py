import csv
from pathlib import Path


STORAGE_DIR = Path(__file__).resolve().parent / "storage"


class Task:
    def __init__(self, status, name, description, pirority):  # Constructor
        self.status = status
        self.name = name
        self.description = description
        self.pirority = pirority


class ToDoList:
    def __init__(self, name, tasks, id):
        self.name = name
        self.tasks = []
        self.tasks = tasks
        self.id = id  # This is needed to have To-do lists with emoji \
        # \ or special characters in their name.

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        try:
            self.tasks.remove(task)

        except ValueError:
            print("Already removed!")

    def show_all_tasks(self):
        print(f"""\n ==== To-Do List: "{self.name}" ==== \n""")
        for i, task in enumerate(self.tasks):

            # To show task status using "x" as "Done", and " " as "Unfinished"
            status_holder = " " if task.status == "New" else "✅" 

            pirority_color = "🔵" if task.pirority == "Low" else "🟡" if task.pirority == "Medium" else "🔴"

            print(f"{i + 1}. [{status_holder}] | {task.name} | {pirority_color} {task.pirority} | {task.description}")
        print(f" ==== ++++ ==== \n")

    def save_tasks(self):
        with open(STORAGE_DIR / f"L-{self.id}.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["status", "name", "description", "pirority"])

            for task in self.tasks:
                task_holder = [task.status, task.name, task.description, task.pirority]
                writer.writerow(task)

    def load_tasks(self):
        with open(STORAGE_DIR / f"L-{self.id}.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                task = Task(row["status"], row["name"], row["description"], row["pirority"])
                self.tasks.append(task)


if __name__ == "__main__":
    print("This module is not meant to be run directly. Please run main.py instead.")