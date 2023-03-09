from product.functions import ReadProducts, DumpProducts


class Product():
    def __init__(self, Name, Price):
        self.Name: list = Name
        self.Price: int = Price
        self.Id = None

    def json(self):
        return {"Name": self.Name, "Price": self.Price, "Id": self.Id}

    def DumpProduct(self) -> int:
        Products = ReadProducts()
        ProductId = len(Products["products"])+1
        Products["products"].append(self.json)
        DumpProducts(Products)
        self.Id = ProductId
        return ProductId
