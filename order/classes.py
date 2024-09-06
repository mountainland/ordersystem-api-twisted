from .functions import CreateOrder


class Order:
    def __init__(
        self,
        Order: list,
        Customer: int,
        Price: int = 0,
        IsReady: bool = False,
        Picked: bool = False,
    ):
        self.Order: list = Order
        self.Customer: int = Customer
        self.Price: int = Price
        self.IsReady: bool = IsReady
        self.Picked: bool = Picked

    def CalcPrice(self):
        price = 0
        for product in self.Order:
            ProductSum = product["price"] * product["count"]
            price += ProductSum

        self.Price = price

    def DumpOrder(self):
        if self.Price == 0:
            self.CalcPrice()

        ID = CreateOrder(
            {
                "order": self.Order,
                "customer": self.Customer,
                "price": self.Price,
                "is_ready": self.IsReady,
                "picked": self.Picked,
            }
        )
        return ID, self.Price
