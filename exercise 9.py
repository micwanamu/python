'''
Exercise 09
Write a program (modify the old one) that asks the user for their first name, year of birth and the current year, then calculates 
and lists the information about name and age in the terminal.
Sample workflow:
Enter your name: 
Ann 
Enter your birth Year:
2001 
Enter the current Year:
2021

Sample result
Ann, you are 30 years old.

Use "new line": \n
'''

name = input("Please enter your first name... \n")
birth = int(input("Please enter your year of birth... \n"))
year = int(input("Please enter the current year... \n"))
age = year - birth

print(name + ' you are ' + str(age) + ' years old.')
