'''from random import seed
from ripple_api import RippleDataAPIClient
from pprint import pprint

api = RippleDataAPIClient('https://data.ripple.com')
# to get name of a specific transaction type please refer to this link:
# https://developers.ripple.com/transaction-types.html
query_params = dict(type="Payment")
txs = api.get_transactions(**query_params)
#pprint(txs)


acct_info = api(
    account="rBtXmAdEYcno9LWRnAGfT9qBxCeDvuVRZo",
    ledger_index="current",
    queue=True,
    strict=True,
)
response = api.request(acct_info)
result = response.result
import json
print(json.dumps(result["account_data"], indent=4, sort_keys=True))

'''
from cmath import e
from web3 import Web3, EthereumTesterProvider,HTTPProvider
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/bde4e3babba54474844b65de59d0a039'))
import json
usdt = '0xdAC17F958D2ee523a2206206994597C13D831ec7' 
usdt_test = '0xbA6879d0Df4b09fC678Ca065c00dd345AdF0365e'

with open("usdt_abi.json", "r") as file:
    usdt_erc20 = file.read()
    
#value_to = input('value_to_send')
#wallet_id = input("addr from: ")  
#addr_id = input("addr to: ")  
'''adr_verify = Web3.isAddress(wallet_id)
if not adr_verify:
    raise e '''
usdt_abi= w3.eth.contract(abi=usdt_erc20, address=usdt_test)
_name = usdt_abi.functions.name().call()
_symbol = usdt_abi.functions.symbol().call()

print(_name) 
print(_symbol)
#return {"total": total}
