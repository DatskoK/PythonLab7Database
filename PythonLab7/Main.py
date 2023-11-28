from switch import Switch
from Function import Function
from Database import Database
from Chair import Chair
from Bookshelf import Bookshelf

F = Function()

data_list_chair = Database.getData(Chair)
data_list_bookshelf = Database.getData(Bookshelf)
data_list_all = data_list_chair + data_list_bookshelf

def printString(function):
    for f in function:
        print(f)

while True:
    print()
    print("Select the list you want to work with:")
    print("a) All lists;")
    print("b) Chair;")
    print("c) Bookshelf;")
    print("q) Exit")

    choice_list = input("Your list: ")
    print()
    with Switch(choice_list) as case:
        if case('a'):
            data_list = data_list_all
        if case('b'):
            data_list = data_list_chair
        if case('c'):
            data_list = data_list_bookshelf
        if case('q'):
            break
        if case.default:
            print("Wrong choice. Please try again.")
            
    while True:
        print()
        print("Select a task from the list:")
        print("a) a list of furniture of a given name;")
        print("b) a list of furniture of a certain manufacturer, the price of which is within certain limits;")
        print("c) a list of furniture sorted by material, then by name.")
        print("d) add new furniture to the list;")
        print("e) remove furniture from the list;")
        print("q) Back")

        choice = input("Your choice: ")
        print()
        with Switch(choice) as case:
            if case('a'):
                name = input("Enter the name of the furniture: ")
                printString(F.listFurnitureSpecifiedName(data_list, name))
            if case('b'):
                manufacturer = input("Enter the furniture manufacturer: ")
                try:
                    minPrice = int(input("Enter the minimum price: "))
                    maxPrice = int(input("Enter the maximum price: "))
                except ValueError:
                    printString(F.listFurnitureCertainManufacturerWithinPriseLimits(data_list, manufacturer, minPrice, maxPrice))
            if case('c'):
                printString(F.listFurnitureSortedMaterialThenName(data_list))
            if case('d'):
                id = int(input("Id: "))
                if F.isIdValid(data_list, id) or data_list == data_list_all:
                    print("Furniture with such an id already exists.")
                else:
                    name = input("Name: ")
                    weight = input("Weight: ")
                    manufacturer = input("Manufacturer: ")
                    price = input("Price: ")
                    length = input("Lenght: ")
                    width = input("Width: ")
                    height = input("Height: ")
                    material = input("Material: ")
                    if data_list == data_list_chair:
                        extra = input("Legs: ")
                        Database.addNewChairData(id, name, weight, manufacturer, price, length, width, height, material, extra)
                        data_list = Database.getData(Chair)
                    else:
                        extra = input("Shelves: ")
                        Database.addNewBookshelfData(id, name, weight, manufacturer, price, length, width, height, material, extra)
                        data_list = Database.getData(Bookshelf)
            if case ('e'):
                if data_list == data_list_all:
                    print("Unable to execute on a shared list.")
                else:
                    id = int(input("Id: "))
                    if data_list == data_list_chair:
                        Database.deleteDataById(Chair, id)
                        data_list = Database.getData(Chair)
                    else:
                        Database.deleteDataById(Bookshelf, id)
                        data_list = Database.getData(Bookshelf)
            if case('q'):
                break
            if case.default:
                print("Wrong choice. Please try again.")