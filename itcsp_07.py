var_01 = 3*4
print(var_01)
print(type(var_01))

print('concatenation')
print('ab' + 'bc')

# print('The result is:' + 2*2)  # can't concatenate different types
print('The result is: ' + str(2*2))

print('repetition')
print(3*'John')

# number of characters in the string, space is also a character!
print('the length function')
print(len('John'))
print(len('John '))

print('indexing from the left side')
print('John'[0])
print('John'[1])
print('John'[2])
print('John'[3])

# negative numbers are used to index the end of a string
print('indexing from the right side')
print('John'[0])
print('John'[-3])
print('John'[-2])
print('John'[-1])

print('slicing')
s = 'slicing'
s[0:len(s)]  # returns whole string
print(s[0:7])
print(s[2:5])
print(s[-7:-1])

name = input("Enter your name...")
