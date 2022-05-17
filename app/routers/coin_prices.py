from fastapi import FastAPI, WebSocket, BackgroundTasks, APIRouter, Depends, status, HTTPException, Form
import json
from typing import List, Optional
import requests
import binance


router = APIRouter()


@router.get("/",tags=["Coin_Price"])
def root():
    return listData


def get_price(crypto):
    URL = 'https://www.bitstamp.net/api/ticker/btcusd/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")


def main():
    last_price = -1

    while True:

        crypto = 'bitcoin'
        price = get_price(crypto)

        if price != last_price:
           # print('Bitcoin price: ',price)
            last_price = price
    return 

@router.get('/api/v1/btcusd',tags=["Coin_Price"])
async def index(background_tasks: BackgroundTasks):
    background_tasks.add_task(main)
    return {
        "coin": "BTC",
        "name": "Bitcoin",
        "rate": get_price("bitcoin"),
        "coin_logo": "assets\/img\/btc.png"
    }
    

def get_price_bch(crypto_bchusd):
    URL = 'https://www.bitstamp.net/api/v2/ticker/bchusd/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")


def main_bch():
    last_price = -1

    while True:

        crypto_bchusd = 'bitcoin_cash'
        price = get_price_bch(crypto_bchusd)

        if price != last_price:
           # print('Bitcoin price: ',price)
            last_price = price
    return


@router.get('/api/v1/bch',tags=["Coin_Price"])
async def index_bch(background_tasks: BackgroundTasks):
    background_tasks.add_task(main_bch)
    return {
        "coin": "BCH",
        "name": "Bitcoin Cash",
        "rate": get_price_bch("bitcoin_cash"),
        "coin_logo": "assets\/img\/bch.png"
    }
    

def getethercoinPrice(crypto_ether):
    URL = 'https://www.bitstamp.net/api/v2/ticker/ethusd/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")


def main_ether():
    last_price = -1

    while True:

        crypto_ether = 'ether'
        price = getethercoinPrice(crypto_ether)

        if price != last_price:
           # print('Bitcoin price: ',price)
            last_price = price
    return


    

@router.get('/api/v1/ethusd',tags=["Coin_Price"])
async def index_eth(background_tasks: BackgroundTasks):
    background_tasks.add_task(main_ether)
    return {
        "coin": "eth",
        "name": "Ethereum",
        "rate": getethercoinPrice("ether"),
        "coin_logo": "assets\/img\/ether.png"
    }


def getXlmucoinPrice(crypto_xlmusd):
    URL = 'https://www.bitstamp.net/api/v2/ticker/xlmusd/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying xlmusd")


def main_Xlmusd():
    last_price = -1

    while True:

        crypto_xlmusd = 'Stellar'
        price = getXlmucoinPrice(crypto_xlmusd)

        if price != last_price:
           # print('Bitcoin price: ',price)
            last_price = price
    return


@router.get('/api/v1/xlmusd',tags=["Coin_Price"])
async def index_Stellar(background_tasks: BackgroundTasks):
    background_tasks.add_task(main_Xlmusd)
    return {
        "coin": "xlm",
        "name": "Stellar",
        "rate": getXlmucoinPrice("stellar"),
        "coin_logo": "assets\/img\/xlm.png"
        }
    

def getLtccoinPrice(crypto_ltc):
    URL = 'https://www.bitstamp.net/api/v2/ticker/ltcusd/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")


def main_ltc():
    last_price = -1

    while True:

        crypto_ltc = 'litecoin'
        price = getLtccoinPrice(crypto_ltc)

        if price != last_price:
           # print('Bitcoin price: ',price)
            last_price = price
    return


@router.get('/api/v1/ltc',tags=["Coin_Price"])
async def index_ltc(background_tasks: BackgroundTasks):
    background_tasks.add_task(main_ltc)
    return {
        "coin": "ltc",
        "name": "Litecoin",
        "rate": getLtccoinPrice('litercoin'),
        "coin_logo": "assets\/img\/ltc.png"
    }
    

def getxrpusprice(crypto_xrpusd):
    URL = 'https://www.bitstamp.net/api/v2/ticker/xrpusd/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")


def main_xrp():
    last_price = -1

    while True:

        crypto_xrpusd = 'Ripple'
        price = getxrpusprice(crypto_xrpusd)
        if price != last_price:
           # print('Bitcoin price: ',price)
            last_price = price
    return


@router.get('/api/v1/xrpusd',tags=["Coin_Price"])
async def index_xrp(background_tasks: BackgroundTasks):
    background_tasks.add_task(main_xrp)
    return {
        "coin": "xrp",
        "name": "Proton",
        "rate": getxrpusprice("Ripple"),
        "coin_logo": "assets\/img\/xrp.png"
    }
   
    
    


def getDashcoinPrice(crypto_dash):
    URL = 'https://www.dashcentral.org/api/v1/public'
    try:
        r = requests.get(URL)
        priceFloat = json.loads(r.text)
        #ans = json.loads(priceFloat)
        # print(priceFloat)
        data = (priceFloat['exchange_rates'])
    except requests.ConnectionError:
        print("Error querying Bitstamp API")
    return data['dash_usd']
# print('Dash:',getDashcoinPrice(crypto_dash))


def main_dash():
    last_price = -1

    while True:

        crypto_dash = 'dash'
        price = getDashcoinPrice(crypto_dash)

        if price != last_price:
            #print('Dashcoin price: ',price)
            last_price = price
    return
# print(main_xlmusd())


@router.get('/api/v1/dash',tags=["Coin_Price"])
async def index_dash(background_tasks: BackgroundTasks):
    background_tasks.add_task(main_dash)
    return {
        "coin": "dash",
        "name": "Dash",
        "rate": float(getDashcoinPrice("crypto_dash")),
        "coin_logo": "assets\/img\/dash.png"
    }
    
    
@router.get('/api/v1/btcusdt',tags=["Coin_Price"])
def getbnbusdtprice(Binance_Coin):
    base_url = "https://api.binance.com"
    path = "/api/v3/ticker/price"
    params = '?symbol=BNBUSDT'
    try:
        r = requests.get(base_url+path+params)
        data = r.json()
        priceFloat = float(data['price'])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")  

@router.get('/api/v1/tronusdt',tags=["Coin_Price"])
def gettrxusdtprice(tron_Coin):
    base_url = "https://api.binance.com"
    path = "/api/v3/ticker/price"
    params = '?symbol=TRXUSDT'
    try:
        r = requests.get(base_url+path+params)
        data = r.json()
        priceFloat = float(data['price'])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")  



@router.get('/api/v1/bnbusdt',tags=["Coin_Price"])
def binance_BNBUSDT():
    base_url = "https://api.binance.com"
    path = "/api/v3/ticker/price"
    params = '?symbol=BNBUSDT'
    r = requests.get(base_url+path+params)
    data = r.json()
    return {
        "coin": "BNB",
        "name": "Binance Coin",
        "rate_usdt": float(data['price']),
        "coin_logo": "assets\/img\/bnb.png"
    }


@router.get('/api/v1/trxusdt',tags=["Coin_Price"])
def binance_TRXUSDT():
    base_url = "https://api.binance.com"
    path = "/api/v3/ticker/price"
    params = '?symbol=TRXUSDT'
    r = requests.get(base_url+path+params)
    data = r.json()
    return {
        "coin": "TRX",
        "name": "TRON Coin",
        "rate_usdt": float(data['price']),
        "coin_logo": "assets\/img\/trx.png"
    }
    
    
@router.get('/api/v1/btcusdt',tags=["Coin_Price"])
def binance_BTCUSDT():
    base_url = "https://api.binance.com"
    path = "/api/v3/ticker/price"
    params = '?symbol=BTCUSDT'
    r = requests.get(base_url+path+params)
    data = r.json()
    return {
        "coin": "BTC",
        "name": "Bitcoin",
        "rate_usdt": float(data['price']),
        "coin_logo": "assets\/img\/btcusdt.png"
    }  
    
    
@router.get("/api/v1/all_coin_binance",tags=["Coin_Price"])
def all_coin():
    PATH = '/api/v3/ticker/price'
    base_url = "https://api.binance.com"
    params = {
        'symbol': 'BTCUSDT'
    }

   #url = urljoin(base_url, PATH)
    r = requests.get(base_url+ PATH)
    if r.status_code == 200:
        data = r.json()
        json_formatted_str = json.dumps(data, indent=4)
    else:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Not a valid eth wallet check the wallet and try again")
    return{"coins" : json_formatted_str}




listData = [
    {
        "coin": "btc",
        "name": "Bitcoin",
        "rate": get_price("bitcoin"),
        "coin_logo": "assets\/img\/btc.png"
    },
    {
        "coin": "bch",
        "name": "Bitcoin Cash",
        "rate": get_price_bch("bitcoin_cash"),
        "coin_logo": "assets\/img\/bch.png"
    },
    {
        "coin": "ltc",
        "name": "Litecoin",
        "rate": getLtccoinPrice('litercoin'),
        "coin_logo": "assets\/img\/ltc.png"
    },
    {
        "coin": "xrp",
        "name": "Ripple",
        "rate": getxrpusprice("Ripple"),
        "coin_logo": "assets\/img\/xrp.png"
    },
    {
        "coin": "dash",
        "name": "dash",
        "rate": getDashcoinPrice("crypto_dash"),
        "coin_logo": "assets\/img\/dash.png"
    },
    {
        "coin": "xlm",
        "name": "Stellar",
        "rate": getXlmucoinPrice("stellar"),
        "coin_logo": "assets\/img\/xlm.png"
    },
    {
        "coin": "ether",
        "name": "Ethereum",
        "rate": getethercoinPrice("ether"),
        "coin_logo": "assets\/img\/ether.png"
    },
    {
        "coin": "BNB",
        "name": "Binance Coin",
        "rate": getbnbusdtprice("Binance_Coin"),
        "coin_logo": "assets\/img\/bnb.png"
    
    },
    {
        "coin": "TXR",
        "name": "TRON Coin",
        "rate": gettrxusdtprice("tron_Coin"),
        "coin_logo": "assets\/img\/txr.png"
    
    }
]

