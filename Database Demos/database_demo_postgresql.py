import psycopg2

def create_table():
	conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' post=''")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
	conn.commit()
	conn.close()

def insert1(item, quantity, price):
	conn = psycopg2.connect("lite.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO store VALUES(?, ?, ?)", (item, quantity, price))
	conn.commit()
	conn.close()

#insert1("Water", 2, 10.5)
#insert1("Coffee", 3, 30.5)

def view():
	conn = psycopg2.connect("lite.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM store")
	rows=cur.fetchall()
	conn.close()
	return rows

def delete(item):
	conn = psycopg2.connect("lite.db")
	cur = conn.cursor()
	cur.execute("DELETE FROM store WHERE item= ?", (item,))
	conn.commit()
	conn.close()

def update(quantity, price, item):
	conn = psycopg2.connect("lite.db")
	cur = conn.cursor()
	cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity, price, item))
	conn.commit()
	conn.close()


#delete("Coffee")
update(30, 56,"Wine Glass")


print(view())

	