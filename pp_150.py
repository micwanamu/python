'''
Exercise 150, file pp_150.py (on the basis of exercie 100)
Write a program that computes the value of n factorial - n!
Use iterative implementation
Expected results
0! = 1
1! = 1
2! = 1 * 2 = 2
3! = 1 * 2 * 3 = 6
4! = 1 * 2 * 3 * 4
10! = 3628800
32! = 263130836933693530167218012160000000
n! = 1 * 2 * 3 * .... * n

In order to do it implement the function 
def factorial(n: int) -> int:

Improve error handling using exceptions
'''


def factorial(n: int) -> int:
    factorio = 1
    for i in range(1, n + 1):
        factorio = factorio * i

    return factorio


try:
    number = int(input("Enter an integer to calculate the factorial: "))
    assert number >= 0
except AssertionError:
    print("Negative numbers cannot make factorials.")
else:
    number = factorial(number)
    print(number)
