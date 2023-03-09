from order.functions import ReadOrders, DumpOrders


class Order():
    def __init__(self, Order, Customer, Price=0, IsReady=False):
        self.Order: list = Order
        self.Customer: int = Customer
        self.Price: int = Price
        self.IsReady: bool = IsReady

    def CalcPrice(self):
        price = 0
        for product in self.Order:
            ProductSum = product["price"] * product["count"]
            price += ProductSum

        self.Price = price

    def DumpOrder(self):
        if self.Price == 0:
            self.CalcPrice()

        Orders = ReadOrders()
        OrderId = len(Orders["orders"])+1
        Orders["orders"].append(
            {"Order": self.Order, "Customer": self.Customer, "Price": self.Price, "IsReady": self.IsReady})
        DumpOrders(Orders)
        return OrderId, self.Price
