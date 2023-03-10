from product.functions import ReadProducts, DumpProducts


class Product():
    def __init__(self, Name, Price):
        self.Name: str = Name
        self.Price: int = Price
        self.Id = None

    def DumpProduct(self) -> int:
        if type(self.Name) != str or type(self.Price) != int:
            raise TypeError("YOURE MONSTER")
        Products = ReadProducts()
        ProductId = len(Products["products"])+1
        self.Id = ProductId
        Products["products"].append(
            {"Name": self.Name, "Price": self.Price, "Id": self.Id})
        DumpProducts(Products)
        self.Id = ProductId
        return ProductId
