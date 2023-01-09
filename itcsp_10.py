# functions:
# e.g. print(), input(), len() - not associated with any object

# methods
# e.g. s.lower(), s.upper(), s.capitalize() - associated with the objects and its type

# while loop
counter = 0  # counter has to be declared before while loop
while counter < 6:
    print(counter)
    counter += 1

### infinite loop ###
# while counter < 6:
# print(counter)
# counter += 1
# ctrl + c breaks the loop

# produces a sequence of numbers, starts from 0 and ends at the specified number
type(range(5))
# start (optional) - default is 0
# stop (required)
# step (optional) - default is 1; how much will be added at one time

# for loop
print('first loop')
for i in range(5):
    print(i)  # i is initialized during the loop

print('second loop')
for i in range(3, 7):
    print(i)

print('third loop')
for i in range(3, 20, 2):  # step is 2
    print(i)

vowels = 'aeiouy'
vowelCount = 0
word = 'Appalachicola'
new_word = word.lower()  # includes uppercase letters
for letter in new_word:
    if letter in vowels:
        vowelCount += 1
print('The number of vowels is', vowelCount)

# while True:  # infinite loop
#    text = input('Enter any text...')

while True:  # finite loop
    text = input('Enter any text...')
    if text == 'exit':
        break

# lists are ordered, the elements remain in the order you gave them
mylist1 = [1, 3, 4, 2, 5]
mylist2 = ['hello', 'world', 'smile']
# you can store lists in lists, as well as different types of elements
mylist3 = [[1, 2, 3, ], 'Warsaw', 5]
mylist1[0]  # returns the first element
i = 2
print(mylist2[i-1])  # returns the second element
# lists are mutable, unlike strings
first_list = [2, 'cat', 5.0, True]
first_list[0] = 'test'
print(first_list)

L = [1, 2, 3, 4]
L.append(5)
L.remove(1)
