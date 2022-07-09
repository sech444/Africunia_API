from binance import ThreadedWebsocketManager, ThreadedDepthCacheManager
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv
import os
from binance.client import Client
import time
from binance.enums import *




load_dotenv()

API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
BASE_URL = 'https://api.binance.com'


headers = {
    'X-MBX-APIKEY': API_KEY
}


client = Client(API_key, Secret_Key)

print("logged in")


balance = client.get_asset_balance(asset='usdt')

print(balance)
"""
withdraws = client.get_withdraw_history(coin='usdt')

for i in withdraws:
    print(i)"""
prices =  client.get_avg_price(symbol='BNBUSDT')

info = client.get_symbol_info('BNBUSDT')
print(info['filters'][2]['minQty'])

print(".....................")

"""print("...loading ....")
info_ = client.get_margin_account()

for i in info_:
    print(i)
    

from binance.exceptions import BinanceAPIException
try:
    # name parameter will be set to the asset value by the client if not passed
    result = client.withdraw(
        coin='ETH',
        address='<eth_address>',
        amount=1)
except BinanceAPIException as e:
    print(e)
else:
    print("Success")
    
balance = client.get_asset_balance(asset='gnox')

print(balance)

print("making order.....")
order = client.order_market_buy(
    symbol='BNBUSDT',
    quantity=0.05)

order = client.create_order(
    symbol='BNBUSDT',
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=0.0461,
    price=10)"""

#print(order)

from decimal import Decimal as D, ROUND_DOWN, ROUND_UP
import decimal
order = client.get_order(
    symbol='BNBUSDT',
    orderId=4136872022)
print(order)
print("..................new line.................")
pair = 'BNBUSDT'
info = client.get_symbol_info(symbol=pair)
print(info)
print("..................new line.................")
price_filter = float(info['filters'][0]['tickSize'])
print(price_filter)
print("..................new line.................")
ticker = client.get_symbol_ticker(symbol=pair)
print(ticker)
print("..................new line.................")
price = float(ticker['price'])
print(price)
print("..................new line.................")
price_ = D.from_float(price).quantize(D(str(price_filter)))
print(price_)
print("..................new line.................")
minimum = float(info['filters'][2]['minQty']) # 'minQty'
print(minimum)
print("..................new line.................")
quant = D.from_float(0.002).quantize(D(str(minimum))) # if quantity >= 10.3/price
print(quant)
