from db.db import get_connection, set_item, get_item, create_item, get_all


def GetOrders():
    all = get_all(get_connection(), "ordersystem", "orders")
    return all


def ReadOrders(times=0) -> dict:
    raise DeprecationWarning("ReadOrders is deprecated")


def CreateOrder(Order):
    ID = create_item(get_connection(), "ordersystem", "orders", Order)
    return ID


def GetOrder(OrderId: int) -> dict:
    OrderToReturn = get_item(get_connection(), "ordersystem", "orders", {"ID": OrderId})
    return OrderToReturn


def SetOrder(OrderId: int, Order: dict) -> None:
    query = {"ID": OrderId}
    new = {"$set": Order}
    set_item(get_connection(), "ordersystem", "orders", query, new)
