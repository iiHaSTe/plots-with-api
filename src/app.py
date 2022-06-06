
from fastapi import FastAPI
from json import load, dumps
import sqlite3


app = FastAPI()



con = sqlite3.connect("./data/users.sqlite")



@app.get("/users/")
def get_user_item(user_id: int=None, item: str=None):
	users = load(open("./data/users.json", "r"))
	try:
		if item is None and user_id is None:
			return users
		elif (not user_id is None) and item is None:
			return users[user_id-1]
		elif not (user_id is None and item is None):
			return users[user_id-1][item]
	except IndexError:
		return {
			"title": "error",
			"msg": f"out of range \n(max length of this list is {len(users)})"
		}
	except KeyError:
		return {
			"title": "error",
			"msg": "'"+item+"'"+" is not found in dictionary"
		}
con.close()
