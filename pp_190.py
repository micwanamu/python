'''
Exercise 190

https://www.w3schools.com/python/python_regex.asp

Using RE find all the 5-characters length

Think about the following Special Sequences
\b
\w
{}


`\b` matches at the beginning or end of a word ². A word is defined as a sequence of alphanumeric characters or underscores, i.e., 
any character that can appear in a Python identifier ². The `\b` symbol is used to match word boundaries ¹. 

For example, in the string "The quick brown fox jumps over the lazy dog", `\bfox\b` would match "fox" but not "foxy" or "foxes" ¹.

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
    print(re.findall(r"\b\w{5}\b", words))


get_text()
