import json
import bcrypt

from exceptions.exceptions import UserNotFoundException

from config.config import SALT

def ReadUsers() -> dict:
    with open("users.json", "r") as f:
        data = json.load(f)
        
    return data["users"]

def GetUser(Username) -> dict:
    Users = ReadUsers()
    
    for User in Users:
        if User["username"] == Username:
            return User
    
    raise UserNotFoundException(Username)

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
        User = GetUser(Username)

        if bcrypt.checkpw(str.encode(Password), User["password"]):
            return True
    
        elif bcrypt.checkpw(HashPassword(str.encode(Password)), User["password"]):
            return True
        
        else:
            return False
        
    except UserNotFoundException:
        return False

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

def CreateUser(Username, Password, Firstname, Lastname, Creator):
    User = {"username": Username, "password": HashPassword(Password), "firstname": Firstname, "lastname": Lastname, "creator": Creator}

    DumpUser(User)
    
    
def CheckLogin(request):
    user = request.getHeader('user')        
    token = request.getHeader('password')
    
    if IsPasswordRight(user, token):
        return True
    
    else:
        return False