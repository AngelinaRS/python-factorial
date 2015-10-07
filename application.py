"Factorial"

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def reset():
    """This cleans the screen"""
    if os.name == ("posix"): #In Linux
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"): #In windows
        os.system("cls")
reset()

def factorial(number):
    """This creates the factorial of the any number"""
    if number <= 1: #If the number is lesser than "0" will return "1"
        return 1
    #If number is longer than "1" will elaborate the factorial of any number
    return number * factorial(number-1)

def minuscule(choose_user):
    """This converts the choose user in munuscule"""
    choose_user = choose_user.lower()
    return choose_user

def valid_number():
    """This verifies if the user inserted numbers"""

    reset()
    while True:
        number = raw_input(" -- Insert the number to see the factorial --  \n - ")
        try:
            number = int(number) #If the number is interger
            return number
        except ValueError:
            reset()
            print "Only can insert numbers"
    return number

def print_factorial():
    """This ask the number to show the factorial"""
    number = valid_number()
    print factorial(number)

def print_other_factorial():
    """This ask is want to see other number"""
    print_factorial()
    while True:
        choose_user = raw_input("\nDo you want to know the factorial of other number?  y/n  ")
        choose_user = minuscule(choose_user)
        if choose_user == "y":
            print_factorial()
        elif choose_user == "n":
            reset()
            menu()
        else:
            reset()
            print "Only can write -y- or -n-\n"


def menu():
    """This saves the menu"""
    #Show to the user the options
    print "Choose an option\n"
    print "Insert (1) to see the factorial"
    print "Insert (2) to exit"

    while True:

        choose_user = raw_input("- ")

        if choose_user == "1":
            print_other_factorial() #Call the function to show the factioal number

        elif choose_user == "2":
            reset()
            print "\n\nBye\n\n"
            sys.exit() #Exit the program

        else:
            reset()
            print "**Choose a valid option**\n"
            menu()

if __name__ == '__main__':
    menu()
