# Filename: ex010.py
# Name: Dan H. Perry
# Username: dhperry
# Course and Section: CITC 1301 A02
# Assignment: Ex010
# Due Date: Today
# Description: input from keyboard

def main():

    name = input("Enter a name: ")
    length = len(name)
    print("The length is ", length)
    r = name.lower()
    print(f'Name in lower case is {r}')
    r = name.upper()
    print(f'Name in upper case is {r}')
    r = name.title()
    print(f'Name in title case is {r}')





main()



