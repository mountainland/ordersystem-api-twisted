import json


def ReadCustomers() -> dict:
    with open("customer.json", "r") as f:
        return json.load(f)


def DumpCustomers(orders) -> None:
    with open("customer.json", "w") as f:
        json.dump(orders, f)


def GetCustomer(OrderId) -> dict:
    Customers = ReadCustomers()
    CustomerToReturn = Customers["customers"][OrderId]

    return CustomerToReturn

