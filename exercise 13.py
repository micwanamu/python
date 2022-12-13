'''
Exercise 13
Write a program, your task is to enter 3 positive integers x, y, z, calculate and print the least number among them
Use input() function and conditionals.
INPUT: int
OUTPUT: int
'''

x = int(input('Enter the first integer number'))
y = int(input('Enter the second integer number'))
z = int(input('Enter the third integer number'))

if x == y == z:
    print("All of your numbers are equal.", x, y, z)
elif x < y and x < z:
    print(x)
elif x == y:
    print("Two of your numbers are equal.", x, y)
elif x == z:
    print("Two of your numbers are equal.", x, z)
elif y < x and y < z:
    print(y)
elif y == x:
    print("Two of your numbers are equal.", y, x)
elif y == z:
    print("Two of your numbers are equal.", y, z)
elif z < x and z < y:
    print(z)
elif z == y:
    print("Two of your numbers are equal.", z, y)
elif z == x:
    print("Two of your numbers are equal.", z, x)
