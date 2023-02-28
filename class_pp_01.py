###
# Function revision
###

import string


def send_greetings(name: str) -> None:
    print(f'Hello {name}')


send_greetings('Jess')
send_greetings('Bill')
send_greetings('Ann')


def send_self_presentation(name, surname, birth_year, current_year):
    age = current_year - birth_year
    return f'Hello, my name is {name} {surname} and I am {age} years old.'


print(send_self_presentation('Jessica', 'Jones', 1998, 2023))

###
# FPT group 1
###


def show_products(products: list) -> None:
    print('\n===== My products:')
    for i in range(len(products)):
        print(f'{i+1}. {products[i]}')


# lists start with 0, which is why we have i + 1 to make it start from 1
products = []
while True:
    menu = '''
    1. Add product
    2. Change name
    3. Remove product
    4. Show all
    5. Exit program
    '''
    print(menu)
    operation = input('Enter something')
    if operation == '5':
        break
    elif operation == '1':
        name = input('Enter the name of the product you want to add...')
        products.append(name)
        print(f'-> ... {name} added\n')
    elif operation == '2':
        index = int(
            input('Enter the product number you want to rename...'))
        old_name = products[index-1]
        new_name = input(f'Enter the new name for "{products[index-1]}" ...')
        products[index-1] = new_name
        print(f'-> "{old_name}" renamed\n')
    elif operation == '3':
        index = int(
            input('Enter the product number you want to remove'))
        if len(products) >= 1:
            prod = products.pop(index-1)
            print(f'-> "{prod}" removed.\n')
    elif operation == '4':
        show_products(products)
    else:
        print('Wrong index')


###
# FPT group 2
###


text = '''
Artificial Intelligence (AI) is a rapidly evolving field that involves the development of computer systems capable of performing tasks that typically require human intelligence such as 
visual perception, speech recognition, and decision-making. AI systems can be trained using large amounts of data to recognize patterns and make predictions. Machine learning is a 
subfield of AI that focuses on the development of algorithms that can learn from and make predictions based on data. The use of AI is becoming widespread across various industries, 
including healthcare, finance, transportation, and retail. While AI has the potential to bring about significant positive change in our society, it also raises ethical and social issues. 
For example, the use of AI in decision-making could perpetuate existing biases and lead to unfair outcomes. There are also concerns about job displacement as AI systems become more capable 
of performing tasks that were previously done by humans. To address these challenges, there is a growing need for responsible and ethical AI development and deployment. 
This involves creating systems that are transparent, explainable, and accountable, as well as investing in education and training to ensure that individuals have the skills and knowledge 
to participate in the AI-driven economy. In conclusion, AI is a rapidly evolving field that has the potential to bring about significant positive change, but it is important that we approach 
its development and deployment with caution and responsibility.
'''


def remove_punctuation(word: str) -> str:
    punct = string.punctuation
    wordCleared = ''
    for character in word:
        if character not in punct:
            wordCleared += character
    return wordCleared


def get_word_frequency_dictionary(wordList: list) -> dict:
    dictionary_of_words = {}
    for word in wordList:
        if word not in dictionary_of_words.keys():
            dictionary_of_words[word] = 1  # find for the first time
        else:
            dictionary_of_words[word] += 1  # find for another time
    return dictionary_of_words


def print_dictionary(d: dict, num) -> None:
    counter = 0
    for k, v in d.items():
        counter += 1
        print(f'{counter}. {k}{v}')
        if counter == num:
            break


def print_word_number(wordList: list) -> None:
    print(f'\nTotal of words: {len(wordList)}')


wordList = text.split()
wordListWithoutPunct = []
for word in wordList:
    wordCleared = remove_punctuation(word)
    wordListWithoutPunct.append(wordCleared.lower())
dictionary_of_words = get_word_frequency_dictionary(wordListWithoutPunct)
# sorted_dictionary_of_words = get_sorted_dictionary(dictionary_of_words)
# extra task for sorting the dictionary
print_dictionary(dictionary_of_words, 10)
print_word_number(wordListWithoutPunct)

###
# New material
###

# Keyword arguments
# used during function calling


def add_profile(index, ix, iy, area):
    print(
        f'Adding profile {index} with moments of interia Ix={ix} cm4, Iy={iy} cm4, and area {area} cm2')


add_profile('MC014', 166.9, 23.6, 14.99)
add_profile(index='MC014', ix=166.9, iy=23.6, area=14.99)

# Default (optional) arguments
# must be declared in function definition


def add_item(item_name, quantity=1):  # 1 is defined as the default number
    print(f'{quantity} units of {item_name} was added')


add_item('bread')
add_item('apples', 2)

# *args (xargs)


def print_numbers(*numbers):  # it can be iterated
    print(numbers)


print_numbers(1, 2, 3, 4, 5)


def print_numbers(*numbers):
    for n in numbers:
        print(n)


print_numbers(1, 2, 3, 4, 5, 6, 7)


def summarize(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum


print(f'The sum of the number is {summarize(1,2,3,4,5)}')

# **kwargs (xxargs)


def add_user(**user: dict) -> None:
    print(type(user))
    print(user)


# collection of keyword arguments
add_user(id=1, name='John', surname='Kowalski', age=25)


def print_user(**user: dict) -> None:
    for key, value in user.items():
        print(f'{key} = {value}')


print_user(id=1, name='John', surname='Kowalski', age=25)

users = []


def add_user(**user: dict) -> None:
    users.append(user)


add_user(id=1, name='John', surname='Kowalski', age=25)
add_user(id=2, name='Anna', surname='Nowicka', age=25)
print(users)
