from db.db import get_connection, create_item, get_item, set_item, get_items, get_all


def ReadProducts() -> (
    dict
):  # TODO: Name isn't good, should probably be something, that lets you know, this is database
    raise DeprecationWarning("ReadProducts() is deprecated, use GetProducts() instead")
    myclient = get_connection()
    mydb = myclient["ordersystem"]
    mycol = mydb["products"]

    return mycol


def DumpProducts(orders: dict) -> None:
    raise DeprecationWarning(
        "DumpProducts() is deprecated"
    )  # TODO: This function is deprecated, and should be remowed from anywhere.


def GetProduct(ProductId: int) -> dict:
    Product = get_item(get_connection(), "ordersystem", "products", {"ID": ProductId})

    return Product


def CreateProduct(Product):
    ID = create_item(get_connection(), "ordersystem", "products", Product)

    return ID


def SetProduct(ProductId: int, Product: dict) -> None:
    query = {"ID": ProductId}
    new = {"$set": Product}
    set_item(get_connection(), "ordersystem", "products", query, new)


def GetProducts():
    all = get_all(get_connection(), "ordersystem", "products")
    return all
