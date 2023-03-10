from order.functions import ReadOrders, DumpOrders


class Order():
    def __init__(self, Order: list, Customer: int, Price: int=0, IsReady: bool=False):
        self.Order: list = Order
        if not type(Customer) == int:
            raise TypeError("Should be int")
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
        if type(self.Order) != list or type(self.Customer) != int or type(self.Price) != int:
            raise TypeError("YOU ARE MONSTER")
        if self.Price == 0:
            self.CalcPrice()

        Orders = ReadOrders()
        OrderId = len(Orders["orders"])+1
        Orders["orders"].append(
            {"Order": self.Order, "Customer": self.Customer, "Price": self.Price, "IsReady": self.IsReady})
        DumpOrders(Orders)
        return OrderId, self.Price
