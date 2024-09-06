from db.db import get_connection, set_item, get_item, create_item, get_items, get_all


def ReadCustomers() -> dict:
    # This is deprecated and will be removed in a future release
    raise DeprecationWarning("ReadCustomers is deprecated")


def GetCustomer(CustomerId, recalculate=True) -> dict:
    CustomerToReturn = get_item(
        get_connection(), "ordersystem", "customers", {"ID": CustomerId}
    )
    print(CustomerToReturn)
    CustomerToReturn["balance"] = int(CustomerToReturn["balance"])
    if recalculate:
        CustomerToReturn["balance"] -= int(CalcCustomer(CustomerId))
    return CustomerToReturn


def create_customer(customer_dict):
    ID = create_item(get_connection(), "ordersystem", "customers", customer_dict)
    return ID


def CalcCustomer(CustomerId):
    Orders = get_items(
        get_connection(), "ordersystem", "orders", {"customer": CustomerId}
    )
    Sum = 0

    for Order in Orders:
        # This was earlier -=, and it caused bug, that made infinite money glich.
        Sum += Order["price"]

    return Sum


def SetCustomer(Customerid, data, admin=False):
    if admin:
        if "balance" in data:
            if data["balance"].startswith("="):
                data["balance"] = data["balance"].replace("=", "")
                data["balance"] = int(data["balance"])
                data["balance"] += CalcCustomer(Customerid)
            else:
                data["balance"] = int(data["balance"])
                custo = GetCustomer(Customerid, False)
                balance = custo.get("balance")

                data["balance"] += balance

    query = {"ID": Customerid}
    # if you remove $set this wont work: https://www.mongodb.com/docs/manual/reference/operator/update/set/
    new = {"$set": data}
    set_item(get_connection(), "ordersystem", "customers", query, new)


def GetCustomers():
    customers = get_all(get_connection(), "ordersystem", "customers")

    return customers
