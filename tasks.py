#!/usr/bin/env python

#utility import
from os import system
from termcolor import cprint,colored
import colorama

#coloring support (for priorities & errors)
colorama.init()

#global task 'vector'
tasks = []

#primitive ui
def printMenu():
    menu_items = ["1 - Create task", "2 - Remove task", "3 - Set priority", \
    "4 - Display sorted by priority", "5 - Display sorted by name"]
    print("Select an action to perform:\n ")
    for item in menu_items:
        print(item)

def createTask():
    global tasks
    name = raw_input("Task name: ")
    tasks.append(name)
    pass # TODO

def removeTask():
    print(colored(tasks.pop(),"blue") + " task has been deleted\n")
    pass # TODO

def setPriority():
    pass # TODO

def displayByPriority():
    print("Current tasks:")
    for task in tasks:
        cprint(task,"blue")
    pass # TODO

def displayByName():
    print("Current tasks:")
    for task in sorted(tasks):
        cprint(task,"blue")
    pass # TODO

def defaultAction():
    cprint("No such action available!\n", "red")
    pass

def main():
    actions = {"1": createTask, "2": removeTask, "3": setPriority, "4": displayByPriority, "5": displayByName}

    while True:
        printMenu()
        select = raw_input("\nSelect an option: ")

        if select == "q":
            break
        else:
            system('clear')
            actions.get(select, defaultAction)()
main()

#Tasks priority
#Display task format?
#Display sorted by priority
#Display sort by name
#Remove task
