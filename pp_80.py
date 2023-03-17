'''
Exercise 80, file "pp_80.py"
The text is given:
shakespeare = 'When forty winters shall besiege thy brow, And dig deep trenches in thy beautys field, ....'
Write a program that will find and print to the terminal the longest word in the text.
In order to achieve it, implement the function that will delete all '.', ',', get the list of all words,  
use dictionary comprehension to get word:length pairs and use sorted() functio.

Expected result:
The longest word is 'trenches' with the length 8 characters.

'''

shakespeare = 'When forty winters shall besiege thy brow, And dig deep trenches in thy beautys field, ....'


def get_longest_word(text: str) -> tuple[str, int]:
    '''
    Function returns the longest word together with its length

    Parameters:
        text: any text
    Returns:

    Exemplary result:
    ('trenches',8)
    '''

    for character in shakespeare:
        shake_new = shakespeare.replace('.', '').replace(
            ',', '').lower()
    sorted_freq = list(
        sorted(
            {i: len(i) for i in shake_new.split()}.items(),
            key=lambda item: item[1],
            reverse=True,
        )
    )
    return sorted_freq[0]


longest_word = get_longest_word(shakespeare)
print(
    f"The longest word is '{longest_word[0]}',"
    f" with the length of {longest_word[1]} characters."
)
