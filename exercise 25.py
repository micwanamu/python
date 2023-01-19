'''
Exercise 25
Your task is to swap the values of x and y. 

INPUT: int
x = 3 y = 2
OUTPUT: int
x = 2 y = 3

use temporary variable, not tuple method

'''

x = 3
y = 2

print('Changing variables...')
# Variables are swapped
swap_var = x
x = y
y = swap_var

# Printed
print(x)
print(y)
