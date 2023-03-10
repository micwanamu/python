'''
Write a program that will raise all the elements of a list to the third power
Input : list of integers
Returns : list of integer numbers raised to the third power
use map function
'''

int_list = [6, 9, 12, 89, 2]

print('Raising to the third power...')
raised = list(map(lambda x: pow(x, 3), int_list))
print(raised)
