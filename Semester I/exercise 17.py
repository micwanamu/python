'''
Exercise 17
For any entered string. Write a program that will reverse the order of the letters and print to the console.
e.g., for "Hello world", printed result should be 'dlrow olleH'
Typing in an "exit" should break the loop end exit the program
INPUT: str
OUTPUT: str

Use while loop, input(), don't use lists (only strings) 

'''

string = input('Enter something...')
reversed = string[::-1]
print(reversed)
