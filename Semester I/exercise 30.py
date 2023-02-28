'''
Exercise 30 (modify exercise 25)
Write a program that swaps the values of x and y. For this purpose create a function 
swap_two_values(x:int, y:int)->None. 

INPUT: int x, y
OUTPUT: int
e.g., x = 2, y = 3

use f-string, function, invoke the function with examplary data
'''


def swap_values(x, y):
    swap_var = x
    x = y
    y = swap_var
    print(
        f'The values x and y have been swapped. x is now {x} and y is now {y}.')


x = 3
y = 2
print(f'x is {x} and y is {y}.')
swap_values(x, y)
