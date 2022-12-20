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

user_filename = input(
    "PDF format checker. Enter the filename with its extension...")
extension_name = user_filename.split(".", 1)[1]
ex_lower = extension_name.lower()
print("Your file is of type pdf") if ex_lower == 'pdf' else print(
    "Your file is not of type pdf")
