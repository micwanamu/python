'''

Exercise 01, file pp_01.py
Write a function named fizz_buzz(num) that will return the string 'Fizz' if the num parameter  is divisible by 3,
will return the string 'Buzz' if the num is divisible by '5',
will return the string 'FizzBuzz' if the num is divisible by 3 and 5
will return num for any other number
Function should include docstring
Program should implement entering the number many times  during runtime. Typing "q"  should cause quitting the program.


'''


def fizz_buzz(num):
    '''
    Enter a number and the function will:
    return 'Fizz" if the num is divisible by 3,
    return 'Buzz' if the num is divisible by 5,
    return 'FizzBuzz' if the num is divisible by 3 and 5,
    return the number for any other number
    Enter 'q' if you want to quit the program.
    '''

    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)


userinput = input('Enter any number or enter q to exit program...')
if userinput == 'q':
    print("Quitting...")
    quit()
else:
    fizz_buzz(int(userinput))
