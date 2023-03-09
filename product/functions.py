import json


def ReadProducts() -> dict:
    with open("order.json", "r") as f:
        return json.load(f)


def DumpProducts(orders) -> None:
    with open("order.json", "w") as f:
        json.dump(orders, f)


def GetProduct(OrderId) -> dict:
    Products = ReadProducts()
    ProductToReturn = Products["orders"][OrderId]

    return ProductToReturn


def SetProduct(ProductId, Product: dict) -> None:
    Products = ReadProducts()
    Products[ProductId] = Product
    DumpProducts(Product)
