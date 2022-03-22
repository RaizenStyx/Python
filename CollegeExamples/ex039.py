# Filename: ex030.py
# Name: Dan H. Perry
# Username: dhperry
# Course and Section: CITC 1301 A02
# Assignment: Ex030
# Due Date: Today
# Description: for loop

import math

def main():

    print(f'Degrees  Radians   Sine   Cosine')
    for degree in range(0,91,5):
        rad = math.radians(degree)
        sine = math.sin(rad)
        cosine = math.cos(rad)
        print(f'{degree:6d}{rad:10.2f}{sine:8.3f}{cosine:8.3f}')




main()



