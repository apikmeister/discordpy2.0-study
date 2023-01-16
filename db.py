from bson.objectid import ObjectId
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import bcrypt

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

# access the database
# db = client["mydb"]
users_collection = client.usersinfo.users

def getUser(username):
    user = users_collection.find_one({"username": username})
    if user is None:
        return False
    user["password"] = user["password"].decode('utf-8')
    return user

def checkUser(username):
    if getUser(username):
        return True
    else:
        return False
    
def addUser(username, password):
    if not checkUser(username):
        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = { 
                "username": username,
                "password": password
        }
        users_collection.insert_one(user)
        return True
    
def updatePass(username, password):
    if checkUser(username):
        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        users_collection.update_one(
            {'username': username},
            {"$set":{'password': password}})
        return True
    
def deleteUser(username):
    if checkUser(username):
        users_collection.delete_one({"username": username})
        return True

# references
# def addUserDb(username,passwor):
#     if not checkUser(username):
#         collection = db[region]
#         password=encryptPass(password)
#         user={
#             "username":username,
#             "password":password
#             }
#         collection.insert_one(user)
#         return True

# def encryptPass(password):
#     password=Fernet(KEY).encrypt(password.encode('utf-8'))
#     return password

# def checkUser(username,region):
#     if getUser(username,region):
#         return True
#     else:
#         return False

# def updatePass(username,password,region):
#     if checkUser(username,region):
#         password=encryptPass(password)
#         collection=db[region]
#         collection.update_one(
#             {'username':username},
#             {"$set":{'password':password}})
#         return True

# def getUser(username,region):
#     collection=db[region]
#     user = collection.find_one({"username": username})
#     if user==None:
#         return False
#     user["password"]=(Fernet(KEY).decrypt(user["password"])).decode('utf-8')
#     return user

# def delUser(username,region):
#     try:
#         collection = db[region]
#         collection.delete_one({"username":username})
#         collection = db['reminders']
#         collection.delete_many({"username":username,"region":region})
#         return True
#     except:
#         return False
