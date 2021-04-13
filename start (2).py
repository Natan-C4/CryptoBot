import sqlite3

a = 1
connection = sqlite3.connect("sqlite.db")

cursor = connection.cursor()

cursor.execute("INSERT INTO `crypto` (coin_id) VALUES (?) ",
               (a))


connection.commit()

connection.close()

#2, 131, 1027, 1321, 1376, 1720, 1831
