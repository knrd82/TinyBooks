import itertools as it

class Book:
    bid_iter = it.count(1, 1)

    def __init__(self, **kwargs):
        self.bid = next(self.bid_iter)
        self.title = kwargs.get("title")
        self.author = kwargs.get("author")
        self.category = kwargs.get("category")
        self.pages = kwargs.get("pages")
        self.publisher = kwargs.get("publisher")
        self.price_cat = kwargs.get("pricecat")

    def __str__(self):
        return "{:<6}{:<40}{:<20}{:<10}{:<4}{:<15}{:<4}".format(self.bid, self.title, self.author, self.category,
                                                                self.pages, self.publisher, self.price_cat)
