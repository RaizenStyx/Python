# Filename: citc1301a02-creed23-lab17.py
# Name: Connor Reed
# Username: creed23
# Course and Section: CITC 1301 A02
# Assignment: Lab17
# Due Date: 19 03 2020
# Description: For loop lab4


def main():
    x = int(input('Enter Age: '))


    if x < 18 :
        print("You're too young to vote")
    if x < 65:
        print('You cannot retire yet')
    if x >= 65:
        print('Ready to hang it up?')
    if x == 0:
        print('Invalid age')





main()