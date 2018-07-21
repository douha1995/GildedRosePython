import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('INSERT INTO items values ("Aged Brie",11,10);')
conn.execute('INSERT INTO items values ("Sulfuras, Hand of Ragnaros",11,80);')
conn.execute('INSERT INTO items values ("Backstage passes to a TAFKAL80ETC concert",11,10);')
conn.execute('INSERT INTO items values ("Conjured",11,10);')
print ("Inserted dummy records.")
conn.close()
