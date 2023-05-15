import re
import sys
if re.search('^a[b-e]', sys.argv[1]):
    print('a match')
else:
    print('no match')

# a in the last position, b-e in the second to last position
if re.search('[b-e]a$', sys.argv[1]):
    print('a match')
else:
    print('no match')

# any word ending with a ([a-zA-Z]) for both small and capital letters
if re.search('[a-z]a$', sys.argv[1]):
    print('a match')
else:
    print('no match')

if re.search('[a-z]ana$', sys.argv[1]):
    print('a match')
else:
    print('no match')

# h followed by 0 or more e characters and o at the end; nothing can be between the e and the o though but things can stand before the h
if re.search("he*o", sys.argv[1]):
    print('a match')
else:
    print('no match')

# same, but any character can be between e and o (at least one e)
if re.search("he.*o", sys.argv[1]):
    print('a match')
else:
    print('no match')

l_txt = ['hello world', 'gghello world', 'hello world and planet']
for text in l_txt:
    x = re.search("he.*o", text)
    print(text + '--->' + str(x))


txt = "This is banana. Banana is very good. I like it very much.\n Here are other fruits: strawberries, raspberries, pineapples"
L1 = re.findall('banana', txt)
L2 = re.findall('banana', txt.lower())  # changes text so not recommended
L3 = re.findall('[Bb]anana', txt)
print(L1, L2, L3)
# L4 = re.split('\s', txt) # splits at every space
