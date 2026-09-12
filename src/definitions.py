import csv


class Task:
    def __init__(self, name, description, pirority):  # Constructor
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
            print(f"{i + 1}. | {task.name} | {task.pirority} | {task.description}")
        print(f" ==== ++++ ==== \n")

    def save_tasks(self):
        with open(f"../storage/L-{self.id}.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["name", "description", "pirority"])

        for task in self.tasks:
            task_holder = [task.name, task.descriptions, task.pirority]
            writer.writerow(task)

    def load_tasks(self):
        with open(f"/storage/L-{self.id}.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                task = Task(row[0], row[1], row[2])
                self.tasks.append(task)


if __name__ == "__main__":
    print("This module is not meant to be run directly. Please run main.py instead.")