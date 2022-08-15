from fastapi import FastAPI, WebSocket, BackgroundTasks, APIRouter, Depends, status, HTTPException, Form
import json
from typing import List, Optional
from web3 import Web3, EthereumTesterProvider,HTTPProvider
from cryptos import *
import requests
from blockcypher import  get_transaction_details
#from app.schemas import web_hook

router = APIRouter()


w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/bde4e3babba54474844b65de59d0a039'))




@router.post('/api/v1/api/eth_webhook', tags=["WebHook"])
def eth_transaction_receipt(tx_hash:str = Form(...),webhook_url:str = Form(...)) -> dict():
    try:
        receipt_ = w3.eth.get_transaction(tx_hash)
        w3.toJSON(receipt_ ['hash'])
        data = {
            'acc': 'transaction',
            'details': w3.toJSON(receipt_ ),
        }
        r=requests.post(webhook_url,data=json.dumps(data))

        return {"data" : w3.toJSON(receipt_ )}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid eth tx_hash")


@router.post('/api/v1/api/exl_webhook', tags=["WebHook"])
def transaction_receipt(tx_hash:str = Form(...),webhook_url:str = Form(...)) -> dict():
    try:
        exl_url = "https://rpc.exlscan.com/"
        bsc_w3 = Web3(Web3.HTTPProvider(exl_url))
        receipt_ = bsc_w3.eth.get_transaction(tx_hash)
        data = {
            'acc': 'transaction',
            'details': bsc_w3.toJSON(receipt_ ),
        }
        r=requests.post(webhook_url, data=json.dumps(data))

        return {"data" : bsc_w3.toJSON(receipt_ )}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid exl tx_hash")



@router.post('/api/v1/api/bnb_webhook', tags=["WebHook"])
def transaction_receipt(tx_hash:str = Form(...),webhook_url:str = Form(...)) -> dict():
    try:
        bsc = "https://bsc-dataseed.binance.org/"
        bsc_w3 = Web3(Web3.HTTPProvider(bsc))
        receipt_ = bsc_w3.eth.get_transaction(tx_hash)
        data = {
            'acc': 'transaction',
            'details': bsc_w3.toJSON(receipt_ ),
        }
        r=requests.post(webhook_url,data=json.dumps(data))

        return {"data" : bsc_w3.toJSON(receipt_ )}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid bnb tx_hash")

@router.post("/api/v1/btc_webhook", tags=["WebHook"])
def btc_webhook(btc_txhash: str = Form(...),webhook_url: str = Form(...)):
    try:
        c = Bitcoin()
        tx_hash = c.fetchtx(btc_txhash)
        data = {
            'acc': 'transaction',
            'details': tx_hash
        }
        r=requests.post(webhook_url,data=json.dumps(data))
        
        return {"btc_txhash": tx_hash}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid btc tx_hash")


@router.post("/api/v1/dash_webhook", tags=["WebHook"])
def dash_webhook(dash_txhash: str = Form(...),webhook_url: str = Form(...)):
    try:
        tx_hash = get_transaction_details(dash_txhash, 'dash')
        data = {
            'acc': 'transaction',
            'details': json.dumps(tx_hash, indent=2, sort_keys=True, default=str)

        }
        r=requests.post(webhook_url,data=json.dumps(data))
    
        return {"dash_txhash": tx_hash}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid dash tx_hash")

@router.post("/api/v1/ltc_webhook", tags=["WebHook"])
def ltc_webhook(ltc_txhash: str = Form(...),webhook_url: str = Form(...)):
    try:
        tx_hash = get_transaction_details(ltc_txhash, 'ltc')
        data = {
            'acc': 'transaction',
            'details': json.dumps(tx_hash, indent=2, sort_keys=True, default=str)

        }
        r=requests.post(webhook_url,data=json.dumps(data))
        
        return {"ltc_txhash": tx_hash}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid ltc tx_hash")
