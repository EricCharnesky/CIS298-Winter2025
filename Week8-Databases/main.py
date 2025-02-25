import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()


cursor.execute('SELECT name FROM customer')
for row in cursor:
     print(row)