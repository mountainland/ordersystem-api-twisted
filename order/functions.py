import json


def ReadOrders() -> dict:
    with open("data.json", "r") as f:
        return json.load(f)


def DumpOrders(orders) -> None:
    with open("data.json", "w") as f:
        json.dump(orders, f)


def GetOrder(OrderId) -> dict:
    Orders = ReadOrders()
    OrderToReturn = Orders["orders"][OrderId]

    return OrderToReturn


def SetOrder(OrderId, Order: dict) -> None:
    Orders = ReadOrders()
    Orders[OrderId] = Order
    DumpOrders(Orders)
