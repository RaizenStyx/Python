# Filename: ex030.py
# Name: Dan H. Perry
# Username: dhperry
# Course and Section: CITC 1301 A02
# Assignment: Ex030
# Due Date: Today
# Description: for loop

import math

def main():

    print(f'degrees    radians')
    for x in range(0,91,5):  # print one char/ line
        rad = math.radians(x)
        print(f'{x:6d}{rad:12.3f}')

    print(f'{x} After the for loop')


main()



