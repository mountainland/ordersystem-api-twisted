from klein import run, route
import json

from order.classes import Order
from order.functions import ReadOrders, GetOrder, SetOrder, GetOrders
from product.classes import Product
from product.functions import ReadProducts, GetProduct, SetProduct, GetProducts
from customer.classes import Customer
from customer.functions import ReadCustomers, GetCustomer, SetCustomer, GetCustomers

from login.functions import CreateUser, IsPasswordRight, CheckLogin, GetUser

from config import config

from db.db import get_id

def abort(request, code, response=""):
    request.setResponseCode(code)
    request.write(str(response).decode())
    request.finish()

def admin_required(request, response=""):
    user = GetUser(request.getHeader('user'), request.getHeader('password'))
    if not user["is_admin"] == True:
        if response == "":
            response = json.dumps({"error": "Admin level access required"})
        abort(request, 403, response=response)


def login_required(request, response=""):
    if not CheckLogin(request):
        if response == "":
            response = json.dumps({"error": "Login required"})
        abort(request, 401, response=response)


@route("/id/<string:collection>", methods=["GET", "POST"])
def idi(request, collection):
    respons = get_id(collection)
    
    return respons
        

@route('/orders/', methods=["GET", "POST"])
def orders(request):
    login_required(request)

    if request.method == b"POST":
        content = json.loads(request.content.read())
        OrderItem = Order(content["order"], content["customer"])
        OrderId, Price = OrderItem.DumpOrder()
        return str({"status": "OK", "id": OrderId, "price": Price})

    if request.method == b"GET":
        orders = GetOrders()
        return json.dumps({"orders": orders})


@route('/order/<int:OrderId>', methods=["GET", "POST"])
def order(request, OrderId):
    login_required(request)

    if request.method == b"POST":

        admin_required(request)
        content = json.loads(request.content.read())
        SetOrder(OrderId, content)
        return json.dumps({"status": "OK"})

    if request.method == b"GET":

        OrderToReturn = GetOrder(OrderId)

        return str(OrderToReturn)


@route('/products/', methods=["GET", "POST"])
def products(request):
    login_required(request)

    if request.method == b"POST":

        content = json.loads(request.content.read())
        ProductItem = Product(content["Name"], content["Price"])
        ProductId = ProductItem.DumpProduct()
        return json.dumps({"status": "OK", "id": ProductId})

    if request.method == b"GET":
        
        products_list = GetProducts()
        
        return json.dumps({"products": products_list})


@route('/product/<int:ProductId>', methods=["GET", "POST"])
def product(request, ProductId):
    login_required(request)

    if request.method == b"POST":
        content = json.loads(request.content.read())
        #if content["IsReady"] == True:
            #item = GetProduct(ProductId)

        SetProduct(ProductId, content)
        return json.dumps({"status": "OK"})

    if request.method == b"GET":

        ProductToReturn = GetProduct(ProductId)

        return json.dumps(ProductToReturn)


@route('/customers/', methods=["GET", "POST"])
def customers(request):
    login_required(request)

    if request.method == b"POST":

        content = json.loads(request.content.read())
        CustomerItem = Customer(
            content["FirstName"], content["LastName"], content["PhoneNumber"], content["Email"])
        Id = CustomerItem.DumpCustomer()
        return str({"status": "OK", "id": Id})

    if request.method == b"GET":
        return json.dumps({"customers": GetCustomers()})


@route('/customer/<int:CustomerId>', methods=["GET", "POST"])
def customer(request, CustomerId):
    login_required(request)

    if request.method == b"GET":
        CustomerToReturn = GetCustomer(CustomerId)

        return json.dumps(CustomerToReturn)

    if request.method == b"POST":
        content = json.loads(request.content.read())
        CustomerToReturn = GetCustomer(CustomerId)
        user = GetUser(request.getHeader('user'))
        if user["is_admin"] == True:
            SetCustomer(CustomerId, content, True)

        return json.dumps({"status": "Ok"})


@route('/users/', methods=["POST"])
def users(request):
    login_required(request)

    if request.method == b"POST":
        admin_required(request)

        data = json.loads(request.content.read())

        CreateUser(data["username"], data["password"], data["firstname"],
                   data["lastname"], request.getHeader('user'), data.get('is_admin', False))


@route("/login/", methods=["POST"])
def login(request):

    
    login_required(request, json.dumps(
        {"error": "Väärä salasana tai käyttäjänimi"}))

    username = request.getHeader('user')
    user = GetUser(username, request.getHeader('password'))
    return json.dumps({"is_admin": user.get("is_admin")})


run(config.HOST, config.PORT, displayTracebacks=False)
