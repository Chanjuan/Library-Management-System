import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database="test"
)
cur=conn.cursor()

def connect():
    cur.execute("CREATE TABLE book (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(20), author VARCHAR(20), year INT,isbn INT)")
    conn.commit()
    #conn.close()

def insert(title,author,year,isbn):
    cur.execute("INSERT INTO book VALUES(null,%s,%s,%s,%s)",(title,author,year,isbn))
    conn.commit()
    #conn.close()

def view():
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    #conn.close()
    return rows

def search(title='',author='',year='',isbn=''):
    cur.execute("SELECT * FROM book WHERE title=%s OR author=%s OR year=%s OR isbn=%s",(title,author,year,isbn))
    rows=cur.fetchall()
    #conn.close()
    return rows

def delete(id):
    cur.execute("DELETE FROM book WHERE id=%s",(id,))
    conn.commit()

def update(id,title,author,year,isbn):
    cur.execute("UPDATE book SET title=%s,author=%s,year=%s,isbn=%s WHERE id=%s",(title,author,year,isbn,id))
    conn.commit()

#insert("The Sun","Jhon Smith",1918,92401934)
#delete(5)
#update(4,"The Moon","Jhon Smooth",1908,28481038)
#print(view())
print(search(author="Jhon Smith"))