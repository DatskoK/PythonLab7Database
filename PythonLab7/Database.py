import sqlite3

class Database:
    
    @staticmethod
    def createDB():
        with sqlite3.connect('Furniture.db') as db:
            cursor = db.cursor()
            query_1 = """ CREATE TABLE IF NOT EXISTS Bookshelf(id INTEGER PRIMARY KEY, name TEXT, weight INTEGER, manufacturer TEXT, price INTEGER, length INTEGER, width INTEGER, height INTEGER, material TEXT, shelves INTEGER)"""
            query_2 = """ CREATE TABLE IF NOT EXISTS Chair(id INTEGER PRIMARY KEY, name TEXT, weight INTEGER, manufacturer TEXT, price INTEGER, length INTEGER, width INTEGER, height INTEGER, material TEXT, legs INTEGER)"""
            cursor.execute(query_1)
            cursor.execute(query_2)

    @staticmethod
    def getData(select_class):
        table = select_class.__name__
        data_list = []
        with sqlite3.connect('Furniture.db') as db:
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()

            for row in rows:
                id, name, weight, manufacturer, price, length, width, height, material, extra = row
                dimensions = (length, width, height)
                furniture = select_class(id, name, weight, manufacturer, price, dimensions, material, extra)
                data_list.append(furniture)

        return data_list
    
    @staticmethod
    def addNewChairData(id, name, weight, manufacturer, price, length, width, height, material, legs):
        with sqlite3.connect('Furniture.db') as db:
            cursor = db.cursor()
            cursor.execute(f''' INSERT INTO Chair (id, name, weight, manufacturer, price, length, width, height, material, legs) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ''',
                      (id, name, weight, manufacturer, price, length, width, height, material, legs))
            db.commit()

    @staticmethod
    def addNewBookshelfData(id, name, weight, manufacturer, price, length, width, height, material, shelves):
        with sqlite3.connect('Furniture.db') as db:
            cursor = db.cursor()
            cursor.execute(f''' INSERT INTO Bookshelf (id, name, weight, manufacturer, price, length, width, height, material, shelves) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ''',
                      (id, name, weight, manufacturer, price, length, width, height, material, shelves))
            db.commit()

    @staticmethod
    def deleteDataById(select_class, id):
        furniture = select_class.__name__
        with sqlite3.connect('Furniture.db') as db:
            cursor = db.cursor()
            cursor.execute(f' DELETE FROM {furniture} WHERE id = ? ', (id,))
            db.commit()