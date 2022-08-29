import asyncio
from web3 import Web3
import decimal
from decimal import Decimal
from fastapi import FastAPI, WebSocket, BackgroundTasks, APIRouter, Depends, status, HTTPException, Form
import json
import requests as r


router = APIRouter()




# Change this to use your own RPC URL
web3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
# AggregatorV3Interface ABI
abi = '[{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"description","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint80","name":"_roundId","type":"uint80"}],"name":"getRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'
# Price Feed address
addr_ETH_USD = '0x9ef1B8c0E4F7dc8bF5719Ea496883DC6401d5b2e'
addr_USDT_USD = "0xB97Ad0E74fa7d920791E90258A6E2085088b4320"
addr_BUSB_USD = '0xcBb98864Ef56E9042e7d2efef76141f15731B82f'
addr_BNB_USD = '0x0567F2323251f0Aab15c8dFb1967E4e8A7D42aeE'
addr_BTC_USD = '0x264990fbd0A4796A3E3d8E37C4d5F87a3aCa5Ebf'
addr_BCH_USD = '0x43d80f616DAf0b0B42a928EeD32147dC59027D41'
addr_LTC_USD = '0x74E72F37A8c415c8f1a98Ed42E78Ff997435791D'
addr_TRX_USD = '0xF4C5e535756D11994fCBB12Ba8adD0192D9b88be'
addr_XLM_USD = '0x27Cc356A5891A3Fe6f84D0457dE4d108C6078888'
addr_XRP_USD = '0x93A67D414896A280bF8FFB3b389fE3686E014fda'
addr_USDT_BNB = '0xD5c40f5144848Bd4EF08a9605d860e727b991513'
addr_BTC_ETH = '0xf1769eB4D1943AF02ab1096D7893759F6177D6B8'
addr_BNB_USD = '0x0567F2323251f0Aab15c8dFb1967E4e8A7D42aeE'



# Set up contract instance
# Set up while loop for prices feed
def get_Ltccoin_Price(crypto_ltc):
    contract = web3.eth.contract(address=addr_LTC_USD, abi=abi)
    latestData = contract.functions.latestRoundData().call()
    prices = latestData[1]/ 10**8
    
    return prices


def main_ltc():
  
  last_price = -1
  
  while True:
    
    crypto = 'Litecoin'
    price = get_Ltccoin_Price(crypto)
  
    if price != last_price:
      #print('LTC_USD: ',price)
      last_price = price
    return last_price



# Set up while loop for prices feed
def get_ETH_USD(crypto_ltc):
    contract = web3.eth.contract(address=addr_ETH_USD, abi=abi)
    latestData = contract.functions.latestRoundData().call()
    prices= latestData[1]/ 10**8
    return float(prices)




def main_eth():
  
  last_price = -1
  
  while True:
    
    crypto = 'Ethereum'
    price = get_ETH_USD(crypto)
  
    if price != last_price:
      #print('ETH_USD: ',price)
      last_price = price
    return last_price
  



# Set up while loop for prices feed
def get_USDT_USD(crypto_ltc):
    contract = web3.eth.contract(address=addr_USDT_USD, abi=abi)
    latestData = contract.functions.latestRoundData().call()
    prices = latestData[1]/10 **8
    
    return prices



def main_usdt():
  
  last_price = -1
  
  while True:
    
    crypto = 'Tether'
    price = get_USDT_USD(crypto)
  
    if price != last_price:
      #print('USDT_USD: ',price)
      last_price = price
    return last_price
      



# Set up while loop for prices feed
def get_BUSB_USD(crypto_ltc):
    contract = web3.eth.contract(address=addr_BUSB_USD, abi=abi)
    latestData = contract.functions.latestRoundData().call()
    prices = latestData[1]/10 **8
    
    return prices




def main_busb():
  
  last_price = -1
  
  while True:
    
    crypto = 'bitcoin'
    price = get_BUSB_USD(crypto)
  
    if price != last_price:
      #print('BUSB_USD: ',price)
      last_price = price
    return last_price
      

# Set up while loop for prices feed
def get_BTC_USD(crypto_ltc):
    contract = web3.eth.contract(address=addr_BTC_USD, abi=abi)
    latestData = contract.functions.latestRoundData().call()
    prices = latestData[1]/10 **8
    
    return prices




def main_btc():
  
  last_price = -1
  
  while True:
    
    crypto = 'bitcoin'
    price = get_BTC_USD(crypto)
  
    if price != last_price:
      #print('BTC_USD: ',price)
      last_price = price
    return last_price


# Set up while loop for prices feed
def get_BCH_USD(crypto_ltc):
    contract = web3.eth.contract(address=addr_BCH_USD, abi=abi)
    latestData = contract.functions.latestRoundData().call()
    prices = latestData[1]/10 **8
    
    return prices




def main_bitcash():
  
  last_price = -1
  
  while True:
    
    crypto = 'bitcash'
    price = get_BCH_USD(crypto)
  
    if price != last_price:
      #print('BCH_USD: ',price)
      last_price = price
    return last_price
      



# Set up while loop for prices feed
def get_TRX_USD(crypto_ltc):
    contract = web3.eth.contract(address=addr_TRX_USD, abi=abi)
    latestData = contract.functions.latestRoundData().call()
    prices = latestData[1]/10 **8
    
    return prices



def main_trx():
  
  last_price = -1
  
  while True:
    
    crypto = 'Tron'
    price = get_TRX_USD(crypto)
  
    if price != last_price:
      #print('TRX_USD: ',price)
      last_price = price
    return last_price


# Set up while loop for prices feed
def get_XLM_USD(crypto_ltc):
    contract = web3.eth.contract(address=addr_XLM_USD, abi=abi)
    latestData = contract.functions.latestRoundData().call()
    prices = latestData[1]/10 **8
    
    return prices




def main_xlm():
  
  last_price = -1
  
  while True:
    
    crypto = 'Stellar'
    price = get_XLM_USD(crypto)
  
    if price != last_price:
      #print('XLM_USD: ',price)
      last_price = price
    return last_price
      


# Set up while loop for prices feed
def get_XRP_USD(crypto_ltc):
    contract = web3.eth.contract(address=addr_XRP_USD, abi=abi)
    latestData = contract.functions.latestRoundData().call()
    prices = latestData[1]/ 10**8
    
    return prices



def main_xrp():
  
  last_price = -1
  
  while True:
    
    crypto = 'Ripple'
    price = get_XRP_USD(crypto)
  
    if price != last_price:
      #print('XRP_USD: ',price)
      last_price = price
      return last_price
      




# Set up while loop for prices feed
def get_BNB_USD(crypto_ltc):
    contract = web3.eth.contract(address=addr_BNB_USD, abi=abi)
    latestData = contract.functions.latestRoundData().call()
    prices = latestData[1]/10 **8
    
    return prices




def main_bnb():
  
  last_price = -1
  
  while True:
    
    crypto = 'bitcoin'
    price = get_BNB_USD(crypto)
  
    if price != last_price:
      #print('XRP_USD: ',price)
      last_price = price
    return last_price
    


# Set up while loop for prices feed
def get_BTC_ETH(crypto_ltc):
    contract = web3.eth.contract(address=addr_BTC_ETH, abi=abi)
    latestData = contract.functions.latestRoundData().call()
    prices = latestData[1]/10 **18
    #print(1498.555*13.66)
    return prices




def main_btc_eth():
  
  last_price = -1
  
  while True:
    
    crypto = 'bitcoin'
    price = get_BTC_ETH(crypto)
  
    if price != last_price:
      #print('BTC_ETH: ',price)
      last_price = price
    return last_price
      





listData = [
    {
        "coin": "btc",
        "name": "Bitcoin",
        "rate": main_btc(),
        "coin_logo": "assets/img/btc.png"
    },
    {
        "coin": "bch",
        "name": "Bitcoin Cash",
        "rate": main_bitcash(),
        "coin_logo": "assets/img/bch.png"
    },
    {
        "coin": "ltc",
        "name": "Litecoin",
        "rate": main_ltc(),
        "coin_logo": "assets/img/ltc.png"
    },
    {
        "coin": "xrp",
        "name": "Ripple",
        "rate": main_xrp(),
        "coin_logo": "assets/img/xrp.png"
    },
    {
        "coin": "xlm",
        "name": "Stellar",
        "rate": main_xlm(),
        "coin_logo": "assets/img/xlm.png"
    },
    {
        "coin": "ether",
        "name": "Ethereum",
        "rate": main_eth(),
        "coin_logo": "assets/img/ether.png"
    },
     {
        "coin": "BNB",
        "name": "Binance Coin",
        "rate": main_bnb(),
        "coin_logo": "assets/img/bnb.png"
    },
    {
        "coin": "TRX",
        "name": "TRON Coin",
        "rate": main_trx(),
        "coin_logo": "assets\\/img\\/trx.png"
    },
    {
        "coin": "BUSD",
        "name": "Binance USD",
        "rate": main_busb(),
        "coin_logo": "assets\\/img\\/busd.png"
    },
     {
        "coin": "BTC_ETH",
        "name": "BTC_ETH",
        "rate": main_btc_eth(),
        "coin_logo": "assets\\/img\\/btc.png"
    },
     {
        "coin": "usdt",
        "name": "Tether",
        "rate": main_usdt(),
        "coin_logo": "assets\/img\/usdt.png"
    }

]

@router.get('/api/v1/oracle_chainlink_feeds',tags=["Coin_Price"])
def oracle_feeds():
    return{'oracle': listData}