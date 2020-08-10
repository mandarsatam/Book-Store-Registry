import sqlite3


class Database():

	def __init__(self):
		self.conn=sqlite3.connect("books.db")
		self.cur = self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, name TEXT, author TEXT, year INTEGER, isbn INTEGER )")
		self.conn.commit()

	def insert(self, name, author, year, isbn):
		self.cur.execute("INSERT INTO book VALUES(NULL, ?, ?, ?, ?)", (name, author, year, isbn))
		self.conn.commit()


	def view(self):
		self.cur.execute("SELECT * FROM book")
		rows=self.cur.fetchall()
		return rows

	def search(self, name="", author="", year="", isbn=""):
		self.cur.execute("SELECT * FROM book WHERE name= ? OR author=? OR year=? OR isbn=?", (name, author, year, isbn))
		row=self.cur.fetchall()
		return row

	def delete(self, id1):
		self.cur.execute("DELETE FROM book WHERE id=?", (id1,))
		self.conn.commit()


	def update(self, id1, name, author, year, isbn):
		self.cur.execute("UPDATE book SET name=?, author=?, year=?, isbn=? WHERE id=?", (name, author, year, isbn, id1))
		self.conn.commit()


	def __del__(self):
		self.conn.close()












