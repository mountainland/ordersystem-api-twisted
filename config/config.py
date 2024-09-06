# Klein
HOST = "localhost"
PORT = 8080

# Hashing
SALT = b""  # Your salt for hashing

# Database url
IP = "127.0.0.1"
URL = f"mongodb://{IP}:27017/"


# OTHER SERVERS:
SERVERS = []

MAIN_ID_SERVER = ""

AM_I_ID_SERVER = False


if MAIN_ID_SERVER == "":

    AM_I_ID_SERVER = True

USERNAME = "admin"

# FOr getting userinfo from other servers
PASSWORD = "admin"
