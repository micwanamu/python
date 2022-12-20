import string
print('hat' == 'hat')
print('Hat' == 'hat')

print(string.ascii_lowercase)  # prints all lowercase
print(string.ascii_uppercase)  # prints all uppercase
print(string.digits)  # prints all digits

# ord function returns the unicode number
print(ord('H'))
print(ord('h'))
print(ord('c'))
print(ord('ł'))
print(ord('l'))

# returns true or false, checks the relationship between two items
x = isinstance(5, int)
print(x)

number1 = 5.0
if isinstance(number1, int):
    print("Yes")
else:
    print("No")

# Ternary operator
number2 = 6
print("Yes") if isinstance(number2, int) else print("No")

s1 = "Hi there!"
# don't modify the string
print(s1.upper())
print(s1.lower())

s2 = "hELLO AND WELCOME"
print(s2.capitalize())  # first word starts from uppercase, rest lowercase

s3 = "he lives in poznan"
print(s3.title())  # all words start from uppercase

s4 = "   he lives     in  Poznan   "
print(s4.strip())  # deletes white spaces from the beginning and end

s5 = "he lives in Poznan"
print(s5.strip('n'))  # deletes the provided character at the end
# deletes the provided characters from the beginning and end
print(s5.strip('nha'))

print(s5.lstrip('nha'))  # left strip, removes only from the left side
print(s5.rstrip('nha'))  # right strip, removes only from the right side

# prints the position of the first occurrence of the character in the string
print(s5.find('i'))
print(s5.find('x'))  # print -1 if the character is not found
print(s5.index('i'))  # same function as find()


print(s5.replace('i', 'B'))  # replaces all
print(s5.replace('i', 'B', 1))  # replaces the first occurrence
print(s5.replace('i', ''))  # removes all instances of i
