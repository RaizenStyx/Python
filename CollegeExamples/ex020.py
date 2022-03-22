# Filename: ex010.py
# Name: Dan H. Perry
# Username: dhperry
# Course and Section: CITC 1301 A02
# Assignment: Ex010
# Due Date: Today
# Description: input from keyboard

import math

def main():
    degree = 30
    rad = math.radians(degree)
    sine = math.sin(rad)
    cosine = math.cos(rad)
    arcsine = math.asin(sine)
    print(f'Degrees = {degree}')
    print(f'Radians = {rad:<8.2f}')
    print(f'Sine = {sine:<8.2f}')
    print(f'Sine = {sine:<8.5f}')
    print(f'Sine = {sine}')
    print(f'Cosine = {cosine:<8.2f}')
    print(f'Arcsine = {arcsine:<8.2f}')
    rad = round(rad,1)
    print(f'Radians = {rad:<8.5f}')
    rnd = round(12345.65001,-2)
    print(f'rounding = {rnd}')


main()



