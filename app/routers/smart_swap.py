from time import sleep
import datetime
from wsgiref.validate import validator
from fastapi import FastAPI, WebSocket, BackgroundTasks, APIRouter, Depends, status, HTTPException, Form
import json
import xrpl
import requests
import pandas as pd
from app.schemas import BNB_network, USDT_network, Ripple_network
from typing import Optional
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
from json import JSONEncoder
import asyncio
from aiohttp import ClientResponse
from tronpy import AsyncTron
from fastapi import FastAPI, WebSocket, BackgroundTasks, APIRouter, Depends, status, HTTPException, Form, Response
import json
from web3 import Web3
from dotenv import load_dotenv
from cryptography.fernet import Fernet
import os
import jwt
from app.utils import VerifyToken
from fastapi.security import HTTPBearer
import random


token_auth_scheme = HTTPBearer()
from tronpy.exceptions import (
   
    AddressNotFound,

)
w3 = Web3(Web3.HTTPProvider('https://rpc.exlscan.com/'))


router = APIRouter()

contract_addr ='0x561748A6B1D8b328788dc49C03e0605cc2030953'
dbAddress = w3.toChecksumAddress(contract_addr).lower()
#print(dbAddress )

load_dotenv()
#w3 = os.getenv("w3")


address_key = os.getenv("address_key")




with open("pancake.json", "r") as file:
    Compiled_code = file.read()
    #print(Compiled_code)

#afcash ='0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b'
#contract_addr
Afcash=w3.eth.contract(address=contract_addr, abi=Compiled_code)

#print(Afcash.functions.name().call())

# connect to the Tron blockchain
client_trx = Tron()  #network='nile'

with open("./networks_id.json",'r') as net_file:
    data_n = net_file.read()
    #print(net_file.read())
    
#df1 = pd.DataFrame(data_n).astype(str) 
Df1=pd.read_json(data_n)

#"sssU6icMrRgxgcv5hhgd4xXCBUK7X"
@router.post("/api/v1/xrp_transaction", tags=["Transaction"])
def xrp_transaction(Network: Ripple_network,response: Response, token: str = Depends(token_auth_scheme),private_key= Form(...), account_to = Form(...),value_to_send = Form(...),destination_tag:Optional[int] = Form(None, description="Please comfirm if the recciving address reuires a MEMO/Tag.")):
    """A valid access token is required to access this route"""

    # result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # # 👇 new code
    # if result.get("status"):
    #     response.status_code = status.HTTP_400_BAD_REQUEST
    #     return result
    # # 👆 new code
    TokenA = Network.value
    #print(len(TokenA))
    if len(TokenA) == 25 :
        bsc = Df1['BNB']['Binance Smart Chain']
        #xrp_tx()
        # print(bsc)
        # return bsc
    elif len(TokenA) == 10 :
        bsc = Df1['XRP']['XRP client']
        #result = ast.literal_eval(bsc)
        #print(bsc)
        # return bsc
    elif len(TokenA) == 16 :
        bsc = Df1['ETH']['Ethereum Mainnet']
        #result = ast.literal_eval(bsc)
        # print(bsc)
        # return bsc
    elif len(TokenA) == 21 :
        bsc = Df1['polygon']['Polygon Mainnet Matic']
        # #result = ast.literal_eval(bsc)
        # print(bsc)
        # return bsc
    else :
        len(TokenA) == 25 
        bsc = Df1['BNB']['Binance Smart Chain']
        # result = ast.literal_eval(bsc)
        # print(result)
        # return bsc
    client = eval(bsc)
   #print(bsc_w3)
    
    # #print(bsc_w3.isConnected())
    # account_1 = private_key
    # account_2 = account_to
    # value = value_to_send
    # #print("sending567 ...................................................01")
    
    if len(private_key) == 44:
        fernet_obj = Fernet(private_key)

        encrypted_message = b'gAAAAABjPDT8CmjRPxPKJgyN7_PMPm5SutGf80MOiGcnyU8QZ4NbPUzbSgrrzipbSr2hbPbS_yZKGj2TDhGjQkikJcFGTF1E2naU5E5OVNoHJsECmnp47Hk='
        decrypted_message = fernet_obj.decrypt(encrypted_message).decode("utf-8")
        #decrypted_message = bytes(decrypted_mess, 'utf-8')
        key = decrypted_message
    else:
        key = private_key
    #if len(decrypted_message) == 66:
    priv_key = key
    #print('getting wallet')
    xrp_wallet = Wallet(seed=priv_key, sequence=16237283)
    p_wallet = str(xrp_wallet)
    #print(p_wallet)
    wallet_2 = json.dumps(xrp_wallet, default=vars)
    #get the classic_address to check balance 
    s=str(wallet_2)
    D2=ast.literal_eval(s)
    #print(D2)
    acct_info = AccountInfo(account=D2["classic_address"],ledger_index="validated",strict=True,)
    #print(acct_info)
    response2 = client.request(acct_info)
    result = response2.result["account_data"]
    bals = result['Balance']
    #print(bals) # "rMCcNuTcajgw7YTgBy1sys3b89QqjUrMpH"
    try:
        current_validated_ledger = get_latest_validated_ledger_sequence(client)
        xrp_wallet.sequence = get_next_valid_seq_number(xrp_wallet.classic_address, client)
        if value_to_send > bals:
            return{"data": "Invalid details" }
        #print('prepare the transaction')
        # the amount is expressed in drops, not 
        # see https://xrpl.org/basic-data-types.html#specifying-currency-amounts
        my_tx_payment = Payment(
            account=xrp_wallet.classic_address,
            amount=value_to_send,
            destination=account_to, 
            destination_tag=destination_tag,
            last_ledger_sequence=current_validated_ledger + 20,
            sequence=xrp_wallet.sequence,
            fee="10",
        )
        # sign the transaction
        my_tx_payment_signed = safe_sign_transaction(my_tx_payment,xrp_wallet)
        #print("my_tx_payment_signed")
        # submit the transaction
        tx_response = send_reliable_submission(my_tx_payment_signed, client)
        #print('submited the transaction')
        #print(json.dumps(tx_response.result, indent=4, sort_keys=True))
        
        metadata = tx_response.result.get("meta", {})
        if metadata.get("TransactionResult"):
            #print("Result code:", metadata["TransactionResult"])
            return {"transaction": tx_response.result}
    except  xrpl.constants.XRPLException as e:
        #print(e)
        data = str(e)
        #print(data)
        #print(json.dumps(data, default=vars))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=data)
      

@router.post("/api/v1/get_xrp_bals", tags=["Transaction"])
def Get_xrp_bals(response: Response, token: str = Depends(token_auth_scheme),user_adr: str = Form(...)):
    """A valid access token is required to access this route"""

    # result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # # 👇 new code
    # if result.get("status"):
    #     response.status_code = status.HTTP_400_BAD_REQUEST
    #     return result
    # # 👆 new code
    JSON_RPC_URL = "https://xrplcluster.com"
    client = JsonRpcClient(JSON_RPC_URL)
    adr_verify = user_adr
    
    try:
        test_account = adr_verify #  "r9D7zkVzi1ja1yqwvB1iLFZsxioWP2oVtK"

        acct_info = AccountInfo(
            account=test_account,
            ledger_index="validated",
            strict=True,
        )
        response2 = client.request(acct_info)
        result = response2.result["account_data"]
        #print(result['Balance'])
        #print("response.status: ", response2.status)
        #print('Look up info about your account ')

        #print(json.dumps(response2.result, indent=4, sort_keys=True))
        return{"balances": float(result['Balance'])/10 **6}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid xrp wallet check the wallet and try again")
        
        
@router.post('/api/v1/api/xrp_webhook', tags=["WebHook"])
def transaction_receipt(tx_hash:str = Form(...),webhook_url:str = Form(...)) -> dict():
    JSON_RPC_URL = "https://xrplcluster.com"
    client = JsonRpcClient(JSON_RPC_URL)
    try:#print(json.dumps(tx_hash.result, indent=4, sort_keys=True))
        data = xrpl.transaction.get_transaction_from_hash(tx_hash = tx_hash, client = client)
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
PRIVATE_KEY = "your Private Key "

amount = 1000000
print(amount)'''
# send some 'amount' of Tron to the 'wallet' address
@router.post("/api/v1/tron_transaction", tags=["Transaction"])
async def send_tron(Network: USDT_network, response: Response, token: str = Depends(token_auth_scheme),sender_address =  Form(...), recipient_address = Form(...), account_to_send = Form(...),private_key = Form(...)):
    """A valid access token is required to access this route"""

    TokenA = Network.value
    print(len(TokenA))
    if len(TokenA) == 25 :
        bsc = Df1['BNB']['Binance Smart Chain']
        #xrp_tx()
        # print(bsc)
        # return bsc
    elif len(TokenA) == 10 :
        bsc = Df1['XRP']['XRP client']
        #result = ast.literal_eval(bsc)
        #print(bsc)
        # return bsc
    elif len(TokenA) == 16 :
        bsc = Df1['ETH']['Ethereum Mainnet']
        #result = ast.literal_eval(bsc)
        # print(bsc)
        # return bsc
    elif len(TokenA) == 21 :
        bsc = Df1['polygon']['Polygon Mainnet Matic']
        # #result = ast.literal_eval(bsc)
        # print(bsc)
        # return bsc
    else :
        len(TokenA) == 25 
        bsc = Df1['BNB']['Binance Smart Chain']
        # result = ast.literal_eval(bsc)
        # print(result)
        # return bsc
    client = eval(bsc)
   #print(bsc_w3)
    
    # #print(bsc_w3.isConnected())
    # account_1 = private_key
    # account_2 = account_to
    # value = value_to_send
    # #print("sending567 ...................................................01")
    
    if len(private_key) == 44:
        fernet_obj = Fernet(private_key)

        encrypted_message = b'gAAAAABjSOx-vUeOVYauXwja28UPOSHegavGNeyAK5jQtO6pAlUKmaTxGegOxTOyvfWWb06XQcoo5b76qLAldh9jGsI8RUy6bij-_YCLElzTNaqy0NFnXPgAgyULjouP-fLRd1xz5YiOBFyXbeCYyH_VCoGfBk9rHVakZQFmKeF-6WFx5BqWhpE='
        decrypted_message = fernet_obj.decrypt(encrypted_message).decode("utf-8")
        #decrypted_message = bytes(decrypted_mess, 'utf-8')
        key = decrypted_message
    else:
        key = private_key
    #if len(decrypted_message) == 66:
    priv_key = key
    
    client = Tron()
    WALLET_ADDRESS = sender_address
    if client.is_address(sender_address) != True:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Invaild wallet")
            
    balance = client.get_account_balance(str(sender_address))
    if balance >= int(account_to_send):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"bals not up to the aomunt you went to send")
    
    try:
        priv_key = PrivateKey(bytes.fromhex(priv_key))
        
        # create transaction and broadcast it
        #print("building txn")
        txn = (client.transfer(str(WALLET_ADDRESS), str(recipient_address), int(account_to_send))
            .memo("test memo")#"Transaction Description") # (
            .build()
            .inspect()
            .sign(priv_key)
            .broadcast()
            )
        # wait until the transaction is sent through and then return the details 
        #print("waiting for transaction is sent through and then return the details ")
        #print(txn)
        details=txn.wait()
        #print(details["transaction"]["transaction"]["txID"])

        return {"transaction hash" : details}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid xrp hash check the hash and try again")
    

@router.post("/api/v1/tron_usdt_tr20_transaction", tags=["Transaction"])
async def usdt_tr20(Network: USDT_network, response: Response, token: str = Depends(token_auth_scheme),sender_address =  Form(...), recipient_address = Form(...), account_to_send = Form(...),PRIVATE_KEY = Form(...)):
    """A valid access token is required to access this route"""

    
    TokenA = Network.value
    print(len(TokenA))
    if len(TokenA) == 25 :
        bsc = Df1['BNB']['Binance Smart Chain']
        #xrp_tx()
        # print(bsc)
        # return bsc
    elif len(TokenA) == 10 :
        bsc = Df1['XRP']['XRP client']
        #result = ast.literal_eval(bsc)
        #print(bsc)
        # return bsc
    elif len(TokenA) == 16 :
        bsc = Df1['ETH']['Ethereum Mainnet']
        #result = ast.literal_eval(bsc)
        # print(bsc)
        # return bsc
    elif len(TokenA) == 21 :
        bsc = Df1['polygon']['Polygon Mainnet Matic']
        # #result = ast.literal_eval(bsc)
        # print(bsc)
        # return bsc
    else :
        len(TokenA) == 25 
        bsc = Df1['BNB']['Binance Smart Chain']
        # result = ast.literal_eval(bsc)
        # print(result)
        # return bsc
    client = eval(bsc)
   #print(bsc_w3)
    
    client = Tron()
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
        #print("building txn")
        txn = (client.transfer(str(WALLET_ADDRESS), str(recipient_address), int(account_to_send))
            .memo("test memo")#"Transaction Description") # (
            .build()
            .inspect()
            .sign(priv_key)
            .broadcast()
            )
        # wait until the transaction is sent through and then return the details 
        #print("waiting for transaction is sent through and then return the details ")
        #print(txn)
        details=txn.wait()
        #print(details["transaction"]["transaction"]["txID"])

        return {"transaction hash" : details}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid xrp hash check the hash and try again")
    


@router.post("/api/v1/get_tron_bals", tags=["Transaction"])
def account_balance(response: Response, token: str = Depends(token_auth_scheme),user_adr: str = Form(...)):
    """A valid access token is required to access this route"""

    # result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # # 👇 new code
    # if result.get("status"):
    #     response.status_code = status.HTTP_400_BAD_REQUEST
    #     return result
    # # 👆 new code
    
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
    client = Tron()
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
    
    
@router.post("/api/v1/exl20_afcash_bals", tags=["Transaction"])
def afcash_bals(response: Response, token: str = Depends(token_auth_scheme),user_adr: str = Form(...)):
    """A valid access token is required to access this route"""

    #result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # 👇 new code
    #if result.get("status"):
        #response.status_code = status.HTTP_400_BAD_REQUEST
        #return result
    
    adr_verify = Web3.isAddress(user_adr.upper())
    if not adr_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild wallet")
    try:
        _trans =Afcash.functions.balanceOf(user_adr).call()
        _bal2_ = w3.fromWei(_trans, 'ether')
        return {"balance": _bal2_}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid exl20_afcash wallet check the wallet and try again")




@router.post("/api/v1/exl20_afcash_transaction", tags=["Transaction"])
def get_afcash_exl20(response: Response, token: str = Depends(token_auth_scheme),account_from: str = Form(...), account_to: str = Form(...), value_to_send: float = Form(...), Private_key: str = Form(...)):
    """A valid access token is required to access this route"""

    #result = VerifyToken(token.credentials).verify()  # 👈 updated code
    
    # 👇 new code
    #if result.get("status"):
        #response.status_code = status.HTTP_400_BAD_REQUEST
        #return result
    
    if len(Private_key) == 44:
        fernet_obj = Fernet(Private_key)

        encrypted_message = b'gAAAAABjPCtaMK7U68jNGPBNKJ8ml5VND9BH3lpofqBGHiwGQWvCE4YNLzG4Mwz2X_KXY_TXZyZ0xZ5T1jFxpsrfTNNH5zinfioYmg-9LVbVt4gmFecuMVtblUtsGsb_nxABE-6RIHP7OL-hbdW9lReGlcINnHls163U536OREM55MMUMMShlMw='
        decrypted_message = fernet_obj.decrypt(encrypted_message).decode("utf-8")
        #decrypted_message = bytes(decrypted_mess, 'utf-8')
        key = decrypted_message
    else:
        key = Private_key
    #if len(decrypted_message) == 66:
    priv_key = key
    
    account_1 = account_from
    account_2 = account_to
    value = value_to_send
    #print("sending234")
    adr_verify = w3.isAddress(account_from)
    if not adr_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild exl20_afcash wallet")

    if not Web3.isChecksumAddress(account_2):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid exl20_afcash wallet check the wallet and try again")
    #print("sending567")
    #value_2 = int(float(value))
    trans = Afcash.functions.balanceOf(account_1).call()
    _bal2_ = w3.fromWei(trans, 'ether')
    if float(value) > _bal2_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insufficient exl20_afcash Funds")
    #print("sending890")
    value_to = w3.toWei(value, 'ether')
    try:
        input_balance = Afcash.functions.transfer(account_2, value_to).buildTransaction(
            {
                'from': account_1,
                'nonce': w3.eth.get_transaction_count(account_1),
                'gas': 21000,
                'gasPrice': w3.toWei('15', 'gwei'),
            }
        ) 

        signed = w3.eth.account.sign_transaction(
            input_balance, private_key=priv_key)
        tx = w3.eth.send_raw_transaction(signed.rawTransaction)
        #print(tx)
        #print(f"Swap tx: {w3.toHex(tx)}")
        return {"hash_tx": w3.toHex(tx)}
    except ValueError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insufficient exl for gas fee")



"""@router.post("/api/v1/exl20_afcash_tarnfar", tags=["Transaction"])
def exl20_afcash_token(response: Response, token: str = Depends(token_auth_scheme), account_to: str = Form(...), value_to_send: float = Form(...), PRIVATE_KEY = Form(...)):
   

    #result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # 👇 new code
    #if result.get("status"):
        #response.status_code = status.HTTP_400_BAD_REQUEST
        #return result
    account_1 = address_key
    account_2 = account_to
    value = value_to_send
    #print("sending234")
    adr_verify = w3.isAddress(address_key)
    if not adr_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild exl20_afcash wallet")

    if not Web3.isChecksumAddress(account_2):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid exl20_afcash wallet check the wallet and try again")
    #print("sending567")
    #value_2 = int(float(value))
    trans = Afcash.functions.balanceOf(account_1).call()
    _bal2_ = w3.fromWei(trans, 'ether')
    if float(value) > _bal2_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insufficient exl20_afcash Funds")
    #print("sending890")
    value_to = w3.toWei(value, 'ether')
    try:
        input_balance = Afcash.functions.transfer(account_2, value_to).buildTransaction(
            {
                'from': account_1,
                'nonce': w3.eth.get_transaction_count(account_1),
                'gas': 250000,
                'gasPrice': w3.toWei('50', 'gwei'),
            }
        )

        signed = w3.eth.account.sign_transaction(
            input_balance, private_key=PRIVATE_KEY)
        tx = w3.eth.send_raw_transaction(signed.rawTransaction)
    
    
        receipt_ = w3.eth.get_transaction(tx)
        return {"New_transaction": w3.toJSON(receipt_ ) }
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Transaction error, most have exl20 for gas fee")
"""

@router.post("/api/v1/eth_fund_me", tags=["WebHook"])        
async def fund_me(response: Response, token: str = Depends(token_auth_scheme), account_from: str = Form(...), value_to_send: float = Form(...), PRIVATE_KEY = Form(...),webhook_url:Optional[str] = Form(None, description="returns the tx hash to the URL that you will provide (that is an HTTP request)")): 
    w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/2b4e6cbc9f444bed94a86178238f8cad'))
    with open("./fund_abi.json", 'r') as f_file:
        data_n = f_file.read()
        
    addr = account_from #w3.isChecksumAddress("0x4Ff26e42af59Bda47ac8D7BB15CEa3c6CaBafC7E")
    value = value_to_send #int(0.001)
    private_key=PRIVATE_KEY #""
    foun_me_address =w3.toChecksumAddress('0x0becF4dc23F996e969Dc07c201C5883Bd3513D2F') 
    abi = data_n
    # print(abi)
    Afcash = w3.eth.contract(address=foun_me_address, abi=abi)
    getusd = w3.toWei(value, 'ether')
    get_rate = Afcash.functions.getConversionRate(int(getusd)).call()
    #nonce = w3.eth.get_transaction_count(addr)
    print(get_rate)
    print("sending890")
    try:
        input_balance = Afcash.functions.deposit().buildTransaction(
                {
                'from': w3.toChecksumAddress(str(addr)),
                'value': w3.toWei(value, 'ether'),
                'nonce': w3.eth.get_transaction_count(addr),
                'gas': 250000,
                'gasPrice': w3.toWei('5', 'gwei'),
                }
            ) 

        signed = w3.eth.account.sign_transaction(input_balance, private_key=private_key)
        #print("signed transaction")
        tx = w3.eth.send_raw_transaction(signed.rawTransaction)
        #print(tx)
        tx_hash = w3.toHex(tx)
        receipt_ = w3.eth.get_transaction(tx_hash)
        await asyncio.sleep(10)
        data = {"amount in eth": value,
                "amount in usd":get_rate /10 **18,
            'tx_hash': w3.toHex(tx),
            'details': w3.toJSON(receipt_ ),
        }
        r=requests.post(webhook_url,data=json.dumps(data))

        return { "amount in eth": value,
                "amount in usd":get_rate /10 **18,
                "tx_hash":tx_hash,
                "data" : w3.toJSON(receipt_ )
                }
    except ValueError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"transaction fail chack your balance and try again") 


'''@router.websocket("/test")
async def test(websocket: WebSocket):
    print('Accepting client connection...')
    await websocket.accept()
    while True:
        try:
            # Wait for any message from the client
            await websocket.receive_text()
            # Send message to the client
            resp = {'value': random.uniform(0, 1)}
            await websocket.send_json(resp)
        except Exception as e:
            print('error:', e)
            break
    print('Bye..')
print(test("request"))
'''
'''
def __call__():
    xrp_contact_addr = '0x1D2F0da169ceB9fC7B3144628dB156f3F6c60dBE'
    if len(private_key) == 44:
        fernet_obj = Fernet(private_key)

        encrypted_message = b'gAAAAABjPDT8CmjRPxPKJgyN7_PMPm5SutGf80MOiGcnyU8QZ4NbPUzbSgrrzipbSr2hbPbS_yZKGj2TDhGjQkikJcFGTF1E2naU5E5OVNoHJsECmnp47Hk='
        decrypted_message = fernet_obj.decrypt(encrypted_message).decode("utf-8")
        #decrypted_message = bytes(decrypted_mess, 'utf-8')
        key = decrypted_message
    else:
        key = private_key
    #if len(decrypted_message) == 66:
    priv_key = key
    account_1 = account_from
    account_2 = account_to
    value = value_to_send

    usdt_bep=bsc_w3.eth.contract(address=busd_addr, abi=usdt_erc20)
    account_1 = account_from
    account_2 = account_to.upper()
    value = value_to_send
    #print("sending567 ...................................................")
    adr_verify = bsc_w3.isAddress(account_1)
    if not adr_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild busd_bep20_wallet")
    #print("sending567 isChecksumAddress")
    if not bsc_w3.isAddress(account_2):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid busd_bep20 wallet check the wallet and try again")
    #print("sending567")
    #value_2 = int(float(value))
    trans = usdt_bep.functions.balanceOf(bsc_w3.toChecksumAddress(account_1)).call()
    _bal2_ = bsc_w3.fromWei(trans, 'ether')
    #print(_bal2_)
    if float(value) > _bal2_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insufficient usdt_bep20 Funds")    
    #print("sending890 .....................................")
    nonce = bsc_w3.eth.get_transaction_count(account_1)
    value_to = bsc_w3.toWei(value, 'ether')
    try:
        input_balance = usdt_bep.functions.transfer(bsc_w3.toChecksumAddress(account_2), value_to).buildTransaction(
            {
                'from': bsc_w3.toChecksumAddress(account_1),
                'nonce': nonce,
                'gas': 250000,
                'gasPrice': w3.toWei('5.5', 'gwei'),
            }
        )

        signed = bsc_w3.eth.account.sign_transaction(
            input_balance, private_key=priv_key)
        tx = bsc_w3.eth.send_raw_transaction(signed.rawTransaction)
        
        return {"hash_tx": bsc_w3.toHex(tx)}
    except ValueError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Transaction error, most have BNB for gas fee")
'''

#foun_me_address = '0x49e8fd12fba447798ad5259c7bbabc0c8f9f9eec'