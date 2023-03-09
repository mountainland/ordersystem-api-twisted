from order.functions import ReadOrders, DumpOrders
from product.classes import Product
from product.functions import 

class Order():
    def __init__(self, Order, Customer, Price=0, IsReady=False):
        self.Order: list = Order
        self.Customer: int = Customer
        self.Price: int = Price
        self.IsReady: bool = IsReady

    def json(self):
        return {"Order": self.Order, "Customer": self.Customer, "Price": self.Price, "IsReady": self.IsReady}

    def CalcPrice(self):
        price = 0
        for product in self.Order:
            ProductSum = product["price"] * product["count"]
            price += ProductSum

        self.Price = price

    def DumpOrder(self) -> int:
        if self.Price == 0:
            self.CalcPrice()

        Orders = ReadOrders()
        OrderId = len(Orders["orders"])+1
        Orders["orders"].append(self.json)
        DumpOrders(Orders)
        return OrderId, self.Price
