# programming task 01
def remove_punctuation(text: str, remove_space: bool = False) -> str:
    punc = '''!()-[];:'"\, <> . /?@  # $%^&*_~'''

    no_punc = ""
    for char in my_str:
        if char not in punc:
            no_punc = no_punc + char
    return no_punc


my_str = "Wow! That's amazing. How did you do it? I'm so impressed. You're awesome, brilliant, and talented. Congratulations! Well done. Bravo!"
print(remove_punctuation(my_str))

###


def remove_punctuation(text: str, remove_space: bool = False) -> str:
    import string
    punct = string.punctuation
    textCleared = ''
    for character in my_str:
        if character not in punct:
            textCleared += character
            no_space = textCleared.replace(' ', '').lower()
    return no_space  # do not print!


my_str = "Wow! That's amazing. How did you do it? I'm so impressed. You're awesome, brilliant, and talented. Congratulations! Well done. Bravo!"
print(remove_punctuation(my_str))

###


def remove_punctuation(text: str, remove_space: bool = False) -> str:
    import string
    punct = string.punctuation

    if remove_space:
        punct += ' '
    return ''.join([t for t in text if t not in punct])


text = "Wow! That's amazing. How did you do it? I'm so impressed. You're awesome, brilliant, and talented. Congratulations! Well done. Bravo!"
print(remove_punctuation(text, True))

print('recursion')

'''
def mult(a, b):
    if b == 0:
        return 0
    if b == 1:  # base case
        return a
    else:  # recursive step
        return a + mult(a, b-1)


a = int(input('a = '))
b = int(input('b = '))
print(f'{a} * {b} = {mult (a,b-1)}')
'''

print('ternary operator')
# [on_true] if [expression] else [on_false]

a, b = 11, 15
min = a if a < b else b
print(min)

a, b = 11, 15
min = a+b if a < b else a-b
print(min)


print('pass statement')
for i in range(1, 5):
    pass  # allows you to skip this section if the code is not ready yet
a, b = 11, 15
if a < b:
    pass

# s = 'Hey, what's up?'
s = 'Hey, what\'s up?'

# s = "His name is "John""
s = "His name is \"John\""

print("Multiline strings\ncan be created\nusing escape sequences.")
