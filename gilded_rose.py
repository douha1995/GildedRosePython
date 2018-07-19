class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in

        self.quality = 80 if name == 'Sulfuras, Hand of Ragnaros' else quality

    def update_backstage_pass(self):
        if self.sell_in < 0:
            self.quality = 0
            return

        self.quality += 1

        if self.sell_in < 11:
            self.quality += 1
        if self.sell_in < 6:
            self.quality += 1

    def update(self):
        if self.name == "Sulfuras, Hand of Ragnaros":
            return

        self.sell_in -= 1

        if self.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_pass()
        elif self.name == "Aged Brie":
            self.quality += (self.quality < 50)
        elif self.name == "Conjured":
            self.quality -= 2
        else:
            self.quality -= 1

        if self.quality > 50:
            self.quality = 50
        elif self.quality < 0:
            self.quality = 0

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
