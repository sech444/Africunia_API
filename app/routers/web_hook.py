from fastapi import FastAPI, WebSocket, BackgroundTasks, APIRouter, Depends, status, HTTPException, Form
import json
from typing import List, Optional
from web3 import Web3, EthereumTesterProvider,HTTPProvider
from cryptos import *
import requests
#from app.schemas import web_hook

router = APIRouter()


w3 = Web3(Web3.HTTPProvider('https://rinkeby.infura.io/v3/bde4e3babba54474844b65de59d0a039'))




@router.post('/api/v1/api/eth_webhook', tags=["WebHook"])
def eth_transaction_receipt(tx_hash:str = Form(...),webhook_url:str = Form(...)) -> dict():
    receipt_ = w3.eth.get_transaction(tx_hash)
    w3.toJSON(receipt_ ['hash'])
    data = {
        'acc': 'transaction',
        'details': w3.toJSON(receipt_ ),
    }
    r=requests.post(webhook_url,data=json.dumps(data))

    return {"data" : w3.toJSON(receipt_ )}


@router.post('/api/v1/api/exl_webhook', tags=["WebHook"])
def transaction_receipt(tx_hash:str = Form(...),webhook_url:str = Form(...)) -> dict():
    exl_url = "https://rpc.exlscan.com/"
    bsc_w3 = Web3(Web3.HTTPProvider(exl_url))
    receipt_ = bsc_w3.eth.get_transaction(tx_hash)
    data = {
        'acc': 'transaction',
        'details': bsc_w3.toJSON(receipt_ ),
    }
    r=requests.post(webhook_url, data=json.dumps(data))

    return {"data" : bsc_w3.toJSON(receipt_ )}



@router.post('/api/v1/api/bnb_webhook', tags=["WebHook"])
def transaction_receipt(tx_hash:str = Form(...),webhook_url:str = Form(...)) -> dict():
    bsc = "https://bsc-dataseed.binance.org/"
    bsc_w3 = Web3(Web3.HTTPProvider(bsc))
    receipt_ = bsc_w3.eth.get_transaction(tx_hash)
    data = {
        'acc': 'transaction',
        'details': bsc_w3.toJSON(receipt_ ),
    }
    r=requests.post(webhook_url,data=json.dumps(data))

    return {"data" : bsc_w3.toJSON(receipt_ )}


@router.post("/api/v1/bitcoin_unspent", tags=["WebHook"])
def bitcoin_bals(bitcoin_addr: str=Form(...)):
    c = Bitcoin()
    addr = bitcoin_addr
    utxo_set = c.unspent(addr)
    utxo = utxo_set#("%s:%d - %ld Satoshis" % (utxo_set['tx_hash'], utxo_set['tx_output_n'], utxo_set['value']), ('btc', utxo_set['value']/10.0**8 ))
    #print(utxo)
    return {'unspent': utxo } #{"bitcoin_bals": utxo }#("%s:%d - %ld Satoshis" % (utxo['tx_hash'], utxo['tx_output_n'], utxo['value']), ('btc', utxo['value']/10.0**8 ))}
#print(bitcoin_bals())


@router.post("/api/v1/btc_webhook", tags=["WebHook"])
def btc_webhook(btc_txhash: str = Form(...),webhook_url: str = Form(...)):
    c = Bitcoin()
    tx_hash = c.fetchtx(btc_txhash)
    data = {
        'acc': 'transaction',
        'details': tx_hash
    }
    r=requests.post(webhook_url,data=json.dumps(data))
    
    return {"btc_txhash": tx_hash}