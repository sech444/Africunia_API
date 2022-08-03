from ast import Not
from cmath import e
from fastapi import FastAPI, WebSocket, BackgroundTasks, APIRouter, Depends, status, HTTPException, Form
import json
from binance.exceptions import BinanceAPIException
from typing import List, Optional
import requests
from web3 import Web3, EthereumTesterProvider,HTTPProvider
from uuid import uuid4
from bitcoin import *
from binance.client import Client
import binascii
import time
import hmac
import hashlib
from urllib.parse import urljoin, urlencode
from eth_account import Account
from cryptos import *
from dotenv import load_dotenv
import os
import re
import asyncio


router = APIRouter()

w3 = Web3(Web3.HTTPProvider('https://rinkeby.infura.io/v3/bde4e3babba54474844b65de59d0a039'))

usdt_abi = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_upgradedAddress","type":"address"}],"name":"deprecate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"deprecated","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_evilUser","type":"address"}],"name":"addBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"upgradedAddress","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balances","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"maximumFee","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_maker","type":"address"}],"name":"getBlackListStatus","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowed","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getOwner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"newBasisPoints","type":"uint256"},{"name":"newMaxFee","type":"uint256"}],"name":"setParams","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"issue","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"redeem","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"basisPointsRate","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"isBlackListed","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_clearedUser","type":"address"}],"name":"removeBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"MAX_UINT","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_blackListedUser","type":"address"}],"name":"destroyBlackFunds","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_initialSupply","type":"uint256"},{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},{"name":"_decimals","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Issue","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Redeem","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"newAddress","type":"address"}],"name":"Deprecate","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"feeBasisPoints","type":"uint256"},{"indexed":false,"name":"maxFee","type":"uint256"}],"name":"Params","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_blackListedUser","type":"address"},{"indexed":false,"name":"_balance","type":"uint256"}],"name":"DestroyedBlackFunds","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_user","type":"address"}],"name":"AddedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_user","type":"address"}],"name":"RemovedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"}]'

TetherToken_addr = '0xdAC17F958D2ee523a2206206994597C13D831ec7'

load_dotenv()
#w3 = os.getenv("w3")
API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
BASE_URL = 'https://api.binance.com'

headers = {
    'X-MBX-APIKEY': API_KEY
}


client = Client(API_KEY,SECRET_KEY )


@router.post("/api/v1/get_eth_bals", tags=["Transaction"])
def Get_eth_bals(user_adr: str = Form(...)):
    adr_verify = Web3.isAddress(user_adr)
    if not adr_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild wallet")
    _trans = w3.eth.get_balance(user_adr)
    _bal2_ = w3.fromWei(_trans, 'ether')
    try:
        if  not _bal2_:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid eth wallet check the wallet and try again")
        
        return {"balance": _bal2_}
    except ValueError:
        raise e
   



@router.post("/api/v1/eth_tarnsaction", tags=["Transaction"])
async def eth_tarnsaction(background_tasks:BackgroundTasks,account_from:str = Form(...), account_to: str = Form(...),value_to_send: float=Form(...), private_key: str=Form(...)):
    account_1 = account_from 
    adr_verify = w3.isAddress(account_from)
    if not adr_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild wallet")
    account_2 = account_to 
    if not Web3.isChecksumAddress(account_2):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid ETH wallet check the wallet and try again")
            
    value    = value_to_send 
    
    value_2 = int(float(value)) 
    trans = w3.eth.get_balance(value_2)
    _bal2_ = w3.fromWei(trans, 'ether')    
    if float(value) > _bal2_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Insufficient ETH Funds")          
    private_key = private_key  
    addr = account_2
     
    nonce = w3.eth.getTransactionCount(account_1)

    tx = {
                    'nonce': nonce,
                    'to': account_2,
                    'value': w3.toWei(value, 'ether'),
                    'gas': 200000,
                    'gasPrice': w3.toWei('50', 'gwei'),
                }
        
        


    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash =  w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    new_data= (w3.toHex(tx_hash))
    return {"New_tarnsation": new_data , }


@router.post("/api/v1/create_Order_buy", tags=["Transaction"])
def create_Order(symbol: str = Form(...),quantity: float = Form(...)):
    try:
        order = client.order_market_buy(
                    symbol=symbol.upper(),
                    quantity=quantity)


        return{"data" : json.dumps(order, indent=2)}
    except BinanceAPIException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid tarnsation check the symbol eg. BNBUSDT then quantity >= 10.38USDT and try again")


@router.post("/api/v1/create_Order_sell", tags=["Transaction"])
def create_Order(symbol: str = Form(...),quantity: float = Form(...)):
    try:
        order = client.order_market_sell(
                    symbol=symbol.upper(),
                    quantity=quantity)
        
        asyncio.sleep(5)


        return{"data" : json.dumps(order, indent=2)}
    except BinanceAPIException as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid tarnsation check the symbol eg. BNBUSDT then quantity >= 10.38USDT or Account has insufficient balance for requested action, symbol like this BTCUSDT")


@router.post("/api/v1/Order_status", tags=["Transaction"])
def create_Order(symbol: str = Form(...),order_Id: int = Form(...)):
    try:
        order = client.get_order(
            symbol=symbol.upper(),
            orderId=order_Id)#4136872022)
        
        return{"data" : order}
    except BinanceAPIException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid tarnsation check the symbol eg. BNBUSDT then orderid eg. 4136872022 and try again")
            
     
@router.post("/api/v1/asset_balance", tags=["Transaction"])
def create_Order(asset_symbol: str = Form(...)):
    try:   
        bals = client.get_asset_balance(asset=asset_symbol.upper())
        return{"data" : bals}
    except BinanceAPIException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid tarnsation check the asset symbol eg. BNB , USDT ")

@router.post("/api/v1/get_deposit_address", tags=["Transaction"])
def get_deposit_address(asset_symbol: str = Form(...)):
    try:   
        bals = client.get_deposit_address(coin=asset_symbol.upper())
        return{"data" : bals}
    except BinanceAPIException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid tarnsation check the asset symbol eg. BNB , USDT ")


@router.post("/api/v1/bnb_bals", tags=["Transaction"])
def bnb_bals(wallet_id: str=Form(...) ):
    bsc = "https://bsc-dataseed.binance.org/"
    adr_verify = Web3.isAddress(wallet_id)
    if not adr_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild wallet")
    _trans = w3.eth.get_balance(wallet_id)
    _bal2_ = w3.fromWei(_trans, 'ether')
    try:
        if not float(_bal2_):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid BNB wallet check the wallet and try again")
        
        return {"balance": _bal2_}
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid BNB wallet check the wallet and try again")
   

# using web3py to Transfer usdt tether bep20 from one account to other  account with binance

@router.post("/api/v1/usdt_tarnsaction", tags=["Transaction"])
def usdt_tarnsaction(account_from:str = Form(...), account_to: str = Form(...),value_to_send: float=Form(...), private_key: str=Form(...)):
    bsc = "https://bsc-dataseed.binance.org/"
    bsc_w3 = Web3(Web3.HTTPProvider(bsc))
    account_1 = account_from 
    account_2 = account_to 
    value    = value_to_send  
                          
    private_key = private_key  
    addr = account_2
     
    nonce = w3.eth.getTransactionCount(account_1)

    tx = {
                    'nonce': nonce,
                    'to': account_2,
                    'value': bsc_w3.toWei(value, 'ether'),
                    'gas': 200000,
                    'gasPrice': bsc_w3.toWei('50', 'gwei'),
                }
        
    signed_tx = bsc_w3.eth.account.signTransaction(tx, private_key)
    tx_hash =  bsc_w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    new_data= (bsc_w3.toHex(tx_hash))
    return {"New_tarnsation": new_data , }


@router.post("/api/v1/bnb_tarnsaction", tags=["Transaction"])
def bnb_tarnsaction(account_from:str = Form(...), account_to: str = Form(...),value_to_send: float=Form(...), private_key: str=Form(...)):
    bsc = "https://bsc-dataseed.binance.org/"
    bsc_w3 = Web3(Web3.HTTPProvider(bsc))
    account_1 = account_from 
    account_2 = account_to 
    value    = value_to_send  
    
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
     
    nonce = w3.eth.getTransactionCount(account_1)

    tx = {
                    'nonce': nonce,
                    'to': account_2,
                    'value': bsc_w3.toWei(value, 'ether'),
                    'gas': 200000,
                    'gasPrice': bsc_w3.toWei('50', 'gwei'),
                }
        
    signed_tx = bsc_w3.eth.account.signTransaction(tx, private_key)
    tx_hash =  bsc_w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    new_data= (bsc_w3.toHex(tx_hash))
    return {"New_tarnsation": new_data , }



@router.post("/api/v1/exl_afcash_tarnsaction", tags=["Transaction"])
def exl_afcash(account_from:str = Form(...), account_to: str = Form(...),value_to_send: float=Form(...), private_key: str=Form(...)):
    exl_url = "https://rpc.exlscan.com/"
    bsc_w3 = Web3(Web3.HTTPProvider(exl_url))
    account_1 = account_from 
    account_2 = account_to 
    value    = value_to_send  
    
    adr_verify = bsc_w3.isChecksumAddress(account_from)
    if not adr_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild wallet")
        
   
    if not bsc_w3.isChecksumAddress(account_2):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid ETH wallet check the wallet and try again")
    print("building .....tx...2")
    value_2 = int(float(value)) 
    print("building .....tx...3" , value_2 )
    trans = bsc_w3.eth.get_balance(account_1)
    _bal2_ = w3.fromWei(trans, 'ether') 
      
    if float(value) >= _bal2_:
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
                    'chainId': 27082022,
                    'gasPrice': bsc_w3.toWei('1', 'gwei'),
                }   
    signed_tx = bsc_w3.eth.account.signTransaction(tx, private_key)
    tx_hash =  bsc_w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    new_data= bsc_w3.toHex(tx_hash)
    return {"New_tarnsation": new_data , }




@router.post("/api/v1/bitcoin_transaction", tags=["Transaction"])
def _prepare_tx_btc(priv_key:str = Form(...), addr_from:str = Form(...), addr_to:str = Form(...), value:str = Form(...), fee:str = Form(...), change_addr:str = Form(...),segwit=False):  #create unsigned txobj with change output
    c = Bitcoin
    try:
        addr_from = addr_from
        addr_to = addr_to
        value = value
        fee  = fee
        priv_key = priv_key
        change_addr = change_addr
        tx = c.preparesignedtx(priv_key, addr_to, value, fee, change_addr, segwit=False, addr_from = addr_from)
        data = c.pushtx(tx)
        return{"data": data }
    except ValueError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail=f"Transaction error")


@router.post("/api/v1/bitcoincash_transaction", tags=["Transaction"])
def _prepare_tx_bch(priv_key:str = Form(...), addr_from:str = Form(...), addr_to:str = Form(...), value:str = Form(...), fee:str = Form(...), change_addr:str = Form(...),segwit=False):  #create unsigned txobj with change output
    c = BitcoinCash()
    try:   
        addr_from = addr_from
        addr_to = addr_to
        value = value
        fee  = fee
        priv_key = priv_key
        change_addr = change_addr
        tx = c.preparesignedtx(priv_key, addr_to, value, fee, change_addr, segwit=False, addr_from = addr_from)
        data = c.pushtx(tx)
        return{"data": data }
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Transaction error")

@router.post("/api/v1/litecoin_transaction", tags=["Transaction"])
def _prepare_tx_lit(priv_key:str = Form(...), addr_from:str = Form(...), addr_to:str = Form(...), value:str = Form(...), fee:str = Form(...), change_addr:str = Form(...),segwit=False):  #create unsigned txobj with change output
    c = Litecoin()
    try:
        addr_to = addr_to
        addr_from = addr_from
        value = value
        fee  = fee
        priv_key = priv_key
        change_addr = change_addr
        tx = c.preparesignedtx(priv_key, addr_to, value, fee, change_addr, addr_from = addr_from)
        data = c.pushtx(tx)
        return{"data": data }
    except ValueError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail=f"Transaction error")


@router.post("/api/v1/binance_withdraw", tags=["Transaction"])
async def binance_withdraw(background_tasks:BackgroundTasks,Coin:str = Form(...), account_to: str = Form(...),value_to_send: float=Form(...)):
    try:
        # name parameter will be set to the asset value by the client if not passed
        result = client.withdraw(
            coin= Coin,
            address = account_to,
            amount= value_to_send)
        return{"data": result}
    except BinanceAPIException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail=f"Transaction error")


@router.post("/api/v1/dash_transaction", tags=["Transaction"])
def _preparetx_dash(priv_key:str = Form(...),  addr_to:str = Form(...), value:str = Form(...)):  #create unsigned txobj with change output
    c = Dash()
    addr_to = addr_to
    value = value
    #fee  = fee
    priv_key = priv_key
    #change_addr = change_addr
    tx = c.preparesignedtx(priv_key, addr_to, value)
    data = c.pushtx(tx)
    return{"data": data }
    
    