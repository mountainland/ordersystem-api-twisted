from klein import run, route
import json

from order.classes import Order
from order.functions import ReadOrders, GetOrder, SetOrder
from product.classes import Product
from product.functions import ReadProducts, GetProduct, SetProduct
from customer.classes import Customer
from customer.functions import ReadCustomers, GetCustomer

from config import config

@route('/orders/', methods=["GET", "POST"])
def orders(request):
    if request.method == b"POST":
        content = json.loads(request.content.read())
        OrderItem = Order(content["order"], content["customer"])
        OrderId, Price = OrderItem.DumpOrder()
        return str({"status": "OK", "id": OrderId, "price": Price})

    if request.method == b"GET":
        return json.dumps({"orders": ReadOrders()["orders"]})


@route('/order/<int:OrderId>', methods=["GET", "POST"])
def order(request, OrderId):
    if request.method == b"POST":
        content = json.loads(request.content.read())
        if content["IsReady"] == True:
            item = GetOrder(OrderId)
        item["IsReady"] = content["IsReady"]
        SetOrder(OrderId, item)
        return str(item)

    if request.method == b"GET":
        OrderToReturn = GetOrder(OrderId)

        return str(OrderToReturn)


@route('/products/', methods=["GET", "POST"])
def products(request):
    if request.method == b"POST":
        content = json.loads(request.content.read())
        ProductItem = Product(content["Name"], content["Price"])
        ProductId = ProductItem.DumpProduct()
        return json.dumps({"status": "OK", "id": ProductId})

    if request.method == b"GET":
        return json.dumps({"products": ReadProducts()["products"]})



@route('/product/<int:ProductId>', methods=["GET", "POST"])
def product(request, ProductId):
    if request.method == b"POST":
        content = json.loads(request.content.read())
        if content["IsReady"] == True:
            item = GetProduct(ProductId)

        SetProduct(ProductId, item)
        return str(item)

    if request.method == b"GET":
        ProductToReturn = GetProduct(ProductId)

        return str(ProductToReturn)


@route('/customers/', methods=["GET", "POST"])
def customers(request):
    if request.method == b"POST":
        content = json.loads(request.content.read())
        CustomerItem = Customer(content["FirstName"], content["LastName"])
        Id = CustomerItem.DumpCustomer()
        return str({"status": "OK", "id": Id})

    if request.method == b"GET":
        return json.dumps({"customers": ReadCustomers()["customers"]})


@route('/customer/<int:CustomerId>', methods=["GET"])
def customer(request, CustomerId):
    if request.method == b"GET":
        CustomerToReturn = GetCustomer(CustomerId)

        return str(CustomerToReturn)


run(config.HOST, config.PORT, displayTracebacks=False)
