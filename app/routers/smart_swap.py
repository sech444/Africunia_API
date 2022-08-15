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
import asyncio
from tronpy import AsyncTron
from tronpy.exceptions import (
   
    AddressNotFound,

)


# connect to the Tron blockchain
client_trx = Tron(network='nile') #network='nile'

# connect to the XRP blockchain
# Define the network client
JSON_RPC_URL = "https://xrplcluster.com"
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
            destination=account_to, 
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
    if len(adr_verify) == 34:
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
        
        
@router.post('/api/v1/api/xrp_webhook', tags=["WebHook"])
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
                                detail=f"Not a valid xrp hash check the hash ")
        



# integers representing half & one Tron
HALF_TRON = 500000
ONE_TRON = 1000000

# your wallet information
'''#WALLET_ADDRESS = "your wallet here"
PRIVATE_KEY = "your Private Key 


recipient_address = 'TYotKQtGriZGnGw5UUWThj63dqFAtXSTnS'#'TPhBQKbg3WqZnxCeiDw9ZtsaYutkvHqeWS'
amount = 1000000
print(amount)'''
# send some 'amount' of Tron to the 'wallet' address
@router.post("/api/v1/tron_transaction", tags=["Transaction"])
async def send_tron(sender_address =  Form(...), recipient_address = Form(...), account_to_send = Form(...),PRIVATE_KEY = Form(...)):
    client = Tron(network='nile')
    WALLET_ADDRESS = sender_address
    if client.is_address(sender_address) != True:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Invaild wallet")
            
    balance = client.get_account_balance(str(sender_address))
    if balance >= int(account_to_send):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"bals not up to the aomunt you went to send")
    
    try:
        priv_key = PrivateKey(bytes.fromhex(PRIVATE_KEY))
        
        # create transaction and broadcast it
        print("building txn")
        txn = (client.transfer(str(WALLET_ADDRESS), str(recipient_address), int(account_to_send))
            .memo("test memo")#"Transaction Description") # (
            .build()
            .inspect()
            .sign(priv_key)
            .broadcast()
            )
        # wait until the transaction is sent through and then return the details 
        print("waiting for transaction is sent through and then return the details ")
        print(txn)
        details=txn.wait()
        print(details["transaction"]["transaction"]["txID"])

        return {"transaction hash" : details}
 
    
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid xrp hash check the hash and try again")
    

@router.post("/api/v1/get_tron_bals", tags=["Transaction"])
def account_balance(user_adr: str = Form(...)):
    try:
        if client_trx.is_address(user_adr) != True:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Invaild wallet")
    #'TBVmp6ciyuNjV6JFTN4jMXsDms2oo12aPV' #'TSmaksTnwCcKkXDchTknJJb6X39odHsoBK'
        balance = client_trx.get_account_balance(str(user_adr))
        return {'balance' : balance}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"(AddressNotFound): account not found on-chain ")



#transaction_hash  = '76375d0b706ad5271e86ae49499e534cb1e0e7ae2cd1088b149ad35ebd2ee9e7'
@router.post('/api/v1/api/tron_webhook', tags=["WebHook"])
def transation_detail(transaction_hash:str = Form(...),webhook_url:str = Form(...)) -> dict():
    client = Tron(network='nile')
    try:
        info = client.get_transaction(str(transaction_hash))
        tx_xrp = json.dumps(info, default=vars)
        data2 = {
            'account_details': 'transaction',
                'details':  tx_xrp,
                }
        r=requests.post(webhook_url, data=json.dumps(data2))
        return {"data" : tx_xrp}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid xrp hash check the hash and try again")
    
#print("transation_detail....................")


@router.post("/api/v1/wallet_on_tron_network",tags=["Coin_Wallets"])
def create_wallet_on_tron_network(): 
    wallet = client_trx.generate_address()
    #print("Wallet address:  %s" % wallet['base58check_address'])
    #print("Private Key:  %s" % wallet['private_key'])
    
    return {"Wallet address": wallet['base58check_address'],
            "Private Key": wallet['private_key']}
    

# wallet xrp_network
@router.post("/api/v1/wallet_on_xrp_network",tags=["Coin_Wallets"])
def create_wallet_on_xrp_network(): 
    my_wallet = Wallet.create()
    #print(my_wallet.classic_address) # Example: rGCkuB7PBr5tNy68tPEABEtcdno4hE6Y7f
    #print(my_wallet.seed)  
    
    return {"classic_address":my_wallet.classic_address,
            "seed": my_wallet.seed}
    
