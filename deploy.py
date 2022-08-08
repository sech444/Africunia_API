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
print(json.dumps(result["account_data"], indent=4, sort_keys=True))'''


from tronpy import Tron
from tronpy.exceptions import AddressNotFound
from pprint import pprint

client = Tron()

import requests
import base58
import base64
from pprint import pprint


ADDRESS = "TRRNL6w3Fm5rSpxYa5577FuP5HSJT8NoK8"
PRIV_KEY = '0x6dbefdb03ee56b3d14f0a3114f041519d25a9948cba2525d9f4e925d4a6a6c80' # for testing

CONTRACT = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"  # USDT
CONTRACT = "T,,,,,,,,,,,,,,,,,,,,,,ia"

API_URL_BASE = 'https://api.trongrid.io/'
# API_URL_BASE = 'https://api.shasta.trongrid.io/'
# API_URL_BASE = 'https://api.nileex.io/'

# 70a08231: balanceOf(address)
METHOD_BALANCE_OF = 'balanceOf(address)'

# a9059cbb: transfer(address,uint256)
METHOD_TRANSFER = 'transfer(address,uint256)'


DEFAULT_FEE_LIMIT = 1_000_000  # 1 TRX


def address_to_parameter(addr):
    return "0" * 24 + base58.b58decode_check(addr)[1:].hex()


def amount_to_parameter(amount):
    return '%064x' % amount


def get_balance(address=ADDRESS):
    url = API_URL_BASE + 'wallet/triggerconstantcontract'
    payload = {
        'owner_address': base58.b58decode_check(ADDRESS).hex(),
        'contract_address': base58.b58decode_check(CONTRACT).hex(),
        'function_selector': METHOD_BALANCE_OF,
        'parameter': address_to_parameter(address),
    }
    resp = requests.post(url, json=payload)
    data = resp.json()

    if data['result'].get('result', None):
        print(data['constant_result'])
        val = data['constant_result'][0]
        print('balance =', int(val, 16))
    else:
        print('error:', bytes.fromhex(data['result']['message']).decode())


def get_trc20_transaction(to, amount, memo=''):
    url = API_URL_BASE + 'wallet/triggersmartcontract'
    payload = {
        'owner_address': base58.b58decode_check(ADDRESS).hex(),
        'contract_address': base58.b58decode_check(CONTRACT).hex(),
        'function_selector': METHOD_TRANSFER,
        'parameter': address_to_parameter(to) + amount_to_parameter(amount),
        "fee_limit": DEFAULT_FEE_LIMIT,
        'extra_data': base64.b64encode(memo.encode()).decode(),  # TODO: not supported yet
    }
    resp = requests.post(url, json=payload)
    data = resp.json()

    if data['result'].get('result', None):
        transaction = data['transaction']
        return transaction

    else:
        print('error:', bytes.fromhex(data['result']['message']).decode())
        raise RuntimeError


def sign_transaction(transaction, private_key=PRIV_KEY):
    url = API_URL_BASE + 'wallet/addtransactionsign'
    payload = {'transaction': transaction, 'privateKey': private_key}
    resp = requests.post(url, json=payload)

    data = resp.json()

    if 'Error' in data:
        print('error:', data)
        raise RuntimeError
    return data


def broadcast_transaction(transaction):
    url = API_URL_BASE + 'wallet/broadcasttransaction'
    resp = requests.post(url, json=transaction)

    data = resp.json()
    print(data)


def transfer(to, amount, memo=''):
    transaction = get_trc20_transaction(to, amount, memo)
    pprint(transaction)
    transaction = sign_transaction(transaction)
    broadcast_transaction(transaction)


get_balance()

#transfer('T..............q', 5_000, 'test from python')

def check_balance(address):
    try:
        balance=client.get_account_balance(address)
        return balance
    except AddressNotFound:
        return 'Adress not found..!'


print(check_balance(ADDRESS))


