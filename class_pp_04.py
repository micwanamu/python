print('iterables revisited')
# iter and get item

print('range')
for x in range(5):
    print(x)

print('string')
for x in 'Python':
    print(x)

print('list')
for x in ('a', 1, 2, 'b'):
    print(x)

print('tuples')
for x in ('c', 1, 2, 'd'):
    print(x)

print('dictionary')  # only keys in this way
dic = {'a': 1, 'b': 2, 'c': 3}
for x in dic:
    print(x)

print('dictionary keys 2')
for x in dic.keys():
    print(x)

print('dictionary values')
for x in dic.values():
    print(x)

print('dictionary in tuples')
for x in dic.items():
    print(x)

print('unpacking iterable')
d, c = (5, 6)
print(d, c)

for k, v in dic.items():
    print(k, v)
