import sqlite3

connection = sqlite3.connect('business.db')

connection.execute('DELETE FROM products WHERE price > ?', [100])                 # Delete all rows in products
connection.commit()