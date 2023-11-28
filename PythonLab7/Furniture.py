class Furniture(object):
    def __init__(self, id=0, name="", weight=0, manufacturer="", price=0, dimensions=(0,0,0), material=""):
        self._id = id
        self._name = name
        self._weight = weight
        self._manufacturer = manufacturer
        self._price = price
        self._dimensions = dimensions
        self._material = material
    
    def __del__ (self):
        print(f"The Furniture object with id {self._id} is destroyed")

    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}, Weight: {self._weight}, Manufacturer: {self._manufacturer}, Price: {self._price}, Dimensions: {self._dimensions}, Material: {self._material}"

    @property
    def get_id(self):
        return self._id
    @property
    def get_name(self):
        return self._name
    @property
    def get_manufacturer(self):
        return self._manufacturer
    @property
    def get_price(self):
        return self._price
    @property
    def get_material(self):
        return self._material