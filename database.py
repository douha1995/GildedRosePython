import sqlite3
#from gilded_rose import Item

class Database:
	def __init__(self, db_name):
		self.db_name = db_name
		
	def read_database(self):
		connHandle = sqlite3.connect("database.db")
		cursorCurrent = connHandle.cursor()
		cursorCurrent.execute('select rowid,* from items')
		resQuery = cursorCurrent.fetchall()
		rows=len(resQuery);
		#print(rows);
		#for i in range(1,rows):
  		#	items[i]=Item(resQuery[i][1],resQuery[i][2],resQuery[i][3])
  			
		connHandle.close()
		return resQuery

	
	def update_database(self,items):
		connHandle = sqlite3.connect("database.db")
		cursorCurrent = connHandle.cursor()
		print(len(items))
		for i in range(len(items)):
			cursorCurrent.execute(
			'update items set sell_in=' + str(items[i].sell_in) + ', quality=' + str(items[i].quality) + ' where rowid=' + str(i+1))
		connHandle.commit()
		connHandle.close()
