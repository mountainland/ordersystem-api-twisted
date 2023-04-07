import json

from db.db import get_connection
from order import functions


def ReadCustomers() -> dict:
    myclient = get_connection()
    mydb = myclient["ordersystem"]
    mycol = mydb["customers"]

    return mycol


def GetCustomer(CustomerId) -> dict:
    Customers = ReadCustomers()
    CustomerToReturn = Customers.find({"_id": CustomerId})
    CustomerToReturn["balance"] -= CalcCustomer(CustomerId)
    return CustomerToReturn


def CalcCustomer(CustomerId):
    Orders = functions.ReadOrders()
    myquery = { "customer": CustomerId }

    customer_orders = Orders.find(myquery)

    Sum = 0

    for Order in customer_orders:
        Sum -= Order["price"]

    return Sum


def SetCustomer(Customerid, data):
    customers = ReadCustomers()

    new = {"$set": data}
    
    customers.update_one({"_id": Customerid}, new)