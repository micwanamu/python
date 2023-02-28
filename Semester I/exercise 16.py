'''
Exercise 16

Enter any file name together with it's extension.
Check if the entered file name is of type pdf or others.
INPUT: str
Exemplary input
Enter the filname together with it's estension: ...
OUTPUT: str
Exemplary output
Your file has an extension "2s"
Program should implement error handling. In a case that a filename without an extension was entered, the following message should appear:
You entered a filename without an extension, try once more


use:
input()
string slicing
for volunteers/advanced use ternary operator

tests:
file01.docx, myBook.pdf, file02.2s
'''
# enter a filename

# find the index of "." which separates filename and it's extension

# specify the index of the first character of your extension

# write the conditional (if statement), using string slicing, substring your extension and print messages

# for advanced -> use ternary operator

user_filename = input(
    "Format checker. Enter the filename with its extension...")
if '.' not in user_filename:
    print("You entered a filename without an extension, try once more")
else:
    extension_name = user_filename.split(".", 1)[1]
    ex_lower = extension_name.lower()
    if ex_lower == 'pdf':
        print("Your file is of type pdf")
    elif ex_lower == 'docx':
        print("Your file is of type docx")
    elif ex_lower == '2s':
        print("Your file is of type 2s")
    else:
        print("You have entered an invalid extension name")
