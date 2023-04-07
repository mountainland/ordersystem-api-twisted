import json

from db.db import get_connection

def ReadProducts() -> dict: # TODO: Name isn't good, should probably be something, that lets you know, this is database
    myclient = get_connection()
    mydb = myclient["ordersystem"]
    collist = mydb.list_collection_names() # TODO: This doesnt do anything, remove when you can
    mycol = mydb["products"]

    return mycol


def DumpProducts(orders: dict) -> None:
    raise DeprecationWarning("DumpProducts() is deprecated") # TODO: This function is deprecated, and should be remowed from anywhere.


def GetProduct(ProductId: int) -> dict:
    Products = ReadProducts()
    query = {"_id": ProductId}
    ProductToReturn = Products.find(query)
    return ProductToReturn


def SetProduct(ProductId: int, Product: dict) -> None:
    Products = ReadProducts()
    query = {"_id": ProductId}
    new = {"$set": Product}
    Products.update_one(query, new)