import json
import bcrypt

from exceptions.exceptions import UserNotFoundException

import requests

from config.config import SALT, USERNAME, PASSWORD

from config.config import SERVERS

def ReadUsers() -> dict:
    with open("users.json", "r") as f:
        data = json.load(f)

    return data["users"]

def CheckFromServer(servers, username, password, is_right=False):
    user = None
    for server in servers:
        data = requests.post(f"{server}/login/", headers={"user": username, "password": password})
        
        if data.status_code == 200:
            
            user = data.text
            
            user = json.loads(user)
            
            return True, user
    return False, user
        

def GetUser(Username, Password) -> dict:
    Users = ReadUsers()

    for User in Users:
        if User["username"] == Username:
            return User
    
    user = CheckFromServer(SERVERS, Username, Password)
    if not user[0] == True:
        raise UserNotFoundException(Username)
    
    return user[1]


def HashPassword(Password):
    # Declaring our password
    Password = str.encode(Password)

    # Adding the salt to password
    Salt = SALT

    # Hashing the password
    Hashed = bcrypt.hashpw(Password, Salt)

    # return the hashed
    return Hashed


def IsPasswordRight(Username, Password):
    try:
        User = GetUser(Username, Password)

        if User.get("password") == Password:
            return True, User

        else:
            return False, None

    except UserNotFoundException:
        data = CheckFromServer(SERVERS, Username, Password, is_right=True)
        if data[0] == True:
            return True, data[1]
        else:
            return False, None


def DumpUsers(Users):
    data = {"users": Users}
    with open("users.json", "w") as f:
        json.dump(data, f)


def DumpUser(User):
    Users = ReadUsers()
    User["Id"] = len(Users) + 1
    Users.append(User)
    DumpUsers(Users)

    Id = User["Id"]

    return Id


def CreateUser(Username, Password, Firstname, Lastname, Creator, IsAdmin):
    User = {"username": Username, "password": HashPassword(
        Password), "firstname": Firstname, "lastname": Lastname, "creator": Creator, "is_admin": IsAdmin}

    DumpUser(User)


def CheckLogin(request):
    user = request.getHeader('user')
    token = request.getHeader('password')

    if IsPasswordRight(user, token)[0] == True:
        return True

    else:
        return False
