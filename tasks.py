#!/usr/bin/env python2
"""Command-line task manager"""
import json
from os import system
import colorama
from termcolor import colored, cprint

# Coloring support (for priorities & errors)
colorama.init()


class Task(object):
    """Task representation"""
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority


class AvailSaveFormat(Exception):
    """Exception for unavailable file formats for saving"""
    pass


def print_menu():
    """Display menu to the user"""
    menu_items = ["1 - Create task", "2 - Remove task", "3 - Set priority",
                  "4 - Display by priority", "5 - Display by name",
                  "6 - Save to a file", "7 - Read from a file\n"]
    print("Select an action to perform:\n ")
    for item in menu_items:
        print(item)

    print("q - quit program\n ")


def create_task(task_list):
    """Parse user input to create task object"""
    try:
        name = (raw_input("Task name(max 20 characters): "))[:20].lower()

        name_multiplier = 0
        for tsk in task_list:
            if tsk.name == name:
                name_multiplier += 1
        if name_multiplier > 0:
            name += "(" + str(name_multiplier) + ")"
        else:
            pass

    except ValueError:
        print("Please give proper values")

    try:
        priority = int(raw_input("Select priority (1-low 2-medium 3-high): "))

    except ValueError:
        print("Setting default priority as 0")
        priority = 0

    current_task = Task(name, priority)
    task_list.append(current_task)


def remove_task(task_list):
    """Remove task from the list of given name"""
    try:
        task_done = raw_input("Select a task to be completed/removed: ")
        for tsk in task_list:
            if tsk.name == task_done:
                print(colored("NAME: " + tsk.name + " PRIORITY: " +
                              str(tsk.priority), "blue") + " deleted\n")
                task_list.remove(tsk)

    except ValueError:
        print("Please give proper values")


def set_priority(task_list):
    """Set priority of given task to given value"""
    try:
        task_modified = raw_input("Select a task to be modified: ")
        for tsk in task_list:
            if tsk.name == task_modified:
                priority_modified = int(raw_input("Select new priority: "))
                print(colored("NAME: " + task_list[task_list.index(tsk)].name,
                              "blue") + " has now priority: " +
                      colored(str(priority_modified), "red") + "\n")

                task_list[task_list.index(tsk)].priority = priority_modified

    except ValueError:
        print("Please give proper values")


def display_by_priority(task_list):
    """Display tak list ordered by priority values"""
    print("Current tasks:")
    for task in sorted(task_list, key=lambda x: x.priority, reverse=True):
        if task.priority == 1:
            priority_color = "green"
            priority_value = "low"
        elif task.priority == 2:
            priority_color = "yellow"
            priority_value = "medium"
        elif task.priority >= 3:
            priority_color = "red"
            priority_value = "high"
        else:
            priority_color = "blue"
            priority_value = "unspecified"
        cprint("NAME: " + task.name + " PRIORITY: " +
               priority_value, priority_color)


def display_by_name(task_list):
    """Display tak list ordered by name"""
    print("Current tasks:")
    for task in sorted(task_list, key=lambda x: x.name):
        cprint("NAME: " + task.name + " PRIORITY: " +
               str(task.priority), "blue")


def save_to_file(task_list):
    """Save to file of selected type"""
    try:
        f_type = raw_input("Select filetype to save (txt/json): ")
        if f_type == "txt":
            with open("tasks.txt", "w") as outfile:
                for task in task_list:
                    outfile.write(task.name + "\n" + str(task.priority) + "\n")
        elif f_type == "json":
            with open('data.json', 'a') as outfile:
                for task in task_list:
                    json.dump({"name": task.name, "priority": task.priority},
                              outfile)
        else:
            raise(AvailSaveFormat)
        print("Tasklist saved in " + colored("tasks." + f_type, "red"))

    except AvailSaveFormat:
        cprint("No such format available!\n", "red")


def read_from_file(task_list):
    """Read from a file of selected type"""
    try:
        filename = raw_input("Enter name of file to be read from:")
        with open(filename, "r") as infile:
            while True:
                name = infile.readline().rstrip()
                priority = infile.readline().rstrip()
                if not priority:
                    break
                task_list.append(Task(name, int(priority)))
        print("Tasklist read from " + colored("tasks.txt!", "green"))

    except IOError:
        cprint("No such file available!\n", "red")


def default_action(*_):
    """Default action if no menu element is selected"""
    cprint("No such action available!\n", "red")


def main():
    """Main app function"""
    actions = {"1": create_task, "2": remove_task, "3": set_priority,
               "4": display_by_priority, "5": display_by_name,
               "6": save_to_file, "7": read_from_file}
    task_list = []

    while True:
        print_menu()
        select = raw_input("\nSelect an option: ")

        if select == "q":
            break
        else:
            system('clear')
            actions.get(select, default_action)(task_list)

if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        system('exit')

    except EOFError:
        system('exit')
