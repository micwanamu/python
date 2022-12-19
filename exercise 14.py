'''
Exercise 14

Enter any file name together with it's extension e.g., file01.docx, myBook.pdf
Check if the entered file name is of type pdf or others.
INPUT: str
"Enter the filname"
OUTPUT:
"Your file is of type pdf"
"Your file is not of type pdf"

use:
input()
string slicing
ternary operator

'''

x = input("PDF format checker. Enter the filname with its extension...")
print("Your file is of type pdf") if 'pdf' in x else print(
    "Your file is not of type pdf")
