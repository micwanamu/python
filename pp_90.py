'''
Exercise 90, file pp_90.py
Write a program that will check if a word/sentence is a palindrome or not.
Remove punctuations and spaces
Use iterative way (loop) to check if palindrome

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


def is_palindrome(text: str) -> bool:
    '''
    Function checks if any text is palindrome or not

    Parameters:
        text: any text
    Returns:
        True: if text is palindrome
        False: if text is not a palindrome
    '''
    flag = False

    import string
    punct = string.punctuation
    nopunct = ''
    for character in text:
        if character not in punct:
            nopunct += character

    nopunct = nopunct.replace(" ", "").lower()

    mid = len(nopunct)//2

    for i in range(mid):
        flag = True
        if nopunct[i] != nopunct[-i - 1]:
            flag = False
            break

    return flag


text = input("Enter any text to check if it's a palindrome...")

flag = is_palindrome(text)
print(flag)
