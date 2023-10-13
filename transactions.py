import os
from pymongo import MongoClient
from dotenv import load_dotenv


# Load configs
load_dotenv()
MONGODB_URL  = os.environ['MONGODB_URL']


# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URL)

'''Step 1: Define the callback that specifies the sequence of operations to perform inside the transactions.'''
def callback(
       session,
       transfer_id = None,
       account_id_receiver = None,
       account_id_sender = None,
       transfer_amount = None,
):
    # Get reference to 'accounts' collection
    accounts_collection = session.client.bank.accounts

    # Get reference to 'transfer' collection
    transfer_collection = session.client.bank.transfers

    transfer = {
        'transfer_id': transfer_id,
        'to_account': account_id_receiver,
        'to_account_sender': account_id_sender,
        'amount': {'$numberDecimal': transfer_amount},
    }

    # Transaction operations
    # Important: You must pass the session to each operation

    # Update sender account: subtract transfer amount from balance and add transfer ID 
    accounts_collection.update_one(
        {'account_id': account_id_sender},
        {
            '$inc': {'balance': -transfer_amount},
            '$push': {'transfers_complete': transfer_id}
        },
        session = session,
    )

    # Update receiver account: add transfer amount to balance and add transfer ID
    accounts_collection.update_one(
        {'account_id': account_id_sender},
        {
            '$inc': {'balance': transfer_amount},
            '$push' : {'transfers_complete': transfer_id}
        },
        session =session,
    )

    # Add new transfer to 'transfers' collection
    transfer_collection.insert_one(transfer, session=session)
    print('Transaction Successful.')

    return

def callback_wrapper(s):
    callback(
        s,
        transfer_id="TR218721873",
        account_id_receiver="MDB343652528",
        account_id_sender="MDB574189300",
        transfer_amount=120000,
    )

'''Step 2: Start a client session.'''
with client.start_session() as session:
    # Step 3: Use with_transaction to start a transaction, execute the callback, and commit (or cancel on error)
    session.with_transaction(callback_wrapper)

client.close()