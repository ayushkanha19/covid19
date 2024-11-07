import sqlite3
def find_all_books():
    Connection= sqlite3.connect("Data.db")
    cursor= Connection.cursor()
    cursor.execute('SELECT * FROM books')
    books=[row[2] for row in cursor.fetchall()]
    Connection.commit()
    Connection.close()
    print(books)
find_all_books()