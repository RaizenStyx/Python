# Filename: ex010.py
# Name: Dan H. Perry
# Username: dhperry
# Course and Section: CITC 1301 A02
# Assignment: Ex010
# Due Date: Today
# Description: for loop

import math

def main():
    print(f'    x      y')
    for x in range(-15,11):  # calculate table x squared
        y = x*x
        print(f'{x:6d}{y:6d}')
        # end of range() loop
    print(f'{x} After the for loop')


main()



