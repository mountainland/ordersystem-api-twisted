import json


def ReadOrders(times=0) -> dict:
    with open("data.json", "r") as f:
        data = json.load(f)
        return data


def DumpOrders(orders: dict) -> None:
    with open("data.json", "w") as f:
        json.dump(orders, f)


def GetOrder(OrderId: int) -> dict:
    Orders = ReadOrders()
    OrderToReturn = Orders["orders"][OrderId]

    return OrderToReturn


def SetOrder(OrderId: int, Order: dict) -> None:
    Orders = ReadOrders()
    Orders[OrderId] = Order
    DumpOrders(Orders)
