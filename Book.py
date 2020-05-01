import itertools as it

class Book:
    bid_iter = it.count(1, 1)

    def __init__(self, *args):
        self.bid = next(self.bid_iter)
        self.title = args[0]
        self.author = args[1]
        self.category = args[2]
        self.pages = args[3]
        self.publisher = args[4]
        self.price_cat = args[5]
        self.rented_by = "0"

    def __str__(self):
        return "{:<6}{:<60}{:<20}{:<10}{:<4}{:<20}{:<4}".format(self.bid, self.title, self.author, self.category,
                                                                self.pages, self.publisher, self.price_cat)
