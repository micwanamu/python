'''
Exercise 21
For any entered string. Write a program that will reverse the order of the letters and print to the console.
e.g., for "Hello world", printed result should be 'dlrow olleH
Typing in an "exit" should break the loop end exit the program
INPUT: str
OUTPUT: str

Use while loop, input(), use lists

'''

while True:
    user_input = input("Please enter something...")
    if user_input == "exit":
        break
    else:
        new_list = list(user_input)
        new_list.reverse()
        print("".join(new_list))
