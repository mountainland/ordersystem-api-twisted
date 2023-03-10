import json

from order import functions


def ReadCustomers() -> dict:
    with open("data.json", "r") as f:
        data = json.load(f)
        return data 


def DumpCustomers(orders) -> None:
    with open("data.json", "w") as f:
        json.dump(orders, f)


def GetCustomer(OrderId) -> dict:
    Customers = ReadCustomers()
    CustomerToReturn = Customers["customers"][OrderId]

    return CustomerToReturn


def CalcCustomer(CustomerId):
    Orders = functions.ReadOrders()

    Sum = 0

    for Order in Orders:
        if Order["Customer"] == CustomerId:
            Sum += Order["Price"]

    return Sum
            