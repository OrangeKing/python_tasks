#!/usr/bin/env python

from os import system
from termcolor import cprint
import colorama

colorama.init()

def printMenu():
    menu_items = ["1 - Create task", "2 - Remove task", "3 - Set priority", \
    "4 - Display sorted by priority", "5 - Display sorted by name"]

    print("Select an action to perform:\n ")
    for item in menu_items:
        print(item)

def createTask():
    pass # TODO

def removeTask():
    pass # TODO

def setPriority():
    pass # TODO

def displayByPriority():
    pass # TODO

def displayByName():
    pass # TODO

def defaultAction():
    system('clear')
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
            actions.get(select, defaultAction)()
main()

#Task item structure
#Task done/undone
#Tasks priority
#Display task format?
#Display sorted by priority
#Display sort by name
#Remove task
