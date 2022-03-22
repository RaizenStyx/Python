# Filename: ex030.py
# Name: Dan H. Perry
# Username: dhperry
# Course and Section: CITC 1301 A02
# Assignment: Ex030
# Due Date: Today
# Description: for loop

import math

def main():

    total = 0
    product = 1
    y = int(input('How many numbers to enter: '))
    for x in range(y):  # print one char/ line
        numb = int(input('Enter a number: '))
        total = total + numb
        product = product * numb
        #print(f'Running total {total}')

    print(f'Total {total}')
    average = total/y
    print(f'Average {average}')
    print(f'Product {product}')


main()



