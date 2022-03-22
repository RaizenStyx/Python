# Filename: ex010.py
# Name: Dan H. Perry
# Username: dhperry
# Course and Section: CITC 1301 A02
# Assignment: Ex010
# Due Date: Today
# Description: input from keyboard

def main():
    name = input('Enter a name: ')
    age = int(input('Enter your age: '))
    # age = input('Enter your age: ')
    # age = int(age)
    cookies = float(input("How many cookies? "))
    print(f'{name} is {age}')
    print(type(name))
    print(type(age))
    print(f'{cookies} cookies')
    print(type(cookies))


main()



