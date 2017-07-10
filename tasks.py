#!/usr/bin/env python

#utility import
from os import system
from termcolor import cprint,colored
import colorama

#coloring support (for priorities & errors)
colorama.init()

#global task 'vector'
#tasks = []

#primitive ui
def printMenu():
    menu_items = ["1 - Create task", "2 - Remove task", "3 - Set priority", \
    "4 - Display sorted by priority", "5 - Display sorted by name"]
    print("Select an action to perform:\n ")
    for item in menu_items:
        print(item)

    print("q - quit program\n ")


def createTask(task_list):
    current_task = []

    name = (raw_input("Task name: ")).lower()
    current_task.append(name)

    try:
        priority = int(raw_input("Select priority (1-low 2-medium 3-high): "))
    except ValueError:
        print("Setting default priority as 0")
        priority = 0

    current_task.append(priority)
    task_list.append(current_task)

def removeTask(task_list):
    try:
        task_done = raw_input("Select a task to be completed/removed: ")
        for i,tsk in enumerate(task_list):
            for j,name in enumerate(tsk):
                if name == task_done:
                    print(colored("NAME: " + tsk[0] + " PRIORITY: "\
                     + str(tsk[1]),"blue") + " has been deleted\n")

                    task_list.remove(tsk)

    except ValueError:
        print("Please give proper values")
        pass

def setPriority(task_list):
    try:
        task_modified = raw_input("Select a task to be modified: ")
        for i,tsk in enumerate(task_list):
            for j,name in enumerate(tsk):
                if name == task_modified:
                    priority_modified = int(raw_input("Select new priority: "))
                    print(colored("NAME: " + task_list[task_list.index(tsk)][0],"blue") + " has now priority: "\
                     + colored(str(priority_modified),"red") + "\n")

                    task_list[task_list.index(tsk)][1] = priority_modified

    except ValueError:
        print("Please give proper values")
        pass

def displayByPriority(task_list):
    print("Current tasks:")
    for task in sorted(task_list,key=lambda x: x[1],reverse=True):
        if task[1] == 1:
            priorityColor = "green"
            priorityValue = "low"
        elif task[1] == 2:
            priorityColor = "yellow"
            priorityValue = "medium"
        elif task[1] >= 3:
            priorityColor = "red"
            priorityValue = "high"
        else:
            priorityColor = "blue"
            priorityValue = "unspecified"
        cprint("NAME: " + task[0] + " PRIORITY: " + priorityValue,priorityColor)

def displayByName(task_list):
    print("Current tasks:")
    for task in sorted(task_list,key=lambda x: x[0]):
        cprint("NAME: " + task[0] + " PRIORITY: " + str(task[1]),"blue")

def defaultAction():
    cprint("No such action available!\n", "red")
    pass

def main():
    actions = {"1": createTask, "2": removeTask, "3": setPriority, "4": displayByPriority, "5": displayByName}
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
    main()
