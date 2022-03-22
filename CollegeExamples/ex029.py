# Filename: ex010.py
# Name: Dan H. Perry
# Username: dhperry
# Course and Section: CITC 1301 A02
# Assignment: Ex010
# Due Date: Today
# Description: for loop

import math

def main():
    spam = 'Not much of a cheese shop'
    print(f'    x    char')
    for x in range(len(spam),0,-1):  # print one char/ line
        print(f'{x:6d} {spam[0:x]:30s}')
        # end of range() loop
    print(f'{x} After the for loop')


main()



