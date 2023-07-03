import sqlite3
import pandas as pd

conn = sqlite3.connect('books.db')
curs = conn.cursor()

#Create table

#Create the columns of the table
curs.execute('''CREATE TABLE IF NOT EXISTS books
    (
     title VARCHAR(80),
     author VARCHAR(25),
     year INT
     )''')

data = pd.read_csv('books2.csv')

for row in data.itertuples():
    curs.execute("INSERT INTO books VALUES('"+ row.title + "','" 
                 + row.author + "'," + 
                 str(row.year) + ")")

see_table = curs.execute("SELECT * FROM books")
for item in see_table:
    print(item)

curs.close()
conn.close()