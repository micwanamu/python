import sys
import re
inFile = open('testfile.txt', 'r', encoding='utf-8')
stuff = inFile.read()
inFile.close()
lines = stuff.split('\n')  # split into lines
# print lines and lengths
for line in lines:
    print(f'{line}, : {len(line)} characters')

inFile = open('testfile.txt', 'r', encoding='utf-8')
lines = inFile.readlines()
inFile.close()  # muy importante!!!
for line in lines:
    print(f'{line}, : {len(line)} characters')

# another way to open a file
# no need to close the file in this situation because of the with
with open('testfile.txt', 'r') as inFile:
    lines = inFile.readlines()
    for line in lines:
        print(f'{line}, : {len(line)} characters')

with open('testfile.txt', 'r') as inFile:
    lines = inFile.read().splitlines()
    for line in lines:
        print(f'{line}, : {len(line)} characters')
# writing to file is the same, but with a 'w' mode and outFile.write('text...')

try:
    a = int(input('Enter the integer number \'a\': ... '))
    b = int(input('Enter the integer number \'b\': ... '))
    num = a / b
    print(f'The result of division {a} / {b} = {num}')
    print('Writing the results to file...')
    file = open('testfile.txt', 'a', encoding='utf-8')
    file.write(f'\nThe result of division {a} \ {b} = {num}')
except ValueError:
    print('You didn\'t enter a valid number!')
except ZeroDivisionError:
    print('You can\'t divide by 0!')
except FileNotFoundError:
    print('File doesn\'t exist')
except:
    print('Something went wrong...')
else:
    print('File is closed.')
finally:  # executed no matter what
    file.close()

try:
    a = int(input('Enter the integer number \'a\': ... '))
    b = int(input('Enter the integer number \'b\': ... '))
    num = a / b
    print(f'The result of division {a} / {b} = {num}')
    print('Writing the results to file...')
    ############
    with open('testfile.txt', 'a', encoding='utf-8') as file:
        file.write(f'\nThe result of division {a} / {b} = {num}')
    ############
except ValueError:
    print('You didn\'t enter a valid number!')
except ZeroDivisionError:
    print('You can\'t divide by 0!')
except FileNotFoundError:
    print('File doesn\'t exist')
except:
    print('Something went wrong...')
else:
    print('File is closed.')
finally:  # executed no matter what
    file.close()

# REGULAR EXPRESSIONS

if re.search('ab', sys.argv[1]):
    print('a match')
else:
    print('no match')

# test with acb; one characters
if re.search('a.b', sys.argv[1]):
    print('a match')
else:
    print('no match')

# test with accb; two characters
if re.search('a..b', sys.argv[1]):
    print('a match')
else:
    print('no match')

# * = any amount of characters (can be also 0)
if re.search('a*b', sys.argv[1]):
    print('a match')
else:
    print('no match')

# elements which start with abc
if re.search('^abc', sys.argv[1]):
    print('a match')
else:
    print('no match')

if re.search('[a-d]', sys.argv[1]):
    print('a match')
else:
    print('no match')

# a b or c at the beginning of a string
if re.search('^[abc]', sys.argv[1]):
    print('a match')
else:
    print('no match')

# every match except for a b or c
if re.search('[^abc]', sys.argv[1]):
    print('a match')
else:
    print('no match')

# every match except for a b or c at the beginning
if re.search('^[^abc]', sys.argv[1]):
    print('a match')
else:
    print('no match')

# returns a match for any two-digit numbers from 00 and 52 - with exceptions
if re.search('[0-5][0-2]', sys.argv[1]):
    print('a match')
else:
    print('no match')

# returns a match if any of the following characters are in the string
# excludes a through d and f (but e is ok :))
if re.search('[a-df]', sys.argv[1]):
    print('a match')
else:
    print('no match')

# excludes a through d and A through D
if re.search('[a-dA-D]', sys.argv[1]):
    print('a match')
else:
    print('no match')

# string ends with ba, ca, da, ea
if re.search('[b-e]a$', sys.argv[1]):
    print('a match')
else:
    print('no match')

# returns for any word that ends with a
if re.search('[b-z]a$', sys.argv[1]):
    print('a match')
else:
    print('no match')
