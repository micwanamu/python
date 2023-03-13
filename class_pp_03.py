# filter function
# filter(func, *iterables)

print("filtering simple lists")
L1 = [1, 2, 5, 62, 52]


def filter_list(item):
    return item > 10


filter_list = list(filter(filter_list, L1))
print(filter_list)
# has to return boolean value

print("filtering complex lists")
L2 = [
    ('Bread', 10),
    ('Butter', 20),
    ('Dark chocolate', 15),
    ('White chocolate', 17),
    ('Cakes', 19)
]


def price_filter(item):
    return item[1] > 15


filtered_list = list(filter(price_filter, L2))
print(filtered_list)


print("filtering with lambda")
filtered_list = list(filter(lambda item: item[1] > 15, L2))
print(filtered_list)

print("filtering dictionaries")
L2 = [{'Name': 'Bread', 'Price': 10},
      {'Name': 'Butter', 'Price': 20},
      {'Name': 'White chocolate', 'Price': 15},
      {'Name': 'Dark chocolate', 'Price': 30},
      {'Name': 'Cakes', 'Price': 19}
      ]

filtered_list = list(filter(lambda item: item['Price'] > 15, L2))
print(filtered_list)

print("list revisited")
words = ['data', 'science', 'machine', 'learning']
word_length = []
for word in words:
    word_length.append(len(word))
print(word_length)

word_length = list(map(lambda item: len(item), words))
print(word_length)

print("list comprehension")  # creation of lists in other words
words = ['data', 'science', 'machine', 'learning']
word_length = [len(word) for word in words]  # new list will be created
print(word_length)

L2 = [
    ('Bread', 10),
    ('Butter', 20),
    ('Dark chocolate', 15),
    ('White chocolate', 17),
    ('Cakes', 19)
]
prices = [item[1] for item in L2]  # list only with prices
print(prices)

prices = [item[1] * 1/2 for item in L2]
print(prices)
product_prices = [(item[0], item[1]*1.2) for item in L2]  # products and prices
print(product_prices)

prices = [(item[0], item[1]*1.2) for item in L2 if item[1]
          >= 15]  # raise prices only for filtered items
print(prices)

print("dictionaries revisited")
words = ['data', 'science', 'machine', 'learning']
word_length = {}
for word in words:
    word_length[word] = len(word)
print(word_length)

shakes = 'When forty winters shall besiege thy brow, and dig deep trenches in thy beautys filed, ...'
shakes = shakes.replace(',', '').replace('.', '')
words = shakes.split()
word_length = {}
for word in words:
    word_length[word] = len(word)
print(word_length)

word_length = {word: len(word) for word in words}
print(word_length)

shakes = 'When forty winters shall besiege thy brow, and dig deep trenches in thy beautys filed, ...'
shakes = shakes.replace(',', '').replace('.', '').split()
word_length = {word: len(word) for word in words}
print(word_length)

product_dic = {
    'Bread': 10,
    'Butter': 20,
    'Dark chocolate': 15,
    'White chocolate': 17,
    'Cakes': 19
}
prod_pri_inc = {key: value*1.2 for key, value in product_dic.items()}
print(prod_pri_inc)

print("sorting dictionaries")
shakes = 'When forty winters shall besiege thy brow, and dig deep trenches in thy beautys filed, ...'
words = shakes.replace(',', '').replace('.', '').split()
word_length = {word: len(word) for word in words}
sorted_word_length = sorted(
    word_length.items(), key=lambda item: item[1], reverse=True)
print(sorted_word_length)  # list
print(dict(sorted_word_length))  # dictionary
