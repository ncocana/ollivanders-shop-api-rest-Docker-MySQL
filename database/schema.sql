DROP TABLE IF EXISTS inventory;

CREATE TABLE inventory (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    sell_in INT NOT NULL,
    quality INT NOT NULL,
    class_object TEXT NOT NULL
);

INSERT INTO inventory (name, sell_in, quality, class_object) VALUES ("+5 Dexterity Vest", 10, 20, "ConjuredItem"),
        ("Aged Brie", 2, 0, "AgedBrie"),
        ("Elixir of the Mongoose", 5, 7, "NormalItem"),
        ("Sulfuras; Hand of Ragnaros", 0, 80, "Sulfuras"),
        ("Sulfuras; Hand of Ragnaros", -1, 80, "Sulfuras"),
        ("Backstage passes to a TAFKAL80ETC concert", 15, 20, "Backstage"),
        ("Backstage passes to a TAFKAL80ETC concert", 10, 49, "Backstage"),
        ("Backstage passes to a TAFKAL80ETC concert", 5, 49, "Backstage"),
        ("Conjured Mana Cake", 3, 6, "ConjuredItem")
