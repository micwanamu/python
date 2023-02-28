'''
Write a program that asks the user for their first name, year of birth and the current year, then calculates 
and lists the information about name and age in the terminal.
Sample workflow:
Enter your name: ... Ann 
Enter your birth Year: ... 2001 
Enter the current Year: ... 2021

Sample result
Ann, you are 20 years old.

'''

name = input("Please enter your first name...")
birth = int(input("Please enter your year of birth..."))
year = int(input("Please enter the current year..."))
age = year - birth

print(name + ' you are ' + str(age) + ' years old.')
