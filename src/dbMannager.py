import sqlite3

class DataBaseManager():
	def __init__(self, data_base):
		self.conn = sqlite3.connect(data_base)
		self.cur = self.conn.cursor()
	
	def makeTable(self, name, culomns={}):
		sql = "CREATE TABLE IF NOT EXISTS "+name+" (\n\t"
		for ind in culomns:
			sql += str(ind)+ " " + str(culomns[ind]) +"\n\t"
		sql += ");"
		return self.conn.execute(sql)
	
	def insert(self, table, values={}):
		sql = "INSERT INTO "+str(table)+" ("
		for ind, val in enumerate(values):
			if ind == 0:
				sql += "`"+val+"`"
			else:
				sql += ", `"+val+"`"
		sql += ")\nVALUES ("
		for ind, val in enumerate(values):
			if ind == 0:
				if not isinstance(values[val], (int, float)):
					sql += "\""+str(values[val])+"\""
				else:
					sql += str(values[val])
			else:
				if not isinstance(values[val], int):
					sql += ", \""+str(values[val])+"\""
				else:
					sql += ", "+str(values[val])
		sql += ")"
		return self.conn.execute(sql)
	
	def getRows(self, table):
		self.cur.execute("select * from `"+str(table)+"`")
		return self.cur.fetchall()
	
	def clear(self, table):
		return self.conn.execute("DELETE FROM "+str(table)+";")
	
	def close(self):
		self.conn.commit()
		self.conn.close()