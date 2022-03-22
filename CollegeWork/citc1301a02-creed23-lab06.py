# Filename: citc1301a02-creed23-lab06.py
# Name: Connor Reed
# Username: creed23
# Course and Section: CITC 1301 A02
# Assignment: Lab06
# Due Date: Feb 06 2020
# Description: Formatting



def main():
    int1 = 2
    int2 = 11
    Float1 = 3.4567
    Float2 = 12.345678
    String1 = "Not much of a cheese shop"
    String2 = "Where the finest in the land"

    print(f'The first integer is {int1}')
    print(f'The first integer is {int1} and the second is {int2}')


    print(f'{int1:>10d}{int2:>10d}')



    print(f'{Float1:>10.2f}{Float2:>10.2f}')
    print(f'{Float1:>10.3f}{Float2:>10.3f}')

    print(String1)
    print(f'{String2:>31s}')









main()