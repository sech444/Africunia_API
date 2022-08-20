from ast import Try
from cmath import e
from fastapi import FastAPI, WebSocket, BackgroundTasks, APIRouter, Depends, status, HTTPException, Form
import json
from typing import List, Optional
import requests
import binance
from web3 import Web3
from coinpaprika import client as Coinpaprika
from bs4 import BeautifulSoup as BS


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
    

def get_ether_coin_Price(crypto_ether):
    URL = 'https://www.bitstamp.net/api/v2/ticker/ethusd/'#usdtusd
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
        price = get_ether_coin_Price(crypto_ether)

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
        "rate": get_ether_coin_Price("ether"),
        "coin_logo": "assets\/img\/ether.png"
    }



def get_usdt_coin_Price(crypto_ether):
    URL = 'https://www.bitstamp.net/api/v2/ticker/usdtusd/'#usdtusd
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print("Error querying Bitstamp API")


def main_usdt():
    last_price = -1

    while True:

        crypto_ether = 'usdtusd'
        price = get_usdt_coin_Price(crypto_ether)

        if price != last_price:
           # print('Bitcoin price: ',price)
            last_price = price
    return


@router.get('/api/v1/usdtusd',tags=["Coin_Price"])
async def index_usdt(background_tasks: BackgroundTasks):
    background_tasks.add_task(main_ether)
    return {
        "coin": "usdt",
        "name": "Tether",
        "rate": get_usdt_coin_Price("usdtusd"),
        "coin_logo": "assets\/img\/usdt.png"
    }




def get_xlmu_Price(crypto_xlmusd):
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
        price = get_xlmu_Price(crypto_xlmusd)

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
        "rate": get_xlmu_Price("stellar"),
        "coin_logo": "assets\/img\/xlm.png"
        }
    

def get_Ltccoin_Price(crypto_ltc):
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
        price = get_Ltccoin_Price(crypto_ltc)

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
        "rate": get_Ltccoin_Price('litercoin'),
        "coin_logo": "assets\/img\/ltc.png"
    }
    

def get_xrp_price(crypto_xrpusd):
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
        price = get_xrp_price(crypto_xrpusd)
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
        "rate": get_xrp_price("Ripple"),
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
    
    
@router.get('/api/v1/bnb_usdt',tags=["Coin_Price"])
def bnb_usdt():
    base_url = "https://api.binance.com"
    path ="/api/v3/ticker/price"
    params = '?symbol=BNBUSDT'
    try:
        r = requests.get(base_url+path+params)
        data = r.json()
        priceFloat = float(data['price'])
        #print(priceFloat)
        #return priceFloat
        return {
        "coin": "BNB",
        "name": "Binance Coin",
        "rate": priceFloat,
        "coin_logo": "assets\/img\/bnb.png"
    }
    except requests.ConnectionError:
        print("Error querying Bitstamp API")  
   

@router.get('/api/v1/trx_usdt',tags=["Coin_Price"])
def trx_usdt():
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
    
    
@router.get('/api/v1/busd',tags=["Coin_Price"])
def trx_usdt():
    base_url = "https://api.binance.com"
    path = "/api/v3/ticker/price"
    params = '?symbol=BUSDUSDT'
    r = requests.get(base_url+path+params)
    data = r.json()
    return {
        "coin": "BUSD",
        "name": "Binance USD",
        "rate_usdt": float(data['price']),
        "coin_logo": "assets\/img\/busd.png"}
    
    
    
@router.get('/api/v1/btcusdt',tags=["Coin_Price"])
def binance_btcusdt():
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


@router.get("/api/v1/all_afcash",tags=["Coin_Price"])
def AFCASH_coin():
    try:
        client = Coinpaprika.Client()
        pair_list = client.ticker('afcash-africunia-bank')
        quotes = pair_list['quotes']['USD']['price']
        return{"rate": quotes }
    except:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"price updating soon")
    return{"coins" : json_formatted_str}



@router.get("/api/v1/exl_price",tags=["Coin_Price"])
# method to get the price of bit coin
def exl_price():
  # getting the request from url 
    import re
    data = requests.get(url,headers=headers) 
    # converting the text 
    soup = BS(data.text, 'html.parser')
    
    # finding metha info for the current price
    ans = soup.find('span', {"class" :"price"}).text
    listans = [float(s) for s in re.findall(r'[\d]*[.][\d]+', ans)]
    #print(float(listans[0]))
    return{
        "coin": "EXL",
        "name": "Excoincial",
        "rate" : float(listans[0]),
        "coin_logo": "assets\\/img\\/exl.png"
        }
   
# url of the exl coin price

url = "https://www.livecoinwatch.com/price/Excoincial-EXL"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}

def exl_price2():
    try:
    # getting the request from url 
        import re
        data = requests.get(url,headers=headers) 
        # converting the text 
        soup = BS(data.text, 'html.parser')
        
    
        # finding metha info for the current price
        ans = soup.find('div', {"class" :"cion-item text-center text-lg-left second-row-col"}).text
        listans = [float(s) for s in re.findall(r'[\d]*[.][\d]+', ans)]
        #print(float(listans[0]))
        return float(listans[0])
    except:
        return  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"price update soon")


def main_dash2():
    try:
        client = Coinpaprika.Client()
        pair_list = client.ticker('afcash-africunia-bank')
        quotes = pair_list['quotes']['USD']['price']
        
        return quotes
    except:
        return  HTTPException(status_code = 404, detail=  "Id not found")


try:
    base_url = "https://api.binance.com"
    path ="/api/v3/ticker/price"
    params = '?symbol=BNBUSDT'
    r = requests.get(base_url+path+params)
    data = r.json()
    priceFloat = float(data['price'])
    #print(priceFloat)
except:
    raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"price update soon")
    

try:
    base_url = "https://api.binance.com"
    path ="/api/v3/ticker/price"
    params = '?symbol=TRXUSDT'
    r = requests.get(base_url+path+params)
    data = r.json()
    priceFloat2 = float(data['price'])
    #print(priceFloat2)
except:
    raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"price update soon")
    
try:
    base_url = "https://api.binance.com"
    path ="/api/v3/ticker/price"
    params = '?symbol=BUSDUSDT'
    r = requests.get(base_url+path+params)
    data = r.json()
    priceFloat12 = float(data['price'])
    #print(priceFloat2)
except:
    raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"price update soon")

listData = [
    {
        "coin": "btc",
        "name": "Bitcoin",
        "rate": get_price("bitcoin"),
        "coin_logo": "assets/img/btc.png"
    },
    {
        "coin": "bch",
        "name": "Bitcoin Cash",
        "rate": get_price_bch("bitcoin_cash"),
        "coin_logo": "assets/img/bch.png"
    },
    {
        "coin": "ltc",
        "name": "Litecoin",
        "rate": get_Ltccoin_Price('litercoin'),
        "coin_logo": "assets/img/ltc.png"
    },
    {
        "coin": "xrp",
        "name": "Ripple",
        "rate": get_xrp_price("Ripple"),
        "coin_logo": "assets/img/xrp.png"
    },
    {
        "coin": "dash",
        "name": "dash",
        "rate": getDashcoinPrice("crypto_dash"),
        "coin_logo": "assets/img/dash.png"
    },
    {
        "coin": "xlm",
        "name": "Stellar",
        "rate": get_xlmu_Price("stellar"),
        "coin_logo": "assets/img/xlm.png"
    },
    {
        "coin": "ether",
        "name": "Ethereum",
        "rate": get_ether_coin_Price("ether"),
        "coin_logo": "assets/img/ether.png"
    },
     {
        "coin": "BNB",
        "name": "Binance Coin",
        "rate": priceFloat,
        "coin_logo": "assets/img/bnb.png"
    },
    {
        "coin": "TRX",
        "name": "TRON Coin",
        "rate": priceFloat2,
        "coin_logo": "assets\\/img\\/trx.png"
    },
    {
        "coin": "BUSD",
        "name": "Binance USD",
        "rate": priceFloat12,
        "coin_logo": "assets\\/img\\/busd.png"
    },
     {
        "coin": "AFCASH",
        "name": "AFCASH (EXL20)",
        "rate": main_dash2(),
        "coin_logo": "assets\\/img\\/afcash.png"
    },
     {
        "coin": "EXL",
        "name": "Excoincial",
        "rate": exl_price2(),
        "coin_logo": "assets\\/img\\/exl.png"
    },
     {
        "coin": "usdt",
        "name": "Tether",
        "rate": get_usdt_coin_Price("usdtusd"),
        "coin_logo": "assets\/img\/usdt.png"
    }

]



def exl_afcash():
        
    afcash = "0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b"

    #print(tokens)
    exl_url = "https://rpc.exlscan.com/"
    w3 = Web3(Web3.HTTPProvider(exl_url))

    with open("pancake.json", "r") as file:
        swap_Afcash_file = file.read()
        #print(swap_Afcash_file)
    # Closing file

    AfcashSwap = w3.eth.contract(abi=swap_Afcash_file, address=afcash)

    EXL = AfcashSwap.functions.totalSupply().call()

    #print(EXL)
    total = w3.fromWei(EXL, 'ether')

    #print( total) 
    return total 
    
    



def TRC20_afcash():
        
    er20_afcash = "TR26H88jy3zhcLgUw5RxM4BAPozCoiWqHM"
    #afcash_addr = Web3.isAddress(afcash)
    #print(tokens)
    #w3 = Web3(Web3.HTTPProvider('https://api.trongrid.io https://apilist.tronscan.org/api/contracts/code?contract= er20_afcash'))

    base_url = "https://apilist.tronscan.org/api/account?address=TR26H88jy3zhcLgUw5RxM4BAPozCoiWqHM"#" https://apilist.tronscan.org/api/contract?contract=TR26H88jy3zhcLgUw5RxM4BAPozCoiWqHM"
    url = r.get(base_url)
    data = url.json()
    #print(data)
    with open("TRC20_ABI.json", "r") as file:
        swap_Afcash = file.read()
        #print(swap_Afcash_file)
    # Closing file
    
    import requests

    url = "https://api.shasta.trongrid.io/v1/contracts/{TR26H88jy3zhcLgUw5RxM4BAPozCoiWqHM}/tokens"

    headers = {
        'Content-Type': "application/json",
        'TRON-PRO-API-KEY': "148ccca9-c9e0-4493-ad4a-8fe1476a5207"
        }
    response = requests.get( url, headers=headers)
    #print(response.text)


    #AfcashS = w3.eth.contract(address= er20_afcash, abi=swap_Afcash,)
    #res = w3.isConnected()
    #print(res)
   # EXL = AfcashS.functions.totalSupply().call()

    #print(EXL)
    #total = w3.fromWei(EXL, 'ether')

    #print('TRC20 ', total)
    
#TRC20_afcash()

def bep20_afcash():
        
    afcash = "0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b"

    #print(tokens)
    exl_url = "https://bsc-dataseed.binance.org/"
    w3 = Web3(Web3.HTTPProvider(exl_url))

    with open("erc20afcash.json", "r") as file:
        swap_Afcash_file = file.read()
        #print(swap_Afcash_file)
    # Closing file

    AfcashSwap = w3.eth.contract(abi=swap_Afcash_file, address=afcash)

    EXL = AfcashSwap.functions.totalSupply().call()

    #print(EXL)
    total = w3.fromWei(EXL, 'ether')

    #print(total)  
    return total


def er20_afcash():
        
    afcash = "0xb8a5dBa52FE8A0Dd737Bf15ea5043CEA30c7e30B"

    #print(tokens)
    exl_url = "https://mainnet.infura.io/v3/bde4e3babba54474844b65de59d0a039"
    w3 = Web3(Web3.HTTPProvider(exl_url))

    with open("erc20afcash.json", "r") as file:
        swap_Afcash_file = file.read()
        #print(swap_Afcash_file)
    # Closing file

    AfcashSwap = w3.eth.contract(abi=swap_Afcash_file, address=afcash)

    EXL = AfcashSwap.functions.totalSupply().call()

    #print(EXL)
    total = w3.fromWei(EXL, 'ether')

    #print(total)  
    return total

@router.get('/api/v1/total_coins',tags=["Coin_Price"])
def total_coins():

    TRC20 = exl_afcash()
    EXL20 = exl_afcash()
    BEP20 = bep20_afcash()
    ERC20 = er20_afcash()
    total = ERC20 + BEP20 + BEP20 + TRC20
    return{
        "TRC20": TRC20,
        "EXL20" : EXL20,
        "BEP20" : BEP20,
        "ERC20" : ERC20,
        "total" : total
    }



