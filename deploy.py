import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
import pandas as pd

config_logging(logging, logging.DEBUG)

key = “your key”
secret = “your secret key”

logging.info(spot_client.withdraw(coin=“BNB”, amount=0.01, address=""))

so if we do this, will it work:
logging.info(spot_client.withdraw(coin=“USDT”, amount=0.01, address="", network=“TRON”))

please confirm

thanks
Sukhwant