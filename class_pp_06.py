# Exceptions

# 01, Index Error
# numbers = [1,2,3]
# print(numbers[3])
# print('here i am')

# 02, TypeError
# L = [1,7,4]
# print(int(L))

# 03, TypeError
# print('a'/4)

# 04, NameError
# print(a)

# 05, ValueError
# num = int(input('Enter the integer number:...'))
# print(f'Our number is {num}')

# 06, IOError -> FileNotFoundError
# file = open('ztest.py')
# print('File is opened')
# file.close

# 07, FileNotFoundError, IndexError
# file = open('test.py')
# number = [1,2,3]
# print(numbers[3])
# print('File is opened')
# file.close()

# Handling exceptions

# IndexError
try:
    numbers = [1, 2, 3]
    print(numbers[3])
    print('Here I am not')
except IndexError:
    print('Whoops.')  # program not terminated

# ValueError
try:
    num = int(input('Enter the integer number:...'))
    print(f'Our number is {num}')
except ValueError:
    print('You didn\'t input a valid number')

# ValueError a,1,0

try:
    a = int(input('Enter the number \'a\':...'))
    b = int(input('Enter the number \'b\':...'))
    num = a/b
    print(f'The result of division {a} / {b} = {num}')
except ValueError:
    print('Not a valid number.')

# ValueError, ZeroDivisionError
try:
    a = int(input('Enter the number \'a\':...'))
    b = int(input('Enter the number \'b\':...'))
    num = a/b
    print(f'The result of division {a} / {b} = {num}')
except ValueError:
    print('Not a valid number.')
except ZeroDivisionError:
    print('You can\'t divide by 0!')

# raising as exception
'''
if a < 0 or b < 0:
    print('Enter positive int')
    # raise ValueError("You didn't enter the valid number.")
return a/b
'''

try:
    a = int(input('Enter the number \'a\':...'))
    b = int(input('Enter the number \'b\':...'))
    num = a/b
    print(f'The result of division {a} / {b} = {divide(a,b)}')
except ValueError as error:
    print(error)
except ZeroDivisionError:
    print('You can\'t divide by 0!')


try:
    a = int(input('Enter the number \'a\':...'))
    b = int(input('Enter the number \'b\':...'))
    assert a >= 0 and b >= 0  # criteria
    print(f"Division a / b = {a/b}")
except AssertionError:
    print("AssertionError occurred; numbers are not positive integers")
except ZeroDivisionError:
    print("Can't divide by 0")
except:
    print("Enter the correct int number")
else:  # executed when there are no exceptions
    print("Code without exceptions", end=' ')
    print(f"Multiplying a x b = {a*b}", end=' ')
    print('It is okay')
finally:
    print('The try... except block is finished. Always. Useful for cleaning up resources that are used in the try block')
