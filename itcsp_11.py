print("LISTS CONTINUED")

L = [6, 5, 4, 10, 15, 2]
L.sort()
print(L)

print('---')
L = [6, 5, 4, 10, 15, 2]
L.sort(reverse=True)
print(L)

print('---')
L = [6, 5, 4, 10, 15, 2]
L1 = sorted(L)  # returns a new list unlike the previous method
print(L1)

print('---')
L = [6, 5, 4, 10, 15, 2]
L.reverse()
print(L)

print('---')
L = [6, 5, 4, 10, 15, 2]
print(L.count(6))  # one element '6' in the list

print('---')
L = [6, 5, 4, 10, 15, 2]
print(len(L))  # number of all elements in the list

print('---')
L = [1, 2, 3, 4]
print(L[1])
print(L[1:3])
print(L[1:2])

print('---')
L1 = [1, 2, 3, ['a', 'Jason', 'Brown'], 'c']
print(L1[3][1])

# print(dir(list))
# find all methods that belong to a certain class, in this case to lists

# help(list.append)
# # check syntax of any method, in this case of lists

print("TUPLES")
# they are immutable, can't change their structure
# tuples with one element need a comma at the end!
t1 = ('one',)
print(t1)
t2 = (1, 'two', 3.25)
print(t2)
print(t2[0])
print(t2[1:2])
# t2[0] = 2 # gives an error, can't modify tuple

print('---')
t3 = t1 + t2
print(t3)

print('---')
T = (1, 2, 9, 5)
sum = 0
for i in T:
    sum += i
print(sum)

print('---')
T = (1, 2, 9, 5)
sum = 0
for i in range(len(T)):
    sum += T[i]
print(sum)

print("DICTIONARY")
student_grades = {'Ana': 'B', 'Katy': 'A', 'John': 'B'}
s_grade = student_grades['Ana']  # returns B
print(s_grade)
# returns 'No such key', because we declared it to do so
s_grade = student_grades.get('Rob', 'No such key')
print(s_grade)

# adding values
student_grades['Bob'] = 'A'
print(student_grades)

# changing values
student_grades["Ana"] = 2
print(student_grades)

# removing values
del (student_grades['Katy'])
print(student_grades)

s_grade = student_grades.pop('Rob', 'No such key')  # returns 'No such key'
print(s_grade)

# test if key is in dictionary
print('John' in student_grades)
student_grades['Bob'] = 'B'
print(student_grades.keys())

print(list(student_grades.keys()))
for k in student_grades.keys():
    print(k)

print(student_grades.values())
print(list(student_grades.values()))
for v in student_grades.values():
    print(v)

print(student_grades.items())
print(list(student_grades.items()))
for k, v in student_grades.items():
    print(k, v)

print(len(student_grades))
