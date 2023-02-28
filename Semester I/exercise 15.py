'''
Exercise 15
Write a program that counts vowels in a string
The program should implement the possibility for the user to enter any word.

INPUT: str
OUTPUT: str

Use input() function
vowels = 'aeiou'

The exemplary input:
Enter a word ... 

The exemplary output in  terminal should be:
You have 6 vowels in a word "Appalachicola"
Tests:
VOWELS -> 2 vowels
vowels -> 2 vowels
Appalachicola -> 6 vowels

'''

vowels = 'aeiouy'
vowelCount = 0
word = input('Enter any text...')
new_word = word.lower()
for letter in new_word:
    if letter in vowels:
        vowelCount += 1
print('The number of vowels in', word, 'is', vowelCount)
