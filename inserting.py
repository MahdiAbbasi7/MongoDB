import os
import datetime

from dotenv import load_dotenv
from pymongo import MongoClient


# load config from .env
load_dotenv()
MONGODB_URL = os.environ['MONGODB_URL']

# connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URL)

# Get reference to 'bank' database
db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts

new_account = {
    'name':'Mahdi',
    'family':'Abbasi',
    'accounts_type':'checking',
    'balance': 1234567,
    'last_update': datetime.datetime.utcnow(),
}

# For inserting many accounts,
many_new_accounts = [
    {
        'name':'Sara',
        'family':'Ahmadi',
        'accounts_type':'Development',
        'balance': 7654321,
        'last_update': datetime.datetime.utcnow(),
    },

    {
        'name':'John',
        'family':'Alexander',
        'accounts_type':'Tester',
        'balance': 7864738,
        'last_update': datetime.datetime.utcnow(),
    }
]


# Write an extension for insert the 'new account' into the 'accounts' collection.
# res = accounts_collection.insert_one(new_account)
# document_id = res.inserted_id

# For inserting many accounts
ress = accounts_collection.insert_many(many_new_accounts)
document_ids  = ress.inserted_ids


# print(f'INSERT DATA IS SUCCESFULLY AND _id : {document_id}')

print('# of documents inserted :' + str(len(document_ids)))
print(f'INSERT DATAS IS SUCCESFULLY AND _id : {document_ids}')


client.close()

