import json

from db.db import get_connection


def ReadOrders(times=0) -> dict:
    myclient = get_connection()
    mydb = myclient["ordersystem"]
    mycol = mydb["orders"]

    return mycol


def GetOrder(OrderId: int) -> dict:
    Orders = ReadOrders()
    query = {"_id": OrderId}
    OrderToReturn = Orders.find(query)

    return OrderToReturn


def SetOrder(OrderId: int, Order: dict) -> None:    
    Orders = ReadOrders()
    query = {"_id": OrderId}
    new = {"$set": Order}
    Orders.update_one(query, new)