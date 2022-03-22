# Filename: ex030.py
# Name: Dan H. Perry
# Username: dhperry
# Course and Section: CITC 1301 A02
# Assignment: Ex030
# Due Date: Today
# Description: for loop

import math

def main():

    y = int(input('Enter the number: '))
    for x in range(y):
        for a in range(y,x,-1):
            print(f' ', end='')

        for z in range(x+1):
            print('*',end='')
        print()



main()



