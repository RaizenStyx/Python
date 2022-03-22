# Filename: citc1301a02-creed23-lab16.py
# Name: Connor Reed
# Username: creed23
# Course and Section: CITC 1301 A02
# Assignment: Lab16
# Due Date: 27 02 2020
# Description: For loop lab4


import math
def main():
    y = int(input('Enter number of rows: '))
    for x in range(0,y):
        for a in range(x):
            print(' ',end='')
        for z in range(y+y-x,x+1,-1):
            print('*',end='')

        print('')




main()