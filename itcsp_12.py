student_grades = {'Ana': 'B', 'Katy': 'A', 'John': 'B'}

student_grades.clear()
print(student_grades)

print('---')
student_grades = {'Ana': 'B', 'Katy': 'A', 'John': 'B'}
# copy() makes a copy of a dictionary
# not a copy, it is pointing to the same reference
student_grades_01 = student_grades
print(student_grades_01)
student_grades_02 = student_grades.copy()
student_grades["Ana"] = "C"
print('original, changed to make it different from the copy')
print(student_grades)
print('copy')
print(student_grades_02)

print('---')
data = {
    'key1': {
        'inner_key1': 1,
        'inner_key2': 2
    },
    'key2': {
        'inner_key1': 3,
        'inner_key2': 4
    }
}

value = data.get("key1").get("inner_key1", "key not found, error")
value = data['key1']['inner_key2']
print(value)

print('---')
print('formatting string')

name = 'Jess'
print(f'My name is {name} :)')
var1 = 2
var2 = 5
print(f'var1 multiplied by var2 equals: {var1*var2}')

print('---')
print('functions')


def is_even(i):
    """
    Function checks whether the number is even or odd.

    Parameters i (int): positive int number to be checked

    Returns:
    (bool): True if i is even, otherwise False
    """

    return i % 2 == 0


print(is_even(3))
print(is_even.__doc__)  # prints docstring (in triple quotes)
print(str.strip.__doc__)


def greet():
    '''Prints greetings'''
    print('hello')
    print('how are you')


greet()


def send_greeting(name):
    '''Functions prints the greeting
    Parameter:
    name (str) name of the person'''
    print(f'hello {name}')


send_greeting('Jess')
print(send_greeting.__doc__)


def send_greeting(name):
    '''Functions prints the greeting
    Parameter:
    name (str) name of the person
    Returns:
    (str): greeting with a name'''
    return f'hello {name}'


print(send_greeting('Anna'))


def send_self_presentation(name, surname, birth_year, current_year):
    age = current_year - birth_year
    return f'Hello, my name is {name} {surname} and I am {age} years old.'


print(send_self_presentation("Jessica", "Jones", 1998, 2023))
