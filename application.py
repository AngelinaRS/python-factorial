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

