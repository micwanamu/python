# comparison operators
i = 5
j = 7
k = i > j

print(i > j)
print(i >= j)
print(i < j)
print(i <= j)
print(i == j)
print(i != j)

# logical conjunction - and
print(True and True)
print(True and False)
print(False and True)
print(False and False)
# true only if both expressions are true

# logical disjunction - or
print(True or True)
print(True or False)
print(False or True)
print(False or False)
# false only if both expressions are false

# logical negation - not
print(not True)
print(not False)

expression_01 = 2 > 1  # boolean expression
expression_02 = 5 > 6

print(expression_01 and expression_02)
print(expression_01 or expression_02)
print(not expression_02)

# logical operator precedence
print(not True and False)
meal = "fruit"
money = 0
is_lunch_delivered = meal == "fruit" or meal == "sandwich" and money >= 2
# returns true because it groups sandwich and money together
is_lunch_delivered = (meal == "fruit" or meal == "sandwich") and money >= 2
# returns false because checks money and meal separately
print(is_lunch_delivered)
