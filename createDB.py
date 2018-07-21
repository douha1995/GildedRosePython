import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE items (rowid integer auto_increment primary key,name TEXT, sell_in INT, quality INT)')
print ("Table created successfully")

conn.execute('INSERT INTO items values (1,"Aged Brie",11,10);')
conn.execute('INSERT INTO items values (2,"Sulfuras, Hand of Ragnaros",11,80);')
conn.execute('INSERT INTO items values (3,"Backstage passes to a TAFKAL80ETC concert",11,10);')
conn.execute('INSERT INTO items values (4,"Conjured",11,10);')
conn.execute('INSERT INTO items values (5,"Aged Brie",11,10);')
conn.execute('INSERT INTO items values (6,"Sulfuras, Hand of Ragnaros",11,80);')
conn.execute('INSERT INTO items values (7,"Conjured",11,10);'	)
conn.execute('INSERT INTO items values (8,"Backstage passes to a TAFKAL80ETC concert",11,10);')
conn.commit()

print ("Dummy values inserted.")
conn.close()
