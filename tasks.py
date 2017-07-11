#!/usr/bin/env python2

# Utility import
from os import system
from termcolor import cprint, colored
import colorama

# Coloring support (for priorities & errors)
colorama.init()


class Task(object):
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority


# Primitive ui
def printMenu():
    menu_items = ["1 - Create task", "2 - Remove task", "3 - Set priority",
                  "4 - Display by priority", "5 - Display by name"]
    print("Select an action to perform:\n ")
    for item in menu_items:
        print(item)

    print("q - quit program\n ")


def createTask(task_list):
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
        pass

    try:
        priority = int(raw_input("Select priority (1-low 2-medium 3-high): "))

    except ValueError:
        print("Setting default priority as 0")
        priority = 0

    current_task = Task(name, priority)
    task_list.append(current_task)


def removeTask(task_list):
    try:
        task_done = raw_input("Select a task to be completed/removed: ")
        for tsk in task_list:
            if tsk.name == task_done:
                print(colored("NAME: " + tsk.name + " PRIORITY: " +
                      str(tsk.priority), "blue") + " has been deleted\n")
                task_list.remove(tsk)

    except ValueError:
        print("Please give proper values")
        pass


def setPriority(task_list):
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
        pass


def displayByPriority(task_list):
    print("Current tasks:")
    for task in sorted(task_list, key=lambda x: x.priority, reverse=True):
        if task.priority == 1:
            priorityColor = "green"
            priorityValue = "low"
        elif task.priority == 2:
            priorityColor = "yellow"
            priorityValue = "medium"
        elif task.priority >= 3:
            priorityColor = "red"
            priorityValue = "high"
        else:
            priorityColor = "blue"
            priorityValue = "unspecified"
        cprint("NAME: " + task.name + " PRIORITY: " +
               priorityValue, priorityColor)


def displayByName(task_list):
    print("Current tasks:")
    for task in sorted(task_list, key=lambda x: x.name):
        cprint("NAME: " + task.name + " PRIORITY: " +
               str(task.priority), "blue")


def defaultAction(task_list):
    cprint("No such action available!\n", "red")
    pass


def main():
    actions = {"1": createTask, "2": removeTask, "3": setPriority,
               "4": displayByPriority, "5": displayByName}
    task_list = []

    while True:
        printMenu()
        select = raw_input("\nSelect an option: ")

        if select == "q":
            break
        else:
            system('clear')
            actions.get(select, defaultAction)(task_list)

if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        system('exit')

    except EOFError:
        system('exit')
