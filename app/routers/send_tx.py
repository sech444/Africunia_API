from ast import Not, Return
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
import decimal 
from blockcypher import get_address_overview


router = APIRouter()

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/bde4e3babba54474844b65de59d0a039'))

load_dotenv()
#w3 = os.getenv("w3")
API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
etherscan_API = os.getenv("etherscan_API")
BASE_URL = 'https://api.binance.com'

headers = {
    'X-MBX-APIKEY': API_KEY
}


client = Client(API_KEY,SECRET_KEY )


@router.post("/api/v1/get_eth_bals", tags=["Transaction"])
def Get_eth_bals(user_adr: str = Form(...)):
    adr_verify = Web3.isAddress(user_adr.upper())
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
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid eth wallet check the wallet and try again")
   



@router.post("/api/v1/eth_tarnsaction", tags=["Transaction"])
async def eth_tarnsaction(background_tasks:BackgroundTasks,account_from:str = Form(...), account_to: str = Form(...),value_to_send: float=Form(...), private_key: str=Form(...)):
    #checking the wallet if the are eth wallets
    adr_verify = w3.isAddress(account_from)
    if not adr_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"account_from Not a valid ETH wallet check the wallet and try again")
    account_2 = account_to 
    if not Web3.isChecksumAddress(account_to):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"account_to Not a valid ETH wallet check the wallet and try again")
            
    value    = value_to_send 
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
        
        asyncio.sleep(3)


        return{"data" : json.dumps(order, indent=2)}
    except BinanceAPIException as e:
        #print(e)
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


# using web3py to Transfer usdt tether bep20 from one account to other  account with binance

@router.post("/api/v1/usdt_bep20_tarnsaction", tags=["Transaction"])
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


@router.post("/api/v1/usdt_erc20_bals", tags=["Transaction"])
def usdt_bals(wallet_id: str=Form(...) ):
    url = "https://api.etherscan.io/api"
    apikey = etherscan_API
    adr_verify = Web3.isAddress(wallet_id)
    if not adr_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild wallet")
    params = {"module": "account", "action": "balance", "address": wallet_id, "tag": "latest", "apikey": apikey}
    response = requests.get(url, params=params).json()
    total_balance = int(response["result"]) / (10**18)
    try:
        if not float(total_balance):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid wallet check the wallet and try again")
        total_bal = w3.fromWei(total_balance, 'ether')
        return {"balance": total_balance}
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid BNB wallet check the wallet and try again")
        
        
@router.post("/api/v1/usdt_erc20_tarnsaction", tags=["Transaction"])
def usdt_tarnsaction(account_from:str = Form(...), account_to: str = Form(...),value_to_send: float=Form(...), private_key: str=Form(...)):
    usdt_ = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
    account_1 = account_from 
    account_2 = account_to 
    value    = value_to_send  
    
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
                'to' : account_2,
                'value': w3.toWei(value, 'ether'),
                'nonce': w3.eth.get_transaction_count(adr_verify),
            })
        signed = w3.eth.account.sign_transaction(input_balance, private_key=private_key)
        tx = w3.eth.send_raw_transaction(signed.rawTransaction)
        #print(f"Swap tx: {web3.toHex(tx)}")
        return {"Swap tx": w3.toHex(tx)}      
    except ValueError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail=f"Transaction error, most have BNB for gas fee")


@router.post("/api/v1/bnb_", tags=["Transaction"])
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
   



@router.post("/api/v1/busd_tarnsaction", tags=["Transaction"])
def busd_tarnsaction(account_from:str = Form(...), account_to: str = Form(...),value_to_send: float=Form(...), private_key: str=Form(...)):
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


@router.post("/api/v1/busd_bals", tags=["Transaction"])
def busd_bals(wallet_id: str=Form(...) ):
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


@router.post("/api/v1/exl_afcash_bals", tags=["Transaction"])
def exl_afcash_bals(wallet_id: str=Form(...) ):
    exl_url = "https://rpc.exlscan.com/"
    bsc_w3 = Web3(Web3.HTTPProvider(exl_url))
    adr_verify = bsc_w3.isAddress(wallet_id)
    if not adr_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invaild wallet")
    _trans = bsc_w3.eth.get_balance(wallet_id)
    _bal2_ = bsc_w3.fromWei(_trans, 'ether')
    try:
        if not float(_bal2_):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid BNB wallet check the wallet and try again")
        
        return {"balance": _bal2_}
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid BNB wallet check the wallet and try again")
   


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

@router.post("/api/v1/bitcoin_unspent", tags=["Transaction"])
def bitcoin_bals(bitcoin_addr: str=Form(...)):
    try:
        c = Bitcoin()
        addr = bitcoin_addr
        utxo_set = c.unspent(addr)
        utxo = utxo_set#("%s:%d - %ld Satoshis" % (utxo_set['tx_hash'], utxo_set['tx_output_n'], utxo_set['value']), ('btc', utxo_set['value']/10.0**8 ))
        #print(utxo)
        return {'unspent': utxo } #{"bitcoin_bals": utxo }#("%s:%d - %ld Satoshis" % (utxo['tx_hash'], utxo['tx_output_n'], utxo['value']), ('btc', utxo['value']/10.0**8 ))}
        #print(bitcoin_bals())
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid bitcoin address")



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
        
@router.post("/api/v1/get_btc_bals", tags=["Transaction"])   
def btc_bals(user_addr: str = Form(...)):
    try:
        bals = get_address_overview(user_addr, 'btc')#1DEP8i3QJCsomS4BSMY2RpU1upv62aGvhD')
        print(bals)
        return {'BTC':bals['final_balance']/10 **8,
                'full details': bals}
    except:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid ltc address") 

@router.post("/api/v1/bitcash_unspent", tags=["Transaction"])
def bitcash_bals(bitcash_addr: str=Form(...)):
    try:
        c = BitcoinCash()
        addr = bitcash_addr
        utxo_set = c.unspent(addr, 'tbcc')
        utxo = utxo_set#("%s:%d - %ld Satoshis" % (utxo_set['tx_hash'], utxo_set['tx_output_n'], utxo_set['value']), ('btc', utxo_set['value']/10.0**8 ))
        #print(utxo)
        return {'unspent': utxo } #{"bitcoin_bals": utxo }#("%s:%d - %ld Satoshis" % (utxo['tx_hash'], utxo['tx_output_n'], utxo['value']), ('btc', utxo['value']/10.0**8 ))}
        #print(bitcoin_bals())
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid bitcoin address")



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
            
@router.post("/api/v1/get_ltc_bals", tags=["Transaction"])   
def ltc_bals(user_addr: str = Form(...)):
    try:
        bals = get_address_overview(user_addr, 'ltc')#1DEP8i3QJCsomS4BSMY2RpU1upv62aGvhD')
        print(bals)
        return {'LTC':bals['final_balance']/10 **8,
                'full details': bals}
    except:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid ltc address") 
    


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
    
    
@router.post("/api/v1/get_dash_bals", tags=["Transaction"])   
def dash_bals(user_addr: str = Form(...)):
    try:
        bals = get_address_overview(user_addr, 'dash')#1DEP8i3QJCsomS4BSMY2RpU1upv62aGvhD')
        print(bals)
        return {'DASH':bals['final_balance']/10 **8,
                'full details': bals}
    except:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid dash address") 
    
    