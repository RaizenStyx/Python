# Filename: citc1301a02-creed23-lab05.py
# Name: Connor Reed
# Username: creed23
# Course and Section: CITC 1301 A02
# Assignment: Lab05
# Due Date: Feb 06 2020
# Description: Simple Math


fname = input('Enter First Name:')
lname = input('Enter Last Name:')
email = input('Enter Email Address:')
phone = input('Enter Phone Number:')
favint = input('Enter Favorite Integer:')
favfl = input('Enter Favorite floating point number:')


print(f'Name:      {fname} {lname}')
print(f'email:     {email}')
print(f'Phone:     {phone}')
print(f'Integer:   {favint}')
print(f'Float:     {favfl}')


print(id(phone))
print(id(favint))
print(id(favfl))
print(type(phone))
print(type(favint))
print(type(favfl))

# Everything is a string because I used the f string function for it all so it was not
# unusual at all.


