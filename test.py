#
#
#
#
#
def main():

    x = input('Enter Name:')
    y = int(input('Enter Favorite Integer:'))
    z = float(input('Enter Favorite Decimal:'))
    print(f'this is a name: {x} this is a integer: {y} this is a float: {z}')

    print('Lets do some math!')
    a = y+z
    print(f'Fav Integer + Fav Decimal=',a)
    print(f"{a} is {x.title()}'s favorite number!")

    for c in range(y):
        y = c+y      # when y=5, its 5+0, 5+1, then y gets reassigned 6, then 6+2, 8+3, then 11+4
        print(y)

    if x.title() == "Connor":
        print('Hello Connor!')
    else:
        print('Hello Other Person!')
    if a == 10.0:
        print('Best number!')
    else:
        print(c)
    





main()