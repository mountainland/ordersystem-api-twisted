from klein import run, route
import json

from order.classes import Order
from order.functions import ReadOrders, GetOrder, SetOrder
from product.classes import Product
from product.functions import ReadProducts, GetProduct, SetProduct
from customer.classes import Customer
from customer.functions import ReadCustomers, GetCustomer, SetCustomer

from login.functions import CreateUser, IsPasswordRight, CheckLogin, GetUser

from config import config


def abort(request, code, response=""):
    request.setResponseCode(code)
    return ""


def admin_required(request, response=""):
    user = GetUser(request.getHeader('user'))
    if not user["is_admin"] == True:
        if response == "":
            response = json.dumps({"error": "Admin level access required"})
        abort(request, 403, response=response)

def login_required(request, response=""):
    if not CheckLogin(request):
        if response == "":
            response = json.dumps({"error": "Login required"})
        abort(request, 401, response=response)

@route('/orders/', methods=["GET", "POST"])
def orders(request):
    login_required(request)
    


    if request.method == b"POST":
        content = json.loads(request.content.read())
        OrderItem = Order(content["order"], content["customer"])
        OrderId, Price = OrderItem.DumpOrder()
        return str({"status": "OK", "id": OrderId, "price": Price})

    if request.method == b"GET":
        return json.dumps({"orders": ReadOrders()["orders"]})


@route('/order/<int:OrderId>', methods=["GET", "POST"])
def order(request, OrderId):
    login_required(request)
    


    if request.method == b"POST":

        admin_required(request)
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
    login_required(request)
    


    if request.method == b"POST":

        content = json.loads(request.content.read())
        ProductItem = Product(content["Name"], content["Price"])
        ProductId = ProductItem.DumpProduct()
        return json.dumps({"status": "OK", "id": ProductId})

    if request.method == b"GET":

        return json.dumps({"products": ReadProducts()["products"]})


@route('/product/<int:ProductId>', methods=["GET", "POST"])
def product(request, ProductId):
    login_required(request)
    


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
    login_required(request)
    


    if request.method == b"POST":

        content = json.loads(request.content.read())
        CustomerItem = Customer(content["FirstName"], content["LastName"])
        Id = CustomerItem.DumpCustomer()
        return str({"status": "OK", "id": Id})

    if request.method == b"GET":
        return json.dumps({"customers": ReadCustomers()["customers"]})


@route('/customer/<int:CustomerId>', methods=["GET", "POST"])
def customer(request, CustomerId):
    login_required(request)
    


    if request.method == b"GET":
        CustomerToReturn = GetCustomer(CustomerId)

        return json.dumps(CustomerToReturn)

    if request.method == b"POST":
        content = json.loads(request.content.read())
        CustomerToReturn = GetCustomer(CustomerId)
        for item in CustomerToReturn:
            if item in content:
                CustomerToReturn[item] = content[item]
        SetCustomer(CustomerId, CustomerToReturn)

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
    

    login_required(request, json.dumps({"error": "Väärä salasana tai käyttäjänimi"}))

    username = request.getHeader('user')
    user = GetUser(username)
    return json.dumps({"is_admin": user.get("is_admin")})

run(config.HOST, config.PORT, displayTracebacks=False)
