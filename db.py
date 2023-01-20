from bson.objectid import ObjectId
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
import requests

load_dotenv()
KEY = (os.getenv('ENC_KEY')).encode('utf-8')
MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)

login_url = ('https://pelajar.mynemo.umt.edu.my/portal_login_ldap.php')


# access the database
# db = client["mydb"]
users_collection = client.usersinfo.users

def encryptpass(password):
    password=Fernet(KEY).encrypt(password.encode('utf-8'))
    return password

def getUser(discord_id):
    user = users_collection.find_one({"discord_id": discord_id})
    if user is None:
        return False
    user["password"] = (Fernet(KEY).decrypt(user["password"])).decode('utf-8')
    payload = {
        'login': 'student',
        'uid': user["username"],
        'pwd': user["password"] ,
        'submit': 'Log Masuk'
    }
    return payload

def getSession(payload):
    s = requests.Session()
    s.post(login_url, data=payload, verify=False, allow_redirects=True)
    return s

def getResponse(payload): 
    response = requests.Session().post(login_url, data=payload, verify=False, allow_redirects=True)
    return response

def checkUser(username):
    if getUser(username):
        return True
    else:
        return False
    
def addUser(discord_id ,username, password):
    if not checkUser(username):
        password = encryptpass(password)
        user = { 
                "discord_id": discord_id,
                "username": username,
                "password": password
        }
        users_collection.insert_one(user)
        return True
    
def updatePass(username, password):
    if checkUser(username):
        # password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        users_collection.update_one(
            {'username': username},
            {"$set":{'password': password}})
        return True
    
def deleteUser(username):
    if checkUser(username):
        users_collection.delete_one({"username": username})
        return True

