from time import sleep
from fastapi import FastAPI, WebSocket, BackgroundTasks, APIRouter, Depends, status, HTTPException, Form
import json
import xrpl
import requests
from xrpl.models.transactions import Payment
from xrpl.transaction import safe_sign_transaction, send_reliable_submission
from xrpl.ledger import get_latest_validated_ledger_sequence
from xrpl.account import get_next_valid_seq_number
from xrpl.models.requests.account_info import AccountInfo
from xrpl.models.response import Response
from xrpl.wallet import Wallet
from xrpl.clients import JsonRpcClient
from tronpy import Tron
from tronpy.providers import HTTPProvider
from tronpy.keys import PrivateKey
from tronpy.exceptions import AddressNotFound
import ast
import pandas as pd


# Define the network client
JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"#"https://xrplcluster.com"
client = JsonRpcClient(JSON_RPC_URL)

router = APIRouter()


#"sssU6icMrRgxgcv5hhgd4xXCBUK7X"
@router.post("/api/v1/xrp_transaction", tags=["Transaction"])
def xrp_transaction(account_Secret = Form(...), account_to = Form(...),value_to_send = Form(...)):
    xrp_wallet = Wallet(seed=account_Secret, sequence=16237283)
   # p_wallet = str(xrp_wallet)
    wallet_2 = json.dumps(xrp_wallet, default=vars)
    #get the classic_address to check balance
    s=str(wallet_2)
    D2=ast.literal_eval(s)
    acct_info = AccountInfo(account=D2["classic_address"],ledger_index="validated",strict=True,)
    response2 = client.request(acct_info)
    result = response2.result["account_data"]
    bals = result['Balance']
    #print(xrp_wallet.classic_address) # "rMCcNuTcajgw7YTgBy1sys3b89QqjUrMpH"
    try:
        current_validated_ledger = get_latest_validated_ledger_sequence(client)
        xrp_wallet.sequence = get_next_valid_seq_number(xrp_wallet.classic_address, client)
        if account_to <= bals:
            return{"data": "Invalid details" }
        # prepare the transaction
        # the amount is expressed in drops, not 
        # see https://xrpl.org/basic-data-types.html#specifying-currency-amounts
        my_tx_payment = Payment(
            account=xrp_wallet.classic_address,
            amount=value_to_send,
            destination=account_to, #"r9D7zkVzi1ja1yqwvB1iLFZsxioWP2oVtK",
            last_ledger_sequence=current_validated_ledger + 20,
            sequence=xrp_wallet.sequence,
            fee="10",
        )
        # sign the transaction
        my_tx_payment_signed = safe_sign_transaction(my_tx_payment,xrp_wallet)
        #print(my_tx_payment_signed)
        # submit the transaction
  
        tx_response = send_reliable_submission(my_tx_payment_signed, client)
        #print(json.dumps(tx_response.result, indent=4, sort_keys=True))
        
        metadata = tx_response.result.get("meta", {})
        if metadata.get("TransactionResult"):
            #print("Result code:", metadata["TransactionResult"])
            return {"tarnsation": tx_response.result}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Invalid details; could not determine encoding algorithm")
      



@router.post("/api/v1/get_xrp_bals", tags=["Transaction"])
def Get_xrp_bals(user_adr: str = Form(...)):
    adr_verify = user_adr
    p = str(adr_verify)
    print(len(p))
    if adr_verify == 34:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild wallet")
    try:
        test_account = adr_verify #  "r9D7zkVzi1ja1yqwvB1iLFZsxioWP2oVtK"

        acct_info = AccountInfo(
            account=test_account,
            ledger_index="validated",
            strict=True,
        )
        response2 = client.request(acct_info)
        result = response2.result["account_data"]
        print(result['Balance'])
        print("response.status: ", response2.status)
        print('Look up info about your account ')

        print(json.dumps(response2.result, indent=4, sort_keys=True))
        return{"balances": result['Balance']}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid xrp wallet check the wallet and try again")
        
        
@router.post('/api/v1/api/webhook', tags=["WebHook"])
def transaction_receipt(tx_hash:str = Form(...),webhook_url:str = Form(...)) -> dict():
    try:#print(json.dumps(tx_hash.result, indent=4, sort_keys=True))
        data = xrpl.transaction.get_transaction_from_hash(tx_hash = tx_hash, client =client,)
        tx_xrp = json.dumps(data, default=vars)
        data2 = {
            'account_details': 'transaction',
            'details':  tx_xrp,
            }
        r=requests.post(webhook_url, data=json.dumps(data2))
        return {"data" : tx_xrp}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid xrp hash check the hash and try again")
 
'''
#print(tx_response)
print('Look up')

import json

#print(f"Explorer link: https://testnet.xrpl.org/transactions/{tx_id}")
metadata = tx_response.result.get("meta", {})
if metadata.get("TransactionResult"):
    print("Result code:", metadata["TransactionResult"])
#if metadata.get("delivered_amount"):
   # print("XRP delivered:", xrpl.utils.drops_to_xrp(
                #metadata["delivered_amount"]))
print('Look up')
# wallet
from xrpl.wallet import Wallet
my_wallet = Wallet.create()
print(my_wallet.classic_address) # Example: rGCkuB7PBr5tNy68tPEABEtcdno4hE6Y7f
print(my_wallet.seed)  


print('Look up info about your account ...............................up....')
#acc = account()
test_account = "r9D7zkVzi1ja1yqwvB1iLFZsxioWP2oVtK"
from xrpl.models.requests.account_info import AccountInfo
acct_info = AccountInfo(
    account=test_account,
    ledger_index="validated",
    strict=True,
)
response2 = client.request(acct_info)
result = response2.result
print("response.status: ", response2.status)
import json
print(json.dumps(response2.result, indent=4, sort_keys=True))
  '''

"""

# Use private network as HTTP API endpoint
client_trx = Tron() #network='nile'
account = 'TBVmp6ciyuNjV6JFTN4jMXsDms2oo12aPV' #'TSmaksTnwCcKkXDchTknJJb6X39odHsoBK'
def account_balance(account):
    balance = client_trx.get_account_balance(str(account))
    return balance

#print(account_balance(account))

#print('tron sending ......................')


# integers representing half & one Tron
HALF_TRON = 500000
ONE_TRON = 1000000

# your wallet information
WALLET_ADDRESS = "THE8qJCk51n59BeJMg6a5wgo2L7qcFTmqy"
PRIVATE_KEY = "c13217ddd884a4807c2300426496e0d8e03fdaf4fc82aebd07ce8d5f6a4e738b"

# connect to the Tron blockchain
'''Wallet address:  TYotKQtGriZGnGw5UUWThj63dqFAtXSTnS
Private Key:  6fcd2c7bc65a5d9980df6eedd6db65da01b431642ba200e2e5d38b39bc50bf7f'''

recipient_address = 'TYotKQtGriZGnGw5UUWThj63dqFAtXSTnS'#'TPhBQKbg3WqZnxCeiDw9ZtsaYutkvHqeWS'
amount = 1000000
print(amount)
# send some 'amount' of Tron to the 'wallet' address
def send_tron(recipient_address, amount):
    print('sending tron')
    try:
        priv_key = PrivateKey(bytes.fromhex(PRIVATE_KEY))
        
        # create transaction and broadcast it
        txn = (
            client_trx.trx.transfer(WALLET_ADDRESS, str(recipient_address), int(amount))
            .memo("test memo")#("Transaction Description")
            .build()
            .inspect()
            .sign(priv_key)
            .broadcast()
        )
        print('sent tron...................fuunnyf')
        # wait until the transaction is sent through and then return the details 
        #print(txn.wait()) 
        return txn.wait()

    # return the exception
    except Exception as ex:
        return ex
    
send_tron(recipient_address, amount)

#transaction_hash  = '76375d0b706ad5271e86ae49499e534cb1e0e7ae2cd1088b149ad35ebd2ee9e7'
def transation_detail(transaction_hash):
    info = client_trx.get_transaction_info(str(transaction_hash))
    return info
print("transation_detail....................")

print("wallet.....................")
def create_wallet(): 
    wallet = client_trx.generate_address()
    print("Wallet address:  %s" % wallet['base58check_address'])
    print("Private Key:  %s" % wallet['private_key'])
    
print("wallet.....................")
#create_wallet()
trx_hash = 'b277992ba1ef5d09331b6ef11ff85ba5184ffe66329612ffa02c43996bc65a01'
print(transation_detail(trx_hash))
client_tron = Tron()
address = 'TUw9W3BX4kt9dLMcBsNF2AusXFQMnX6wdw' #'TMoJMiQQgzneoGimdJjZtxcPiHJjamqRzK'
def account_balance(address):
    balance = client_tron.get_account_balance(str(address))
    return balance

print(account_balance(address))"""