from flask import Flask,render_template
from gilded_rose import Item, GildedRose
from database import Database
app = Flask(__name__)  

 
@app.route("/")
def hello():
	database = Database("database.db")
  	items = database.read_database()
  	gilded_rose = GildedRose(items)
  	return render_template('index.html',**locals())
   

@app.route("/update")
def update():
  database = Database("database.db")
  items = database.read_database()
  rows=len(items);
		#print(rows);
  for i in range(rows):
  		items[i]=Item(items[i][1],items[i][2],items[i][3])
  gilded_rose = GildedRose(items)
  gilded_rose.update_quality()
  return render_template('index.html',**locals())
	
if __name__ == "__main__":
    app.run()
