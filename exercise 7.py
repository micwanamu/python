'''
Exercise 07
Create a string made of the first, middle and last character and print it to the terminal

Expected results
text = 'abcdefg'  # expected result: adg
text = 'abcdef'  # expected result adf

Hints:
Use string indexing to get the character present at the given index
Get the index of the middle character by dividing string length by 2
Function that returns string length:
l= len(text)

'''
text1 = 'abcdefg'
text2 = 'abcdef'
l1 = len(text1)
l2 = len(text2)
middle1 = l1 // 2
middle2 = l1 // 2

print(text1[0] + text1[middle1] + text1[l1 - 1])
print(text2[0] + text2[middle2] + text2[l2 - 1])
