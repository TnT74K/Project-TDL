import csv
file = open("/storage/file.csv", "r", newline="")
reader = csv.reader(file)

class Task():
    def __init__(self, name, pirority, description): # Constructor
        self.name = name
        self.pirority = pirority
        self.description = description

class ToDoList():
    def __init(self, name, tasks):
        self.name = name
        self.tasks = []
        self.tasks = tasks

    def __str__(self):
        i = 1
        print(f'''\n ==== To-Do List: "{self.name}" ==== \n''')
        for task in self.tasks:
            print(f"{i}. | {task.name} | {task.pirority} | {task.description}")
        print(f" ==== ++++ ==== \n")


    def add_task(self, task):
        self.tasks.append(task)


    def remove_task(self, task):
        try:
            self.tasks.remove(task)

        except ValueError:
            print("Already removed!")

    def show_all(self):
        print(self)


    def save(self, ):
        


    def load(self,):

    