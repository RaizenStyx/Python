# Filename: ex030.py
# Name: Dan H. Perry
# Username: dhperry
# Course and Section: CITC 1301 A02
# Assignment: Ex030
# Due Date: Today
# Description: for loop

import math

def main():

    total = 0
    for x in range(4):  # print one char/ line
        numb = int(input('Enter a number: '))
        total = total + numb
        print(f'Running total {total}')

    print(f'Total {total}')


main()



