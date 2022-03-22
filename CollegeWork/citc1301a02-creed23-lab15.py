# Filename: citc1301a02-creed23-lab15.py
# Name: Connor Reed
# Username: creed23
# Course and Section: CITC 1301 A02
# Assignment: Lab15
# Due Date: 25 02 2020
# Description: For loop lab3

import math

def main():
    radius = int(input('Please enter a radius in cm greater than 5: '))
    pi = math.pi
    print(f'   Radius Area           Circumference')
    for radius in range(5,radius+1):
        ar = math.pow(radius,2)
        x = pi*ar
        y = 2*pi*radius
        print(f'{radius:7d}{x:8.2f}{y:20.2f}')





main()