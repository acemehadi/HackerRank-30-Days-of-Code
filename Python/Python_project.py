import sqlite3


def Creat_table():

    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Store(item TEXT,quantity INTEGER,price US)")
    conn.commit()
    conn.close()


def insert_data(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()


insert_data("Coffecup", 2, 100)


def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Store")
    row = cur.fetchall()
    conn.close()
    print(row)


view()
