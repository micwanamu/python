print("Hello World!")
print('I study at the Faculty of English', 'at Grunwaldzka street.')
print('I', 'want', 'to', 'name', 'a', 'file', sep="_")

print("Ana has a cat", end=" ")  # default is printing in the new line
print("and a dog.")

a = 10
b = "hello"
c = 3.14
print(a, b, c)

'''This is a multiline comment!'''

# a = 3.14 # we can easily create comments with ctrl + /


# int - integer, aka whole numbers
# float - numbers with a decimal point (e.g. 3.1, 1.7*10^3, 9.0)
# bool - True or False, logical values
# NoneType - type with a single value None

print(type(3))
print(type(3.17))
print(type(True))

a = True
print(type(a))

# type conversion
float(3)  # int to float, changes to 3.0
int(3.7)  # float to int, changes 3.7 to 3 - not rounding, but trimming

# An expression combines objects and operators, for example 2 + 2
x = 5
x = x + 6  # overrides the old x, printing only x + 6 doesn't override the original x
print(x)
# if both objects are integers, the results will be an integer, if either is a float, the result will be the float

i = 15
j = 4

# integer division
print(1//4)
print(i//j)
# i % j - modulo division
print(i % j)
# i ** j - i to the power of j
print(i ** j)

# operator precedence
# 1 parentheses
# 2 **
# 3 * and /
# 4 + and - from left to right
