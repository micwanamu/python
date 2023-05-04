'''
Exercise 160, pp_160.py

Task is the same as in exercise 40 - finding the longest word in the given text, but additionally you have to implement a function get_text(). 
The new function should return the text from a file, 
Write a program with a function called map_longest() that takes a text as a parameter and returns the longest word contained in that text and its length - tuple.

Result of a program should be a message 
e.g. after punctuation removal
The longest word in the file 'shakespeare.txt' is 'internethartvmdcsouiucedu' with the length of 25 characters

e.g. without punctuation removal
The longest word in the file 'shakespeare.txt' is '>internet:hart@.vmd.cso.uiuc.edu' with the length of 32 characters

use map function together with lambda

Exception handling should be implemented.
Implement the possibility of entering file_path from command line
'''


def get_text(file_path: str) -> str:
    '''
    Function opens the text file and returns its content

    Parameters:
        file_path: path to your text file
    Returns:
        text
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def remove_punctuation(word: str) -> str:
    '''
    Function removes punctuation from the given string

    Parameters:
        word: any string with or without the punctuation
    Returns:
        string without punctuation
    '''
    import string
    punct = string.punctuation
    return "".join(i for i in word if i not in punct)


def map_longest(text: str, remove_punct: bool = False) -> tuple:
    '''
    Function returns the longest word in the text and it's length

    Parameters:
        text: any text

    Returns:
        tuple: a tuple containing the longest word and it's length

    '''
    if remove_punct == True:
        text = remove_punctuation(text)
    wordList = text.split()

    longest_word = max(wordList, key=lambda word: len(word))
    return longest_word, len(longest_word)


while True:
    path = input("Enter the path to your text file: ")
    try:
        get_text(path)
    except IOError:
        print("The provided path does not exist.")
        continue
    punct = input(
        "Decide whether you want to remove punctuation from the file (y to remove, n to not remove): ")
    if punct == "y":
        decision = True
    elif punct == "n":
        decision = False
    else:
        print("Specify whether you want to remove the punctuation.")
        continue
    print(map_longest(get_text(path), decision))
    loop = input("Do you want to restart the program? (y/n): ")
    if loop == "y":
        continue
    if loop == "n":
        break
