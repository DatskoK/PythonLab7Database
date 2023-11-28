from Furniture import Furniture

class Chair(Furniture):
    def __init__(self, id=0, name="", weight=0, manufacturer="", price=0, dimensions=(0, 0, 0), material="", legs=4):
        super().__init__(id, name, weight, manufacturer, price, dimensions, material)
        self._legs = legs

    def __str__(self):
        return super().__str__() + f", Legs: {self._legs}"