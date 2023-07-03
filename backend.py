import sqlite3

def connect():
    db = sqlite3.connect("books.db")
    curs=db.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text,year INTEGER,isbn INTEGER)")
    db.commit()
    db.close()

def insert( title, author, year, isbn):
    db = sqlite3.connect("books.db")
    curs = db.cursor()
    curs.execute("INSERT INTO book  VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    db.commit()
    db.close()
def search( title, author, year, isbn):
    db = sqlite3.connect("books.db")
    curs = db.cursor()
    curs.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows = curs.fetchall()
    db.close()
    return rows
def viewAll():
    db = sqlite3.connect("books.db")
    curs = db.cursor()
    curs.execute("SELECT * FROM book")
    rows = curs.fetchall()
    db.close()
    return rows

connect()
insert("Atomic habit","Jeams",2015,123456)
viewAll()