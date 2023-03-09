from klein import run, route
import json

from order.classes import Order
from order.functions import ReadOrders, GetOrder, SetOrder
from product.classes import Product
from product.functions import ReadProducts, GetProduct, SetProduct


@route('/order/', methods=["GET", "POST"])
def orders(request):
    if request.method == b"POST":
        content = json.loads(request.content.read())
        OrderItem = Order(content["order"], content["customer"])
        OrderId, Price = OrderItem.DumpOrder()
        return {"status": "OK", "id": OrderId, "price": Price}

    if request.method == b"GET":
        return ReadOrders()["orders"]


@route('/order/<string:OrderId>', methods=["GET", "POST"])
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

@route('/product/', methods=["GET", "POST"])
def products(request):
    if request.method == b"POST":
        content = json.loads(request.content.read())
        ProductItem = Product(content["Name"], content["Price"])
        ProductId = ProductItem.DumpProduct()
        return {"status": "OK", "id": ProductId}

    if request.method == b"GET":
        return ReadProducts()["products"]


@route('/product/<string:ProductId>', methods=["GET", "POST"])
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

run("localhost", 8080)
