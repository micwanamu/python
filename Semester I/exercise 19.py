'''
Exercise 19
There is a list
hashtags = ['spring','summer','winter']
Connect these element with "#". Add this sign also at the beginning.
Print the result to the terminal
INPUT: list
OUTPUT: str
Expected result: #spring#summer#winter
'''
hashtags = ['spring', 'summer', 'winter']
x = "#".join(hashtags)
new_hashtags = "#" + x
print(new_hashtags)
