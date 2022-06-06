
from json import loads, dumps
from random import uniform, choice
from itertools import cycle
from time import sleep
from dbMannager import DataBaseManager
import sqlite3


con = DataBaseManager("../data/users.sqlite")
con.makeTable("user", {
	"id": "intger PRIMARY KEY,",
	"name": "text NOT NULL,",
	"level": "integer,",
	"credits": "integer"
})


def convertToSqlite():
	con.clear("user")
	data = []
	with open("../data/users.json", "r") as f:
		data = loads(f.read())
	
	for ind, val in enumerate(data):
		con.insert("user", {
			"id": ind,
			"name": val["name"],
			"age": val["age"],
			"level": val["level"],
			"credits": val["credits"]
		})

def addUsers():
	data = []
	with open("../data/users.json", "r") as f:
		data = loads(f.read())
	
	names = ("othman", "yassin", "ahmed", "ilyas")
	dataCycle = cycle((
		(15, 20),
		(0, 130),
		(0, 200000)
	))
	
	with open("../data/users.json", "w") as f:
		res = {}
		for _ in range(200):
			for j in ("name", "age", "level", "credits"):
				if j == "name":
					res[j] = choice(names)
				else:
					res[j] = round(uniform(*next(dataCycle)))
			data.append(res)
			res = {}
		f.write(dumps(data, indent=2))

#addUsers()
#convertToSqlite()


'''
[
	{
		"name": "hesham",
		"age": 17,
		"level": 20,
		"credits": 80000
	}
]
'''