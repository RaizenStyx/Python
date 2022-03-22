# Filename: citc1301a02-creed23-lab14.py
# Name: Connor Reed
# Username: creed23
# Course and Section: CITC 1301 A02
# Assignment: Lab14
# Due Date: 25 02 2020
# Description: For loop lab2


def main():
    start = int(input('Input Starting Number:'))
    end = int(input('Input Ending Number:'))
    y=end-start+1
    zero=0
    for x in range(y):
        zero=zero+start
        start=start+1


    print(zero)

main()