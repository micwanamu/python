# SQL

# INSERT INTO table_name (column1, column2)
# VALUES (value1, value2)

# SELECT column1, column2
# FROM table_name

# SELECT column1, column2
# FROM table_name
# WHERE condition; (e.g. with a name starting with J)

import sqlite3
connection = sqlite3.connect(
    r'C:\Users\michw\OneDrive\Documents\UAM\PYTHON CODE\ITCSP\test.db')
command = "INSERT INTO Student (ID, Name, Surname) Values (1, 'Tim', 'Jones')"
connection.execute(command)
connection.commit()
connection.close()

with sqlite3.connect(r'C:\Users\michw\OneDrive\Documents\UAM\PYTHON CODE\ITCSP\test.db') as conn:
    command = "INSERT INTO Student (ID, Name, Surname) Values (2, 'Jim', 'Tones')"
    conn.execute(command)
