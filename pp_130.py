'''
Exercise 130, file: pp_130.py

Write a program that will summarize the digits of the given number

In this aim implement the function
get_sum(num:int)->int:

Use recursive implementation
Remind yourself: n%10, n//10
'''


def get_sum(n: int) -> int:
    '''
    The function takes an integer as input and returns the sum of its digits.

    Parameters:
        n: any positive int number
    Returns:
        the sum of the number digits
    '''
    if n == 0:
        return 0
    else:
        return n % 10 + get_sum(int(n//10))


num = int(input("enter an integer to calculate the sum of its digits: "))
result = get_sum(num)
print(f' The sum of digits in {num} is {result}')
