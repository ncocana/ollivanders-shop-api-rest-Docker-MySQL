class GildedRose(object):
    def __init__(self, items):
        self.items = items

    # Updates quality.
    def update_quality(self):
        for item in self.items:
            item.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class NormalItem(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    # Lowers the value of Sell_in by 1.
    def setSell_in(self):
        self.sell_in = self.sell_in - 1

    # The goods are constantly degrading in quality
    # as they approach their sell by date.
    def setQuality(self, valor):
        # The Quality of an item is never more than 50.
        if self.quality + valor > 50:
            self.quality = 50

        elif 50 >= self.quality + valor >= 0:
            self.quality = self.quality + valor

        # The Quality of an item is never negative.
        else:
            self.quality = 0

        assert 0 <= self.quality <= 50, "%s's quality out of range" % (
            self.__class__.__name__
        )

    # At the end of each day, our system
    # lowers the values of Quality and
    # Sell_in for every item.
    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(-1)

        # Once the sell by date has passed,
        # Quality degrades twice as fast.
        else:
            self.setQuality(-2)
        self.setSell_in()


class ConjuredItem(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    # "Conjured" items degrade in Quality twice
    # as fast as normal items.
    def update_quality(self):
        if self.sell_in >= 0:
            self.setQuality(-2)

        self.setSell_in()


class AgedBrie(NormalItem):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    # "Aged Brie" actually increases in Quality
    # the older it gets.
    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)

        self.setSell_in()


class Sulfuras(NormalItem):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    # "Sulfuras", being a legendary item,
    # never has to be sold or decreases in Quality.
    def update_quality(self):
        pass


class Backstage(NormalItem):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    # "Backstage passes", like Aged Brie,
    # increases in Quality as its Sell_in value approaches.
    def update_quality(self):
        if self.sell_in > 10:
            self.setQuality(1)

        # Quality increases by 2 when there are
        # 10 days or less.
        elif 10 >= self.sell_in > 5:
            self.setQuality(2)

        # And by 3 when there are 5 days or less.
        elif 5 >= self.sell_in > 0:
            self.setQuality(3)

        # Quality drops to 0 after the concert.
        else:
            self.quality = 0

        self.setSell_in()
