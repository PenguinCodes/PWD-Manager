import pymongo
from pymongo import MongoClient
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

cluster = MongoClient("127.0.0.1:27017")
db = cluster["pwd"]
collection = db["pwd"]
password_provided = "Password"  # ADDMASTER PASSD HERE
password = password_provided.encode()
salt = b"_salt"
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))


def dc(message):
    f = Fernet(key)
    message = f.decrypt(message)
    return (message.decode())


def en(message):
    f = Fernet(key)
    message = message.encode()
    return f.encrypt(message)


# MONGODB
def addPW(title, email, password):
    email = en(email)  # encodingemail
    password = en(password)
    email = email.decode()
    password = password.decode()
    collection.insert_one({"title": title, "email": str(email), "password": str(password)})
    print("Added an entry")


def retrivePW(title):
    var = collection.find({"title": title})
    for i in var:
        print(dc(i["email"].encode()), dc(i["password"].encode()))


def deletePW(email):
    email = en(email)
    collection.delete_one({"email": email})
    print("Record Deleted")


def authentication(MasterPassword):
    MasterPassword = en(MasterPassword)
    return collection.find({"masterPwd": MasterPassword})


while (True):
    print(" 1 : To add\n", "2 : To Retrive\n", "3 : To Authenticate\n", "4 : To Delete")
    d = input()
    print(d)
    if d == "1":
        title, email, password = input("Title"), input("Email"), input("Password")
        addPW(title, email, password)
    elif d == "2":
        title = input("Enter Title")
        retrivePW(title)

    elif d == "3":
        c = input("Master PW")
        print(authentication(c))
    elif d == "4":
        c = input("Enter Email of the Record")
        deletePW(c)
    else:
        break
