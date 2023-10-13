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

# Filter by object
# documents_to_delete = {'_id': ObjectId('6527939a93eab479d731f8a1')}
# Filter for accounts with balances less than $2000
documents_to_delete = {'balance': {'$lt':2000}}

# Search for document before delete
print('Searching for target document before delete........ ')
pprint.pprint(accounts_collection.find_one(documents_to_delete))

# Write an experssion that deletes the target account.
# res = accounts_collection.delete_one(documents_to_delete)
# Delete for deleted many fields.
res = accounts_collection.delete_many(documents_to_delete)


print('Searching for target document after delete : ')
pprint.pprint(accounts_collection.find_one(documents_to_delete))

print('Documents deleted: ' + str(res.deleted_count))
client.close()