# -*- coding: utf-8 -*-
from database import Database
class GildedRose(object):

    def __init__(self, items):
        self.items = items
    #print(items)	
    	
    def update_quality(self):
        #for item in self.items:
        for i in range(len(self.items)):
            if self.items[i].name != "Aged Brie" and self.items[i].name != "Backstage passes to a TAFKAL80ETC concert":
                if self.items[i].quality > 0:
                    if self.items[i].name != "Sulfuras, Hand of Ragnaros":
                        self.items[i].quality = max(0,self.items[i].quality - 2) if self.items[i].name == "Conjured" else self.items[i].quality - 1
            else:
                if self.items[i].quality < 50:
                    self.items[i].quality = self.items[i].quality + 1
                    if self.items[i].name == "Backstage passes to a TAFKAL80ETC concert":
                        if self.items[i].sell_in < 11:
                            if self.items[i].quality < 50:
                                self.items[i].quality = self.items[i].quality + 2
                        if self.items[i].sell_in < 6:
                            if self.items[i].quality < 50:
                                self.items[i].quality = self.items[i].quality + 3
            if self.items[i].name != "Sulfuras, Hand of Ragnaros":
                self.items[i].sell_in = self.items[i].sell_in - 1
            if self.items[i].sell_in < 0:
                if self.items[i].name != "Aged Brie":
                    if self.items[i].name != "Backstage passes to a TAFKAL80ETC concert":
                        if self.items[i].quality > 0:
                            if self.items[i].name != "Sulfuras, Hand of Ragnaros":
                                self.items[i].quality = max(0,items[i].quality - 2) if self.items[i].name == "Conjured" else self.items[i].quality - 1
                    else:
                        self.items[i].quality = self.items[i].quality - self.items[i].quality
                else:
                    if self.items[i].quality < 50:
                        self.items[i].quality = self.items[i].quality + 1
        database = Database('database.db')
        database.update_database(self.items)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
