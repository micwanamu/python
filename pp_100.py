'''
Exercise 100, file pp_100.py
Write a program that computes the value of n factorial - n!
Use iterative implementation
Expected results
-10! => ERROR
0! = 1
1! = 1
2! = 1 * 2 = 2
3! = 1 * 2 * 3 = 6
4! = 1 * 2 * 3 * 4
10! = 3628800
32! = 263130836933693530167218012160000000
n! = 1 * 2 * 3 * .... * n

'''


def factorial(n: int) -> int:
    factorio = 1
    for i in range(1, n + 1):
        factorio = factorio * i

    return factorio


number = int(input("enter an integer to calculate the factorial: "))
number = factorial(number)
print(number)
