import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def testNotSpecialItemQualityDecreasesBy1(self):
        items = [Item("normal item", 10, 2)]

        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(gilded_rose.items[0].quality, 1)

    def testAgedBrieQualityIncreases(self):
        items = [Item("Aged Brie", 10, 0)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(gilded_rose.items[0].quality, 1)
        self.assertEqual(gilded_rose.items[0].sell_in, 9)

    def testAgedBrieQualityNeverExceeds50(self):
        items = [Item("Aged Brie", 10, 10)]

        gilded_rose = GildedRose(items)

        for i in range(50):
            gilded_rose.update_quality()

        self.assertEqual(gilded_rose.items[0].quality, 50)

    def testAgedBrieSellInDecreasesBy1(self):
        items = [Item("Aged Brie", 10, 0)]

        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(gilded_rose.items[0].sell_in, 9)

    def testBackStagePassesQualityIncreasesBy1IfSellInIsMoreThan10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 20, 0)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(gilded_rose.items[0].quality, 1)

    def testBackStagePassesQualityIncreasesBy2IfSellInIsEqualTo10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 0)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(gilded_rose.items[0].quality, 2)

    def testBackStagePassesQualityIncreasesBy2IfSellInIsLessThan10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 9, 0)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(gilded_rose.items[0].quality, 2)

    def testBackStagePassesQualityIncreasesBy3IfSellInIsEqualTo5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 0)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(gilded_rose.items[0].quality, 3)

    def testBackStagePassesQualityIncreasesBy3IfSellInIsLess5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 0)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(gilded_rose.items[0].quality, 3)

    def testBackStagePassesQualityIs0IfSellInDateIsNegative(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(gilded_rose.items[0].quality, 0)

    def testBackStagePassesQualityNeverExceeds50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 50, 10)]

        gilded_rose = GildedRose(items)

        for i in range(50):
            gilded_rose.update_quality()

        self.assertEqual(gilded_rose.items[0].quality, 50)

    def testBackStagePassesSellInDecreasesBy1(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 0)]

        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(gilded_rose.items[0].sell_in, 9)

    def testSulfurasQualityNeverAlters(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 0)]

        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(gilded_rose.items[0].quality, 80)

    def testSulfurasSellInNeverAlters(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 13, 0)]

        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(gilded_rose.items[0].sell_in, 13)

    def testConjuredItemQualityDecreasesBy2(self):
        items = [Item("Conjured", 10, 2)]

        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(gilded_rose.items[0].quality, 0)

    def testConjuredSellInDecreasesBy1(self):
        items = [Item("Conjured", 10, 0)]

        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(gilded_rose.items[0].sell_in, 9)


if __name__ == '__main__':
    unittest.main()
