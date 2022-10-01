from ast import Not, Return
from cgi import print_arguments
from cmath import e
from distutils.log import error
from fastapi import FastAPI, WebSocket, BackgroundTasks, APIRouter, Depends, status, HTTPException, Form,Response
import json
from binance.exceptions import BinanceAPIException
from decimal import Decimal as D, ROUND_DOWN, ROUND_UP
import decimal
from typing import List, Optional
import requests
from web3 import Web3, EthereumTesterProvider, HTTPProvider
from uuid import uuid4
from bitcoin import *
from binance.client import Client
from urllib.parse import urljoin, urlencode
from eth_account import Account
from cryptos import *
from dotenv import load_dotenv
import os
from binance.helpers import round_step_size
import asyncio
import decimal
from blockcypher import get_address_overview
from binance.enums import *
from pprint import pformat
from app.utils import VerifyToken
from fastapi.security import HTTPBearer
from cryptography.fernet import Fernet
import jwt
from app.utils import VerifyToken
# Scheme for the Authorization header
token_auth_scheme = HTTPBearer()



router = APIRouter()

w3 = Web3(Web3.HTTPProvider(
    'https://mainnet.infura.io/v3/bde4e3babba54474844b65de59d0a039'))

load_dotenv()
#w3 = os.getenv("w3")
API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
etherscan_API = os.getenv("etherscan_API")
address_key = os.getenv("address_key")
BASE_URL = 'https://api.binance.com'

headers = {
    'X-MBX-APIKEY': API_KEY
}


client = Client(API_KEY, SECRET_KEY)



@router.post("/api/v1/get_eth_bals", tags=["Transaction"])
def Get_eth_bals(response: Response, token: str = Depends(token_auth_scheme),user_adr: str = Form(...)):
    adr_verify = Web3.isAddress(user_adr.upper())
   
    try:
        if not adr_verify:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild wallet")
        _trans = w3.eth.get_balance(user_adr)
        _bal2_ = w3.fromWei(_trans, 'ether')
        return {"balance": _bal2_}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid eth wallet check the wallet and try again")


@router.post("/api/v1/eth_transaction", tags=["Transaction"])
async def eth_transaction(background_tasks: BackgroundTasks,response: Response, token: str = Depends(token_auth_scheme), account_from: str = Form(...), account_to: str = Form(...), value_to_send: float = Form(...), private_key: str = Form(...)):
    # checking the wallet if the are eth wallets
    adr_verify = w3.isAddress(account_from)
    if not adr_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"account_from Not a valid ETH wallet check the wallet and try again")
    account_2 = account_to
    if not Web3.isChecksumAddress(account_to):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"account_to Not a valid ETH wallet check the wallet and try again")

    value = value_to_send
    # check if not sending more the this bals
    value_2 = int(float(value_to_send))
    trans = w3.eth.get_balance(value_2)
    _bal2_ = w3.fromWei(trans, 'ether')
    if float(value) > _bal2_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insufficient ETH Funds")

    # getting the transaction count of the send (nonce)
    nonce = w3.eth.getTransactionCount(account_from)
    # building the transaction
    tx = {
        'nonce': nonce,
        'to': account_2,
        'value': w3.toWei(value, 'ether'),
        'gas': 200000,
        'gasPrice': w3.toWei('50', 'gwei'),
    }

    # sign the transaction and waiting for tx_hash

    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    new_data = (w3.toHex(tx_hash))
    return {"New_transaction": new_data, }


@router.post("/api/v1/create_order_buy", tags=["Transaction"])
def create_Order(response: Response, token: str = Depends(token_auth_scheme),symbol: str = Form(...), quantity: float = Form(...)):
    quantity = '{:.8f}'.format(float(quantity))

    try:
        order = client.order_market_buy(
            symbol=symbol.upper(),
            quantity=quantity)

        return{"data": json.dumps(order, indent=2)}
    except BinanceAPIException as e:
        #print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid transaction check the symbol eg. BNBUSDT then quantity >= 10.38USDT or Account has insufficient balance for requested action, symbol like this BTCUSDT")


@router.post("/api/v1/create_order_sell", tags=["Transaction"])
def create_Order(response: Response, token: str = Depends(token_auth_scheme),symbol: str = Form(...), quantity: float = Form(...)):
    quantity = '{:.8f}'.format(float(quantity))
    try:
        order = client.order_market_sell(
            symbol=symbol.upper(),
            quantity=quantity)

        asyncio.sleep(3)

        return{"data": json.dumps(order, indent=2)}
    except BinanceAPIException as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid transaction check the symbol eg. BNBUSDT then quantity >= 10.38USDT or Account has insufficient balance for requested action, symbol like this BTCUSDT")


@router.post("/api/v1/order_status", tags=["Transaction"])
def create_Order(response: Response, token: str = Depends(token_auth_scheme),symbol: str = Form(...), order_Id: int = Form(...)):
    try:
        order = client.get_order(
            symbol=symbol.upper(),
            orderId=order_Id)  # 4136872022)

        return{"data": order}
    except BinanceAPIException as e:
        print(e)
        print (e.status_code)
        print (e.message)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid transaction check the symbol eg. BNBUSDT then orderid eg. 4136872022 and try again")

def convert_scientific_to_decimal(num):
    if 'e' in str(num):
        return "{:.15f}".format(float(str(num)))
    else:
        return str(num)

@router.post("/api/v1/asset_balance", tags=["Transaction"])
def create_Order(response: Response, token: str = Depends(token_auth_scheme),asset_symbol: str = Form(...)):
    try:
        bals = client.get_asset_balance(asset=asset_symbol.upper())
        return{"data": bals}
    except BinanceAPIException as e:
        print(e)
        print (e.status_code)
        print (e.message)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid transaction check the asset symbol eg. BNB , USDT ")


@router.post("/api/v1/get_deposit_address", tags=["Transaction"])
def get_deposit_address(response: Response, token: str = Depends(token_auth_scheme),asset_symbol: str = Form(...)):
    try:
        bals = client.get_deposit_address(coin=asset_symbol.upper())
        return{"data": bals}
    except BinanceAPIException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid transaction check the asset symbol eg. BNB , USDT ")


# using web3py to Transfer usdt tether bep20 from one account to other  account with binance
contract_addr=w3.toChecksumAddress('0x55d398326f99059fF775485246999027B3197955')

with open("usdt_abi.json", "r") as file:
    usdt_erc20 = file.read()
    

@router.post("/api/v1/usdt_bep20_bals", tags=["Transaction"])
async def usdt_bals(response: Response, token: str = Depends(token_auth_scheme),wallet_id: str = Form(...)):
    """A valid access token is required to access this route"""

    #result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # 👇 new code
    #if result.get("status"):
        #response.status_code = status.HTTP_400_BAD_REQUEST
        #return result
    
    bsc = "https://bsc-dataseed.binance.org/"
    bsc_w3 = Web3(Web3.HTTPProvider(bsc))
        
    
    usdt_bep=bsc_w3.eth.contract(address=contract_addr, abi=usdt_erc20)
    adr_verify = Web3.isAddress(wallet_id.upper())
   
    if not adr_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild wallet")
    try:
        _trans = usdt_bep.functions.balanceOf(wallet_id).call()
        _bal2_ = w3.fromWei(_trans, 'ether')
        return {"balance": _bal2_}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid usdt_bep20 wallet check the wallet and try again")




# using web3py to Transfer usdt tether bep20 from one account to other  account with binance
    
@router.post("/api/v1/usdt_bep20_transaction", tags=["Transaction"])
def usdt_transaction(response: Response, token: str = Depends(token_auth_scheme),account_from: str = Form(...), account_to: str = Form(...), value_to_send: float = Form(...), Private_key: str = Form(...)):
    """A valid access token is required to access this route"""

    #result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # 👇 new code
    #if result.get("status"):
        #response.status_code = status.HTTP_400_BAD_REQUEST
        #return result
   
    if len(Private_key) == 44:
        fernet_obj = Fernet(Private_key)

        encrypted_message = b'gAAAAABjFWoA9dLKDJ-eJHzveb56ka-3X-vJynPR7l1jXPTsC-CKp0Pslpx-S0_qrtLFDUKmDt3Bsf3T-w_UMXXJUDAv6hA5ZOoEJ3kjDiryL05e3bDOAlpF_aMfzYk3jPyZU1ycaIlw2vs0JCuYkW_aBNi87U5HhWOuymXIRcr2NGiUHA9HDQw='
        decrypted_message = fernet_obj.decrypt(encrypted_message).decode("utf-8")
        #decrypted_message = bytes(decrypted_mess, 'utf-8')
        key = decrypted_message
    else:
        key = Private_key
    #if len(decrypted_message) == 66:
    priv_key = key
  
    bsc = "https://bsc-dataseed.binance.org/"
    bsc_w3 = Web3(Web3.HTTPProvider(bsc))
    
    usdt_bep=bsc_w3.eth.contract(address=contract_addr, abi=usdt_erc20)
    account_1 = account_from
    account_2 = account_to.upper()
    value = value_to_send
    #print("sending567 ...................................................")
    adr_verify = bsc_w3.isAddress(account_1)
    if not adr_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild usdt_bep20_wallet")
    #print("sending567 isChecksumAddress")
    if not bsc_w3.isAddress(account_2):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid usdt_bep20 wallet check the wallet and try again")
    #print("sending567")
    #value_2 = int(float(value))
    trans = usdt_bep.functions.balanceOf(account_1).call()
    _bal2_ = bsc_w3.fromWei(trans, 'ether')
    #print(_bal2_)
    if float(value) > _bal2_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insufficient usdt_bep20 Funds")
    
    #print("sending890 .....................................")
    value_to = bsc_w3.toWei(value, 'ether')
    try:
        input_balance = usdt_bep.functions.transfer(bsc_w3.toChecksumAddress(account_2), value_to).buildTransaction(
            {
                'from': account_1,
                'nonce': bsc_w3.eth.get_transaction_count(account_1),
                'gas': 250000,
                'gasPrice': bsc_w3.toWei('5.5', 'gwei'),
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


@router.post("/api/v1/usdt_erc20_bals", tags=["Transaction"])
def usdt_bals(response: Response, token: str = Depends(token_auth_scheme),wallet_id: str = Form(...)):
    """A valid access token is required to access this route"""

    result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # 👇 new code
    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    
    
    url = "https://api.etherscan.io/api"
    apikey = etherscan_API
    adr_verify = Web3.isAddress(wallet_id)
    try:
        if not adr_verify:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild wallet")
        _trans = w3.eth.get_balance(adr_verify)
        _bal2_ = w3.fromWei(_trans, 'ether')
        return {"balance": _bal2_}
    except :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid usdt_erc20 wallet check the wallet and try again")




@router.post("/api/v1/usdt_erc20_transaction", tags=["Transaction"])
def usdt_transaction(response: Response, token: str = Depends(token_auth_scheme),account_from: str = Form(...), account_to: str = Form(...), value_to_send: float = Form(...), private_key: str = Form(...)):
    """A valid access token is required to access this route"""

    result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # 👇 new code
    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    
    usdt_ = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
    account_1 = account_from
    account_2 = account_to
    value = value_to_send

    adr_verify = w3.isAddress(account_from)
    if not adr_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild wallet")

    if not Web3.isChecksumAddress(account_2):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid USDT wallet check the wallet and try again")

    value_2 = int(float(value))
    trans = w3.eth.get_balance(account_1)
    _bal2_ = w3.fromWei(trans, 'ether')
    if float(value) > _bal2_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insufficient USDT Funds")

    with open("usdt_abi.json", "r") as file:
        usdt_erc20 = file.read()

    USDT_ERC20 = w3.eth.contract(abi=usdt_erc20, address=usdt_)
    try:
        input_balance = USDT_ERC20.functions.transfer(account_2, value).buildTransaction({
            'from': adr_verify,
            'gas': 250000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'to': account_2,
            'value': w3.toWei(value, 'ether'),
            'nonce': w3.eth.get_transaction_count(adr_verify),
        })
        signed = w3.eth.account.sign_transaction(
            input_balance, private_key=private_key)
        tx = w3.eth.send_raw_transaction(signed.rawTransaction)
        #print(f"Swap tx: {web3.toHex(tx)}")
        return {"Swap tx": w3.toHex(tx)}
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Transaction error, most have BNB for gas fee")


@router.post("/api/v1/bnb", tags=["Transaction"])
def bnb_transaction(response: Response, token: str = Depends(token_auth_scheme),account_from: str = Form(...), account_to: str = Form(...), value_to_send: float = Form(...), Private_key: str = Form(...)):
    """A valid access token is required to access this route"""

    #result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # 👇 new code
    #if result.get("status"):
        #response.status_code = status.HTTP_400_BAD_REQUEST
        #return result
    
    if len(Private_key) == 44:
        fernet_obj = Fernet(Private_key)

        encrypted_message = b'gAAAAABjFWoA9dLKDJ-eJHzveb56ka-3X-vJynPR7l1jXPTsC-CKp0Pslpx-S0_qrtLFDUKmDt3Bsf3T-w_UMXXJUDAv6hA5ZOoEJ3kjDiryL05e3bDOAlpF_aMfzYk3jPyZU1ycaIlw2vs0JCuYkW_aBNi87U5HhWOuymXIRcr2NGiUHA9HDQw='
        decrypted_message = fernet_obj.decrypt(encrypted_message).decode("utf-8")
        #decrypted_message = bytes(decrypted_mess, 'utf-8')
        key = decrypted_message
    else:
        key = Private_key
    #if len(decrypted_message) == 66:
    priv_key = key
    
    bsc = "https://bsc-dataseed.binance.org/"
    bsc_w3 = Web3(Web3.HTTPProvider(bsc))
    account_1 = account_from
    account_2 = account_to
    value = value_to_send

    adr_verify = w3.isAddress(account_from)
    if not adr_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild wallet")

    if not Web3.isChecksumAddress(account_2):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid ETH wallet check the wallet and try again")

    value_2 = int(float(value))
    trans = bsc_w3.eth.get_balance(account_1)
    _bal2_ = bsc_w3.fromWei(trans, 'ether')
    if float(value) > _bal2_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insufficient ETH Funds")

    private_key = private_key
    addr = account_2

    nonce = bsc_w3.eth.getTransactionCount(account_1)

    tx = {
        'nonce': nonce,
        'to': account_2,
        'value': bsc_w3.toWei(value, 'ether'),
        'gas': 200000,
        'gasPrice': bsc_w3.toWei('5.5', 'gwei'),
    }

    signed_tx = bsc_w3.eth.account.signTransaction(tx, priv_key)
    tx_hash = bsc_w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    new_data = (bsc_w3.toHex(tx_hash))
    return {"New_transaction": new_data, }


@router.post("/api/v1/bnb_bals", tags=["Transaction"])
def bnb_bals(response: Response, token: str = Depends(token_auth_scheme),wallet_id: str = Form(...)):
    """A valid access token is required to access this route"""

    #result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # 👇 new code
    #if result.get("status"):
        #response.status_code = status.HTTP_400_BAD_REQUEST
        #return result
    
    bsc = "https://bsc-dataseed.binance.org/"
    bsc_w3 = Web3(Web3.HTTPProvider(bsc))
    adr_verify = Web3.isAddress(wallet_id)
    try:
        if not adr_verify:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Invaild wallet")
        _trans = bsc_w3.eth.get_balance(bsc_w3.toChecksumAddress(wallet_id))
        _bal2_ = bsc_w3.fromWei(_trans, 'ether')
        return {"balance": _bal2_}
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid BNB wallet check the wallet and try again")


@router.post("/api/v1/busd_transaction", tags=["Transaction"])
def busd_transaction(response: Response, token: str = Depends(token_auth_scheme),account_from: str = Form(...), account_to: str = Form(...), value_to_send: float = Form(...), Private_key: str = Form(...)):
    """A valid access token is required to access this route"""

    #result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # 👇 new code
    #if result.get("status"):
        #response.status_code = status.HTTP_400_BAD_REQUEST
        #return result
    
    if len(Private_key) == 44:
        fernet_obj = Fernet(Private_key)

        encrypted_message = b'gAAAAABjFWoA9dLKDJ-eJHzveb56ka-3X-vJynPR7l1jXPTsC-CKp0Pslpx-S0_qrtLFDUKmDt3Bsf3T-w_UMXXJUDAv6hA5ZOoEJ3kjDiryL05e3bDOAlpF_aMfzYk3jPyZU1ycaIlw2vs0JCuYkW_aBNi87U5HhWOuymXIRcr2NGiUHA9HDQw='
        decrypted_message = fernet_obj.decrypt(encrypted_message).decode("utf-8")
        #decrypted_message = bytes(decrypted_mess, 'utf-8')
        key = decrypted_message
    else:
        key = Private_key
    #if len(decrypted_message) == 66:
    priv_key = key
    
    bsc = "https://bsc-dataseed.binance.org/"
    bsc_w3 = Web3(Web3.HTTPProvider(bsc))
    busd_addr =bsc_w3.toChecksumAddress('0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56')
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
        
    print("sending890 .....................................")
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


@router.post("/api/v1/busd_bals", tags=["Transaction"])
def busd_bals(response: Response, token: str = Depends(token_auth_scheme),wallet_id: str = Form(...)):
    """A valid access token is required to access this route"""

    #result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # 👇 new code
    #if result.get("status"):
        #response.status_code = status.HTTP_400_BAD_REQUEST
        #return result
    
    
    bsc = "https://bsc-dataseed.binance.org/"
    bsc_w3 = Web3(Web3.HTTPProvider(bsc))
        
    busd_addr =bsc_w3.toChecksumAddress('0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56')

    usdt_bep=bsc_w3.eth.contract(address=busd_addr, abi=usdt_erc20)
    adr_verify = Web3.isAddress(wallet_id.upper())
   
    if not adr_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild wallet valid busd_bep20")
    try:
        _trans = usdt_bep.functions.balanceOf(bsc_w3.toChecksumAddress(wallet_id)).call()
        _bal2_ = w3.fromWei(_trans, 'ether')
        return {"balance": _bal2_}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid busd_bep20 wallet check the wallet and try again")

@router.post("/api/v1/exl_transaction", tags=["Transaction"])
def exl_transaction(response: Response, token: str = Depends(token_auth_scheme),account_from: str = Form(...), account_to: str = Form(...), value_to_send: float = Form(...), Private_key: str = Form(...)):
    """A valid access token is required to access this route"""

    #result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # 👇 new code
    #if result.get("status"):
        #response.status_code = status.HTTP_400_BAD_REQUEST
        #return result
    
    if len(Private_key) == 44:
        fernet_obj = Fernet(Private_key)

        encrypted_message = b'gAAAAABjFXUIZ5b4N8QzHdTqzi1DRSxPHIrNRW_sWtyFlFS4CzcQjUfp2dTYvci4j3Vv43YoO5p_bL9dcK9afMk8dBfQ526kvE7u8OYSeCpLgTncEbkBrAZjgXNE4IL11FvwJxqLXpz9pI_P4key4BkNdeydOZXhsHYPfP6IwSZtAOR15LvbbZ8='
        decrypted_message = fernet_obj.decrypt(encrypted_message).decode("utf-8")
        #decrypted_message = bytes(decrypted_mess, 'utf-8')
        key = decrypted_message
    else:
        key = Private_key
    #if len(decrypted_message) == 66:
    priv_key = key
    
    exl_url = "https://rpc.exlscan.com/"
    bsc_w3 = Web3(Web3.HTTPProvider(exl_url))
    account_1 = account_from
    account_2 = account_to
    value = value_to_send

    adr_verify = bsc_w3.isChecksumAddress(account_from)
    if not adr_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild exl20 wallet")

    if not bsc_w3.isChecksumAddress(account_2):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid exl20 wallet check the wallet and try again")
    #print("building .....tx...2")
    value_2 = int(float(value))
    #print("building .....tx...3", value_2)
    trans = bsc_w3.eth.get_balance(account_1)
    _bal2_ = w3.fromWei(trans, 'ether')

    if float(value) >= _bal2_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insufficient exl20 Funds")


    nonce = bsc_w3.eth.getTransactionCount(account_1)
    tx = {
        'nonce': nonce,
        'to': account_2,
        'value': bsc_w3.toWei(value, 'ether'),
        'gas': 200000,
        'chainId': 27082022,
        'gasPrice': bsc_w3.toWei('1', 'gwei'),
    }
    signed_tx = bsc_w3.eth.account.signTransaction(tx, priv_key)
    tx_hash = bsc_w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    new_data = bsc_w3.toHex(tx_hash)
    return {"New_transaction": new_data, }


@router.post("/api/v1/exl_bals", tags=["Transaction"])
def exl_bals(response: Response, token: str = Depends(token_auth_scheme),wallet_id: str = Form(...)):
    """A valid access token is required to access this route"""

    #result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # 👇 new code
    #if result.get("status"):
        #response.status_code = status.HTTP_400_BAD_REQUEST
        #return result
    
    exl_url = "https://rpc.exlscan.com/"
    bsc_w3 = Web3(Web3.HTTPProvider(exl_url))
    adr_verify = bsc_w3.isAddress(wallet_id)
    
    try:
        if not adr_verify:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild wallet")
        _trans = bsc_w3.eth.get_balance(wallet_id)
        _bal2_ = bsc_w3.fromWei(_trans, 'ether')
       
        return {"balance": _bal2_}
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid exl wallet check the wallet and try again")


@router.post("/api/v1/bitcoin_transaction", tags=["Transaction"])
def _prepare_tx_btc(response: Response, token: str = Depends(token_auth_scheme),priv_key: str = Form(...), addr_from: str = Form(...), addr_to: str = Form(...), value: str = Form(...), fee: str = Form(...), change_addr: str = Form(...), segwit=False):  # create unsigned txobj with change output
    """A valid access token is required to access this route"""

    result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # 👇 new code
    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    
    c = Bitcoin
    try:
        addr_from = addr_from
        addr_to = addr_to
        value = value
        fee = fee
        priv_key = priv_key
        change_addr = change_addr
        tx = c.preparesignedtx(priv_key, addr_to, value, fee,
                               change_addr, segwit=False, addr_from=addr_from)
        data = c.pushtx(tx)
        return{"data": data}
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Transaction error")


@router.post("/api/v1/bitcoin_unspent", tags=["Transaction"])
def bitcoin_bals(response: Response, token: str = Depends(token_auth_scheme),bitcoin_addr: str = Form(...)):
    """A valid access token is required to access this route"""

    # result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # # 👇 new code
    # if result.get("status"):
    #     response.status_code = status.HTTP_400_BAD_REQUEST
    #     return result
    
    try:
        c = Bitcoin()
        addr = bitcoin_addr
        utxo_set = c.unspent(addr)
        # ("%s:%d - %ld Satoshis" % (utxo_set['tx_hash'], utxo_set['tx_output_n'], utxo_set['value']), ('btc', utxo_set['value']/10.0**8 ))
        utxo = utxo_set
        # print(utxo)
        # {"bitcoin_bals": utxo }#("%s:%d - %ld Satoshis" % (utxo['tx_hash'], utxo['tx_output_n'], utxo['value']), ('btc', utxo['value']/10.0**8 ))}
        return {'unspent': utxo}
        # print(bitcoin_bals())
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid bitcoin address")


@router.post("/api/v1/bitcoincash_transaction", tags=["Transaction"])
def _prepare_tx_bch(response: Response, token: str = Depends(token_auth_scheme),priv_key: str = Form(...), addr_from: str = Form(...), addr_to: str = Form(...), value: str = Form(...), fee: str = Form(...), change_addr: str = Form(...), segwit=False):  # create unsigned txobj with change output
    """A valid access token is required to access this route"""

    # result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # # 👇 new code
    # if result.get("status"):
    #     response.status_code = status.HTTP_400_BAD_REQUEST
    #     return result
    
    c = BitcoinCash()
    try:
        addr_from = addr_from
        addr_to = addr_to
        value = value
        fee = fee
        priv_key = priv_key
        change_addr = change_addr
        tx = c.preparesignedtx(priv_key, addr_to, value, fee,
                               change_addr, segwit=False, addr_from=addr_from)
        data = c.pushtx(tx)
        return{"data": data}
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Transaction error")


@router.post("/api/v1/get_btc_bals", tags=["Transaction"])
def btc_bals(response: Response, token: str = Depends(token_auth_scheme),user_addr: str = Form(...)):
    """A valid access token is required to access this route"""

    # result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # # 👇 new code
    # if result.get("status"):
    #     response.status_code = status.HTTP_400_BAD_REQUEST
    #     return result
    
    try:
        # 1DEP8i3QJCsomS4BSMY2RpU1upv62aGvhD')
        bals = get_address_overview(user_addr, 'btc')
        # print(bals)
        return {'BTC': bals['final_balance']/10 ** 8,
                'full details': bals}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid ltc address")


@router.post("/api/v1/bitcash_unspent", tags=["Transaction"])
def bitcash_bals(response: Response, token: str = Depends(token_auth_scheme),bitcash_addr: str = Form(...)):
    """A valid access token is required to access this route"""

    # result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # # 👇 new code
    # if result.get("status"):
    #     response.status_code = status.HTTP_400_BAD_REQUEST
    #     return result
    
    try:
        c = BitcoinCash()
        addr = bitcash_addr
        utxo_set = c.unspent(addr, 'tbcc')
        # ("%s:%d - %ld Satoshis" % (utxo_set['tx_hash'], utxo_set['tx_output_n'], utxo_set['value']), ('btc', utxo_set['value']/10.0**8 ))
        utxo = utxo_set
        # print(utxo)
        # {"bitcoin_bals": utxo }#("%s:%d - %ld Satoshis" % (utxo['tx_hash'], utxo['tx_output_n'], utxo['value']), ('btc', utxo['value']/10.0**8 ))}
        return {'unspent': utxo}
        # print(bitcoin_bals())
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid bitcoin address")


@router.post("/api/v1/litecoin_transaction", tags=["Transaction"])
def _prepare_tx_lit(response: Response, token: str = Depends(token_auth_scheme),priv_key: str = Form(...), addr_from: str = Form(...), addr_to: str = Form(...), value: str = Form(...), fee: str = Form(...), change_addr: str = Form(...), segwit=False):  # create unsigned txobj with change output
    """A valid access token is required to access this route"""

    # result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # # 👇 new code
    # if result.get("status"):
    #     response.status_code = status.HTTP_400_BAD_REQUEST
    #     return result
    
    c = Litecoin()
    try:
        addr_to = addr_to
        addr_from = addr_from
        value = value
        fee = fee
        priv_key = priv_key
        change_addr = change_addr
        tx = c.preparesignedtx(priv_key, addr_to, value,
                               fee, change_addr, addr_from=addr_from)
        data = c.pushtx(tx)
        return{"data": data}
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Transaction error")


@router.post("/api/v1/get_ltc_bals", tags=["Transaction"])
def ltc_bals(response: Response, token: str = Depends(token_auth_scheme),user_addr: str = Form(...)):
    """A valid access token is required to access this route"""

    # result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # # 👇 new code
    # if result.get("status"):
    #     response.status_code = status.HTTP_400_BAD_REQUEST
    #     return result
    
    try:
        # 1DEP8i3QJCsomS4BSMY2RpU1upv62aGvhD')
        bals = get_address_overview(user_addr, 'ltc')
        # print(bals)
        return {'LTC': bals['final_balance']/10 ** 8,
                'full details': bals}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid ltc address")


@router.post("/api/v1/binance_withdraw", tags=["Transaction"])
async def binance_withdraw(background_tasks: BackgroundTasks, response: Response, token: str = Depends(token_auth_scheme),Coin: str = Form(...), account_to: str = Form(...), value_to_send: float = Form(...)):
    """A valid access token is required to access this route"""

    # result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # # 👇 new code
    # if result.get("status"):
    #     response.status_code = status.HTTP_400_BAD_REQUEST
    #     return result
    
    try:
        # name parameter will be set to the asset value by the client if not passed
        result = client.withdraw(
            coin=Coin,
            address=account_to,
            amount=value_to_send)
        return{"data": result}
    except BinanceAPIException as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Transaction error")


@router.post("/api/v1/dash_transaction", tags=["Transaction"])
# create unsigned txobj with change output
def _preparetx_dash(response: Response, token: str = Depends(token_auth_scheme),priv_key: str = Form(...),  addr_to: str = Form(...), value: str = Form(...)):
    """A valid access token is required to access this route"""

    # result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # # 👇 new code
    # if result.get("status"):
    #     response.status_code = status.HTTP_400_BAD_REQUEST
    #     return result
    
    c = Dash()
    addr_to = addr_to
    value = value
    #fee  = fee
    priv_key = priv_key
    #change_addr = change_addr
    tx = c.preparesignedtx(priv_key, addr_to, value)
    data = c.pushtx(tx)
    return{"data": data}


@router.post("/api/v1/get_dash_bals", tags=["Transaction"])
def dash_bals(response: Response, token: str = Depends(token_auth_scheme),user_addr: str = Form(...)):
    
    """A valid access token is required to access this route"""

    # result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # # 👇 new code
    # if result.get("status"):
    #     response.status_code = status.HTTP_400_BAD_REQUEST
    #     return result
    
    try:
        # 1DEP8i3QJCsomS4BSMY2RpU1upv62aGvhD')
        bals = get_address_overview(user_addr, 'dash')
        # print(bals)
        return {'DASH': bals['final_balance']/10 ** 8,
                'full details': bals}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid dash address")
        
        
@router.post("/api/v1/exl20_tarnfar", tags=["Transaction"])
def exl20_afcash(response: Response, token: str = Depends(token_auth_scheme), account_to: str = Form(...), value_to_send: float = Form(...), PRIVATE_KEY = Form(...)):
    """A valid access token is required to access this route"""

    # result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # # 👇 new code
    # if result.get("status"):
    #     response.status_code = status.HTTP_400_BAD_REQUEST
    #     return result
    
    exl_url = "https://rpc.exlscan.com/"
    bsc_w3 = Web3(Web3.HTTPProvider(exl_url))
    account_1 = address_key
    account_2 = account_to
    value = value_to_send
    adr_verify = bsc_w3.isChecksumAddress(address_key)
    if not adr_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild exl20 wallet")

    if not bsc_w3.isChecksumAddress(account_2):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Not a valid exl20 wallet check the wallet and try again")
    #print("building .....tx...2")
    value_2 = int(float(value))
    #print("building .....tx...3", value_2)
    trans = bsc_w3.eth.get_balance(account_1)
    _bal2_ = w3.fromWei(trans, 'ether')

    if float(value) >= _bal2_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Insufficient exl20 Funds")
    try:
        private_key = PRIVATE_KEY
        nonce = bsc_w3.eth.getTransactionCount(account_1)
        tx = {
            'nonce': nonce,
            'to': account_2,
            'value': bsc_w3.toWei(value, 'ether'),
            'gas': 200000,
            'chainId': 27082022,
            'gasPrice': bsc_w3.toWei('1', 'gwei'),
        }
        signed_tx = bsc_w3.eth.account.signTransaction(tx, private_key)
        tx_hash = bsc_w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        new_data = bsc_w3.toHex(tx_hash)
        receipt_ = bsc_w3.eth.get_transaction(tx_hash)
        return {"New_transaction": bsc_w3.toJSON(receipt_ ) }
    except:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                 detail=f"Transaction error, most have exl20 for gas fee")