print("\n\n")
import definitions
import csv


def load_lists():
    with open("storage/Lists.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


load_lists()
