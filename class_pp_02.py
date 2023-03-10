# variable scope
# local scope - inside a function
# global scope - created in the main body; available within both global and local scopes (e.g., in a file)

def my_func():
    message = 'a'
# print(message) returns an error because message has only local scope


message = 'a'


def my_func():
    print(message)


my_func()

###
print('###')
###

message = 'a'


def my_func():
    message = 'b'
    print(message)


print(message)  # global message
my_func()  # local message
# can't change global variable inside local scope! the two messages are two different variables with the same name

# list unpacking

# assigning
colors = ['red', 'green', 'blue']
var1 = colors[0]
var2 = colors[1]
var3 = colors[2]

# actual list unpacking
colors = ['red', 'green', 'blue']
var1, var2, var3 = colors
print(var1)
print(var2)
print(var3)

numbers = [1, 2, 5, 7, 9, 9, 9, 9, 9, 9]
first_num, second_num, *others = numbers  # cannot have too few variables!
print(first_num)
print(others)  # no *

numbers = [1, 2, 5, 7, 9, 9, 9, 9, 9, 100]
first_num, *others, last_num = numbers
print(first_num)
print(others)
print(last_num)

# list sorting
L1 = [
    ('Bread', 10),
    ('Butter', 20),
    ('Dark chocolate', 15),
    ('White chocolate', 17),
    ('Cakes', 19)
]
L1.sort(reverse=True)
print(L1)  # sorted alphabetically reversed; sorted by first item

###

L2 = [
    ('Bread', 10),
    ('Butter', 20),
    ('Dark chocolate', 15),
    ('White chocolate', 17),
    ('Cakes', 19)
]


def sort_product(item):
    return item[1]


L2.sort(key=sort_product, reverse=True)
print(L2)  # sorted by key in a descending way

# lambda function (expression) anonymous function, used as a parameter to other functions
# lambda parameters : expression

L2 = [
    ('Bread', 10),
    ('Butter', 20),
    ('Dark chocolate', 15),
    ('White chocolate', 17),
    ('Cakes', 19)
]

L2.sort(key=lambda item: item[1])
print(L2)

# map function

L2 = [
    ('Bread', 10),
    ('Butter', 20),
    ('Dark chocolate', 15),
    ('White chocolate', 17),
    ('Cakes', 19)
]
L2 = list(map(lambda item: item[1], L1))
print(L2)  # transforming the list, only the prices

L2 = list(map(lambda item: (item[0], item[1]*1.2), L1))
print(L2)
