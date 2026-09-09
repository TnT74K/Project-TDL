import csv


class Task:
    def __init__(self, name, pirority, description):  # Constructor
        self.name = name
        self.description = description
        self.pirority = pirority


class ToDoList:
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = []
        self.tasks = tasks


    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        try:
            self.tasks.remove(task)

        except ValueError:
            print("Already removed!")

    def show_all(self):
        i = 1
        print(f"""\n ==== To-Do List: "{self.name}" ==== \n""")
        for task in self.tasks:
            print(f"{i}. | {task.name} | {task.pirority} | {task.description}")
        print(f" ==== ++++ ==== \n")

    def save(
        self,
    ):
        with open(f"../storage/{self.name}.csv", "w", newline="") as file:
            writer = csv.writer(file)

    def load(
        self,
    ):
        with open(f"/storage/{self.name}.csv", "r", newline="") as file:
            reader = csv.reader(file)
