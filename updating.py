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

# Filter 
# document_to_update = {'_id': ObjectId('6527939a93eab479d731f8a1')}
# Many filter
documents_to_update = {'account_type': 'savings'}

# Update 
# add_to_balance = {'$inc':{'balance':100}}
# Updates
"""If fields are not existing , mongo add this field to the database automatically."""
set_fields = {'$set':{'minimum_balance':100}}


# Print orginal documents
# pprint.pprint(accounts_collection.find_one(document_to_update))


# res = accounts_collection.update_one(document_to_update, add_to_balance)
res = accounts_collection.update_one(documents_to_update, set_fields)

print('Document updated :' + str(res.modified_count))

pprint.pprint(accounts_collection.find_one(documents_to_update))

client.close()