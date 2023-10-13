import os
import pprint

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

# Calculate the average balance of checking and saving accounts with balances of less than $1000.

# Select accounts with balances of less than $1000.
select_by_balance = {'$match': {'balance':{'$lt':1000}}}

# Seperate documents by accounts type and calculate the average balance for each account type.
seperate_by_accounts_calculate_avg_balance = {
    '$group':{'_id':'$account_type', 'avg_balance':{'$avg':'$balance'}}
}

# Create an aggregation pipline using 'stage_match_balance' and 'storage_group_account_type'.
pipline = [
    select_by_balance,
    seperate_by_accounts_calculate_avg_balance,
]

# Perform an aggregation on 'pipeline'.
result = accounts_collection.aggregate(pipline)

print()
print(' Aggregiate balance of checking and saving accounts with balances of less than $1000 : ', '\n')

for item in result:
    pprint.pprint(item)

client.close()