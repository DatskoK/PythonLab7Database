class Function:

    @staticmethod 
    def listFurnitureSpecifiedName (data_list, name):
        return [f for f in data_list if f.get_name == name]

    @staticmethod         
    def listFurnitureCertainManufacturerWithinPriseLimits(data_list, manufacturer, min_price, max_price):
        return [f for f in data_list if f.get_manufacturer == manufacturer and min_price <= f.get_price <= max_price]
    
    @staticmethod
    def isIdValid(data_list, id):
        return any(f.get_id == id for f in data_list)

    
#---------------------------SORTED---------------------------

    @staticmethod
    def listFurnitureSortedId(data_list):
        return sorted(data_list, key=lambda f: (f.get_id))
    
    @staticmethod
    def listFurnitureSortedMaterialThenName(data_list):
        return sorted(data_list, key=lambda f: (f.get_material, f.get_name))