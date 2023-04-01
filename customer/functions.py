import json

from order import functions


def ReadCustomers() -> dict:
    with open("data.json", "r") as f:
        data = json.load(f)
        return data


def DumpCustomers(customers) -> None:
    with open("data.json", "w") as f:
        json.dump(customers, f)


def GetCustomer(CustomerId) -> dict:
    Customers = ReadCustomers()
    CustomerToReturn = Customers["customers"][CustomerId]
    CustomerToReturn["Balance"] -= CalcCustomer(CustomerId)
    return CustomerToReturn


def CalcCustomer(CustomerId):
    Orders = functions.ReadOrders()["customers"]

    Sum = 0

    for Order in Orders:
        if Order["Customer"] == CustomerId:
            Sum -= Order["Price"]

    return Sum

def SetCustomer(Customerid, data):
    customers = ReadCustomers()

    customers["customers"][Customerid] = data

    DumpCustomers(customers)
