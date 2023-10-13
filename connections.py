import os
from dotenv import load_dotenv
from pymongo import MongoClient


# load config from .env
load_dotenv()
MONGODB_URL = os.environ['MONGODB_URL']


client = MongoClient(MONGODB_URL)

for name in client.list_database_names():
    print(name)
    
client.close()