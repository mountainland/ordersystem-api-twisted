from product.functions import ReadProducts, DumpProducts, CreateProduct

class Product():
    def __init__(self, Name, Price):
        self.Name: str = Name
        self.Price: int = Price
        self.Id = None

    def DumpProduct(self) -> int:
        ID = CreateProduct({"name": self.Name, "price": self.Price})
        return ID
