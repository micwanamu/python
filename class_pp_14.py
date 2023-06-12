import sqlite3

# with sqlite3.connect(r'C:\Users\michw\OneDrive\Documents\UAM\PYTHON CODE\ITCSP\test.db') as conn:
#    command = "INSERT INTO Student (ID, Name, Surname, Admission_Year) Values (3, 'Joe', 'Test', 2019)"
#    conn.execute(command)

L1 = [(4, 'Jessica', 'Jones', 'IT', 2020),
      (5, 'Super', 'Man', 'Heroes', 2018),
      (6, 'Wonder', 'Woman', 'Heroes', 2017)]


# with sqlite3.connect(r'C:\Users\michw\OneDrive\Documents\UAM\PYTHON CODE\ITCSP\test.db') as conn:
#    command = "INSERT INTO Student (ID, Name, Surname, Department, Admission_Year) VALUES (?, ?, ?, ?, ?)"
#    for l in L1:
#        conn.execute(command, l)

# with sqlite3.connect(r'C:\Users\michw\OneDrive\Documents\UAM\PYTHON CODE\ITCSP\test.db') as conn:
#    command = "SELECT * FROM Student"
#    cursor = conn.execute(command)
#    for row in cursor:
#        print(row)

# with sqlite3.connect(r'C:\Users\michw\OneDrive\Documents\UAM\PYTHON CODE\ITCSP\test.db') as conn:
#    command = "SELECT * FROM Student"
#    cursor = conn.execute(command)
#    students = cursor.fetchall()
#    print(students)

# with sqlite3.connect(r'C:\Users\michw\OneDrive\Documents\UAM\PYTHON CODE\ITCSP\test.db') as conn:
#    command = "SELECT * FROM Student WHERE Name = 'Jessica'"
#    cursor = conn.execute(command)
#    for row in cursor:
#        print(row)

# with sqlite3.connect(r'C:\Users\michw\OneDrive\Documents\UAM\PYTHON CODE\ITCSP\test.db') as conn:
#    command = "SELECT Name, Surname FROM Student WHERE Admission_Year = 2020"
#    cursor = conn.execute(command)
#    for row in cursor:
#        print(row)

# CREATING A PROJECT FROM THE BEGINNING

# with sqlite3.connect(r'C:\Users\michw\OneDrive\Documents\UAM\PYTHON CODE\ITCSP\MyDB.db') as conn:
#    conn.execute(
#        "CREATE TABLE IF NOT EXISTS Students ('ID' INTEGER, 'Name' TEXT, 'Surname' TEXT, 'Major' TEXT, 'AdmissionYear' INTEGER)")
#    command = "INSERT INTO Students (ID, Name, Surname, Major, AdmissionYear) Values (?, ?, ?, ?, ?)"
#    for l in L1:
#        conn.execute(command, l)

with sqlite3.connect(r'C:\Users\michw\OneDrive\Documents\UAM\PYTHON CODE\ITCSP\MyDB1.db') as conn:
    conn.execute(
        '''CREATE TABLE IF NOT EXISTS Students1
    (Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Surname TEXT NOT NULL,
    Major TEXT,
    AdmissionYear INTEGER)''')
    command = "INSERT INTO Students1 (Id, Name, Surname, Major, AdmissionYear) VALUES (?, ?, ?, ?, ?)"
    for l in L1:
        conn. execute(command, l)
