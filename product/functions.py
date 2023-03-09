import json


def ReadProducts() -> dict:
    with open("data.json", "r") as f:
        return json.load(f)


def DumpProducts(orders) -> None:
    with open("data.json", "w") as f:
        json.dump(orders, f)


def GetProduct(ProductId: int) -> dict:
    Products = ReadProducts()
    ProductToReturn = Products[ProductId]
    return ProductToReturn


def SetProduct(ProductId, Product: dict) -> None:
    Products = ReadProducts()
    Products[ProductId] = Product
    DumpProducts(Product)
