# win + r, cmd to open windows terminal

import sys

L1 = sys.argv
print(L1)  # a list whose first element is the name of the file

# you can add other elements to the list (in windows terminal): python class_pp_08.py arg1 arg2 agr3

sentence = sys.argv[1]  # first argument, argument 0 is name of the file
print(len(sentence), "this is the length of the first argument")
# putting an item in double quotes makes it the argument 1 (I think)

n1 = float(sys.argv[1])
n2 = float(sys.argv[2])
print(n1*n2)


vowels = 'aeiou'
word = sys.argv[3]
vowelcount = 0
for letter in word:
    if letter in vowels:
        vowelcount += 1
print(f'There are {vowelcount} vowels in the word.')

# working on files
outFile = open('testfile.txt', 'w')  # has to be in the same folder
# r for reading (default)
# w for writing; creates a new file if it doesn't exist or truncates (replaces) the file if it exists
# a for appending without truncating or creates a new file
# t for text mode (default); no need to declare it

outFile.write('some text!\n')
outFile.read()
outFile.close()


# sample_file = open(
#    r"C:\Users\michw\OneDrive\Documents\UAM\PYTHON CODE\ITCSP\testfile.txt")

outfile = open('testfile.txt', 'w', encoding='utf-8')
outfile.write('some text\n')
outfile.write('... and even more\n')
outfile.close()

# appending to a file
outfile = open('testfile.txt', 'a', encoding='utf-8')
outfile.write('... and EVEN more!\n')
outfile.close()

outfile = open('testfile.txt', 'r')
stuff = outfile.read()
outfile.close()
print(stuff)

outfile = open('testfile.txt', 'r')
stuff = outfile.read()
outfile.close()
lines = stuff.split('\n')
for line in lines:
    print(f'{line}, : {len(line)} characters')
