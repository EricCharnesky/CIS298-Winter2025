import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

# to create tables via code
# cursor.execute("""
# CREATE TABLE "customer" (
# 	"id"	INTEGER,
# 	"name"	TEXT,
# 	PRIMARY KEY("id" AUTOINCREMENT)
# );
# """)

print('customer id, name')
# select field list FROM table_name
cursor.execute('SELECT id, name FROM customer')
for row in cursor:
     print(row)


# join connects the two tables ON the matching fields
cursor.execute("""
select 'order'.id as 'order id', customer.name, 'order'.total, product.name, product.price, quantity from 'order' 
join customer on customer.id = 'order'.customer_id
join order_item on order_item.order_id = 'order'.id
join product on product.id = order_item.product_id
""")
print('name, order_total')
for row in cursor:
     print(row)


print('C - Customer Operations')
print('P - Product Operations')
print('O - Order Operations')

table = input()

print('1 - List all')
print('2 - Add new')
print('3 - Update')
print('4 - Delete')

operation = input()

table_name = { 'C' : 'Customer', 'P' : 'Product', 'O' : "'Order'" }

if operation == '1':
     # string substitution for TABLE NAME only, NOT USER INPUTED DATA
     cursor.execute(f'select * from {table_name[table]}')
     for row in cursor:
          print(row)

elif operation == '3':
     pass
     # update 'order' set customer_id = 2, total = 1000 where id = 4

elif operation == '4':
     # don't delete items that are referenced in other tables
     id = int(input("Enter the id to delete"))
     cursor.execute(f'delete from {table_name[table]} where id = ?', [id])
     connection.commit()

customer_name = input("Enter a new customer name")

cursor.execute('INSERT INTO customer (name) VALUES (?)', [customer_name])

# saves the change
connection.commit()