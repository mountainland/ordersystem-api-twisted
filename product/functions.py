import json


def ReadProducts() -> dict:
    with open("data.json", "r") as f:
        data = json.load(f)
        return data


def DumpProducts(orders: dict) -> None:
    with open("data.json", "w") as f:
        json.dump(orders, f)


def GetProduct(ProductId: int) -> dict:
    Products = ReadProducts()
    ProductToReturn = Products[ProductId]
    return ProductToReturn


def SetProduct(ProductId: int, Product: dict) -> None:
    Products = ReadProducts()
    Products[ProductId] = Product
    DumpProducts(Product)

