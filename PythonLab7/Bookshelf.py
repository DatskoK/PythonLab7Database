from Furniture import Furniture

class Bookshelf(Furniture):
    def __init__(self, id=0, name="", weight=0, manufacturer="", price=0, dimensions=(0, 0, 0), material="", shelves=5):
        super().__init__(id, name, weight, manufacturer, price, dimensions, material)
        self._shelves = shelves

    def __str__(self):
        return super().__str__() + f", Number of Shelves: {self._shelves}"