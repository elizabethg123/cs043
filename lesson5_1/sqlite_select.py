import sqlite3

connection = sqlite3.connect('business.db')

cursor = connection.cursor()

product_cursor = cursor.execute('SELECT prodname, weight, price FROM products')
product_list = product_cursor.fetchall()
for pname, weight, price in product_list:
    print('Product: {}\tWeight: {} kg\tPrice: {}'.format(pname, weight, price))