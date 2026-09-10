print("\n\n")
from definitions import *
from list_manager import *

to_do_lists = load_lists()
print(to_do_lists[0].tasks[0].description)

test_tasks = [
    Task("Physics", "Do 100 tests", "high"),
    Task("Chemistry", "Finish a self-exam", "medium"),
    Task("Math", "Watch the online course", "low"),
]

to_do_lists.append(ToDoList("Konkour Study", test_tasks, 2))

save_lists(to_do_lists)
