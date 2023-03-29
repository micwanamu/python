'''
Exercise 120, file pp_120.py
Write a function that will check if a word/sentence is a palindrome or not.
Use recursive implementation
These are palindromes, test with them:
Dad 
Evil olive.
Never odd or even.
Amore, Roma.

Not palindromes:
test
ad
a
'''

"https://www.dictionary.com/e/palindromic-word/"


def remove_punctuation(text: str, remove_space: bool = False) -> str:
    '''
    Function removes punctuations !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ optionally it can remove spaces

    Parameters:
        text: any text
        remove_space: if True, spaces are removed, if False, spaces are not removed
    Returns:
        text without punctuation, optionally spaces
    '''
    import string
    punct = string.punctuation
    textCleared = ''
    for character in text:
        if character not in punct:
            textCleared += character
            no_space = textCleared.replace(' ', '').lower()
    return no_space


def is_palindrome(text: str) -> bool:
    '''
    Function checks if any text is a palindrome

    Parameters:
        text: any text
    Returns:
        True: if text is palindrome
        False: if text is not a palindrome
    '''
    if len(text) < 1:
        return True
    else:
        if text[0] == text[-1]:
            return is_palindrome(text[1:-1])
        else:
            return False


def print_palindrome_check(text: str) -> None:
    '''
    Function prints the message if text is palindrome or not

    Parameters:
        text: any text
    '''
    if text == True:
        print(f'{phrase} is a palindrome.')
    else:
        print(f'{phrase} is not a palindrome.')


phrase = str(input("Enter any text to check if it's a palindrome..."))


a = remove_punctuation(phrase)
b = is_palindrome(a)
print(print_palindrome_check(b))
