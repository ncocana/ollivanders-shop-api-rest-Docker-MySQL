import pytest
from logic.GildedRose import (
    GildedRose,
    Item,
    NormalItem,
    ConjuredItem,
    AgedBrie,
    Sulfuras,
    Backstage,
)


# Test for NormalItem class.


@pytest.mark.test_update_quality
def test_normal_item():
    normal_item = NormalItem("Normal Item", 10, 20)
    gilded_rose = GildedRose([normal_item])
    gilded_rose.update_quality()
    assert normal_item.sell_in == 9
    assert normal_item.quality == 19


# The quality of an item is never more than 50.
@pytest.mark.test_update_quality
def test_normal_item_quality_no_more_than_fifty():
    normal_item = NormalItem("Normal Item", 10, 52)
    gilded_rose = GildedRose([normal_item])
    gilded_rose.update_quality()
    assert normal_item.sell_in == 9
    assert normal_item.quality == 50


# Once the sell by date has passed, quality degrades twice as fast.
@pytest.mark.test_update_quality
def test_normal_item_date_passed():
    normal_item = NormalItem("Normal Item", 0, 20)
    gilded_rose = GildedRose([normal_item])
    gilded_rose.update_quality()
    assert normal_item.sell_in == -1
    assert normal_item.quality == 18


# The quality of an item is never negative.
@pytest.mark.test_update_quality
def test_normal_item_quality_not_negative():
    normal_item = NormalItem("Normal Item", 1, 0)
    gilded_rose = GildedRose([normal_item])
    gilded_rose.update_quality()
    assert normal_item.sell_in == 0
    assert normal_item.quality == 0


# Test for ConjuredItem class.


# Quality degrades twice as fast as normal items.
@pytest.mark.test_update_quality
def test_conjured_item():
    conjured_item = ConjuredItem("Conjured Item", 5, 30)
    gilded_rose = GildedRose([conjured_item])
    gilded_rose.update_quality()
    assert conjured_item.sell_in == 4
    assert conjured_item.quality == 28


# Test for AgedBrie class.


# Increase in quality the older it gets.
@pytest.mark.test_update_quality
def test_aged_brie():
    aged_brie = AgedBrie("Aged Brie", 2, 0)
    gilded_rose = GildedRose([aged_brie])
    gilded_rose.update_quality()
    assert aged_brie.sell_in == 1
    assert aged_brie.quality == 1


# Increase in quality the older it gets.
@pytest.mark.test_update_quality
def test_aged_brie_date_passed():
    aged_brie = AgedBrie("Aged Brie", 0, 0)
    gilded_rose = GildedRose([aged_brie])
    gilded_rose.update_quality()
    assert aged_brie.sell_in == -1
    assert aged_brie.quality == 2


# Test for Sulfuras class.


# Sell_in and quality do not change.
@pytest.mark.test_update_quality
def test_sulfuras():
    sulfuras = Sulfuras("Sulfuras", 0, 80)
    gilded_rose = GildedRose([sulfuras])
    gilded_rose.update_quality()
    assert sulfuras.sell_in == 0
    assert sulfuras.quality == 80


# Test for Backstage class.


# Quality increases by 1 when there are more than 10 days.
@pytest.mark.test_update_quality
def test_backstage_normal():
    backstage = Backstage("Backstage Passes", 15, 20)
    gilded_rose = GildedRose([backstage])
    gilded_rose.update_quality()
    assert backstage.sell_in == 14
    assert backstage.quality == 21


# Quality increases by 2 when there are 10 days or less.
@pytest.mark.test_update_quality
def test_backstage_ten_days_or_less():
    backstage = Backstage("Backstage Passes", 10, 20)
    gilded_rose = GildedRose([backstage])
    gilded_rose.update_quality()
    assert backstage.sell_in == 9
    assert backstage.quality == 22


# Quality increases by 3 when there are 5 days or less.
@pytest.mark.test_update_quality
def test_backstage_five_days_or_less():
    backstage = Backstage("Backstage Passes", 5, 20)
    gilded_rose = GildedRose([backstage])
    gilded_rose.update_quality()
    assert backstage.sell_in == 4
    assert backstage.quality == 23


# Quality drops to 0 after the concert.
@pytest.mark.test_update_quality
def test_backstage_after_concert():
    backstage = Backstage("Backstage Passes", 0, 20)
    gilded_rose = GildedRose([backstage])
    gilded_rose.update_quality()
    assert backstage.sell_in == -1
    assert backstage.quality == 0
