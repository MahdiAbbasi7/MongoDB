import os
import pprint

from pymongo import MongoClient
from dotenv import load_dotenv

# Import ObjectId from bson package (part of pymongo distribution) to enable querying by objects.
from bson.objectid import ObjectId

# Load configs
load_dotenv()
MONGODB_URL  = os.environ['MONGODB_URL']

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URL)

# Get reference to 'bank' database
db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts

# Query by ObjectId
# document_to_find = {'_id': ObjectId('6527939a93eab479d731f8a0')}

# Query for many objects
documents_to_finds = {'balance':{'$gt':1234568}}

# Write an experssion that retrieves documents matching the query constraints in the 'accounts' collection.
# res = accounts_collection.find_one(document_to_find)
cursor = accounts_collection.find(documents_to_finds)
# pprint.pprint(res)

num_docs = 0
for doc in cursor:
    num_docs += 1
    pprint.pprint(doc)
    print()
print("# of documents found : " + str(num_docs))


client.close()