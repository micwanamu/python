'''
Programming Task 03 (file: pt_03a.py)
Points: 15

https://www.w3schools.com/python/python_regex.asp

On the basis of Exercise 190,
Using RE, in 'shakespeare.txt' file, find and print all the 5-characters length words which starts with a vowel and ends with a vowel.
Additionally, print the amount of these words.
Implement the exception handling
Vowels: 'aeoiuy'
Think about the following Special Sequences
\b
\w
{}

Start your analysis from the line no 253.

`\b` matches at the beginning or end of a word ². A word is defined as a sequence of alphanumeric characters or underscores, i.e.,
any character that can appear in a Python identifier ². The `\b` symbol is used to match word boundaries ¹.

For example, in the string "The quick brown fox jumps over the lazy dog", `\bfox\b` would match "fox" but not "foxy" or "foxes" ¹.
Use input function to enter filepath

Exemplary start
###############################################
Text analyzer - finds all 5 characters length words
which starts with a vowel and ends with a vowel

Enter the text filepath: PYTHON PROGRAMMING\shakespeare.txt
Enter the line number from which you want to start analysis: 253

Results:
['use' ...]
The amount of words is 137

'''
import re
import sys
# file_path: str, start_line: int


def get_text() -> str:
    '''
    Function opens the text file and returns its content

    Parameters:
        file_path: path to your text fileS
        start_line: text analysis should start at this specyfic line
    Returns:
        text
    '''
    file_path = open('shakespeare.txt', 'r', encoding='utf-8')
    stuff = file_path.read()
    file_path.close()
    words = str(re.split('\s', stuff))
    start_end = re.findall(r"\b[aeoiuy]\w*?[aeoiuy]\b", words)
    se_str = str(start_end)
    letter = re.findall(r"\b\w{5}\b", se_str)
    print(letter)
    print(
        f'The number of words starting and ending with a vowel in this document is {len(letter)}')


get_text()
