#In class work

# Variable in class work

x=10
y=20.5
print('X =',x)
print('Y =',y)
print(x,y)

# variables and such. This is called a comment

a= 'Spam'
b= 'Don\'t Panic'



print(a)
print(b)
# when a=b, it goes in order and when it sees it, it will make it be replaced
a=b
print(a)

# math time

a= 4.3
b= 6.9
c= a+b

print('a + b =', c)

# floating rounding errors
# floating point numbers have a certain range.
c= a-b
print('a - b =', c)
# redefined a and b. Use () when not sure about order of operations.
a= 3
b= 5
c=(a+b)*b
print('(a+b)*b=',c)

a=4.3
b=6
z='bill'
print('a',z,'b')
print(a,z,b)
# {} subistutes for the variables after .format the with : can use numbers and
# f for float s for string d for interger
print('{:6.4f}  {:15s}  {:5d}'.format(a,z,b))
#numbers are right alligned
a=24.7
b=478
z='graham'
print('{:6.4f}  {:15s}  {:10d}'.format(a,z,b))
