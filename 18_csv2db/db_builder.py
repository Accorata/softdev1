'''
Henali: Henry (e), Erica (hugo), Aahan (spikes)
SoftDev Pd 8
18: (Python+Sqlite)3: A Mare Widge Made in Hebben
Oct 25, 2022
Estimated Time:
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

students = open('students.csv')
dictionary = csv.DictReader(students)

# c.execute("CREATE TABLE test (name TEXT);")
# c.execute('INSERT INTO test ("testname");')
c.execute("CREATE TABLE students (name TEXT, age INTEGER, id INTEGER);")
for row in dictionary :
    print(row)
    command = "INSERT INTO students VALUES ('"+row['name']+"', "+row['age']+", "+row['id']+");"
    print(command)
    c.execute(command)
# command = ""          # test SQL stmt in sqlite3 shell, save as string
# c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
