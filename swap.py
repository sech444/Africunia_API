import requests
from bs4 import BeautifulSoup as BS
from fastapi import (APIRouter, BackgroundTasks, Depends, FastAPI, Form,
                     HTTPException, WebSocket, status)
from requests.adapters import HTTPAdapter
from stellar_sdk import Asset, Keypair, Network, Server, TransactionBuilder
from stellar_sdk.exceptions import (BadRequestError, BadResponseError,
                                    NotFoundError)
from web3 import Web3

# from requests.packages.urllib3.util.retry import Retry
# w3 = Web3(Web3.HTTPProvider('https://rpc.exlscan.com/'))


# router = APIRouter()

# contract_addr ='0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b'
# dbAddress = w3.toChecksumAddress(contract_addr).lower()
# #print(dbAddress )
# with open("pancake.json", "r") as file:
#     Compiled_code = file.read()
#     #print(Compiled_code)

# Afcash = w3.eth.contract(address= contract_addr, abi=Compiled_code)

# print(Afcash.functions.name().call())

"""alice = input('addr to reciver: ')#'0x9875adb3f2ab35cb2328c9974292e5711eced73b' 0xB1E6c654Cd79265865b07611CAB04E80d245e92e
Address = w3.toChecksumAddress(alice)
bals = Afcash.functions.balanceOf(Address).call()
#bals2 = w3.eth.get_balance(Address)
bals_ = w3.fromWei(bals, 'ether'),
#print(bals2)
print(bals_)"""


"""acct_from = input("acct_from: ")
value_to_send = input("value: ")
my_private_key = input("private_key: ")
tx_hash = Afcash.functions.transferFrom(acct_from, alice, value_to_send).call()
"""

# 2. Sign a transaction


# working with Contract, you need :
# Contract Address
# Contarct ABI
# AfcashSwap = w3.eth.contract(address=tx_receipt.contractAddress, abi = abi)

# Intitial value of favorite number

"""
send_transaction = Afcash.functions.store(15).buildTransaction(
    {
    "gasPrice": w3.eth.gas_price, 
    "chainId": chain_id, 
    "from": my_address, 
    "nonce": nonce + 1,
    }
)

signed_store_tx = w3.eth.account.signTransaction(store_transaction, my_private_key)
store_tx_hash =  w3.eth.send_raw_transaction(signed_store_tx.rawTransaction)
store_tx_receipt = w3.eth.wait_for_transaction_receipt(store_tx_hash)
print(store_tx_receipt)
new_data2 = (w3.toHex(store_tx_hash))
print(new_data2 )

#this program queries for all of the uniswap pair addresses and their token supply

infura_url = 'https://rinkeby.infura.io/v3/bde4e3babba54474844b65de59d0a039'

web3 = Web3(Web3.HTTPProvider(infura_url))

# uniswap_Factory
factory_abi = json.loads('[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
factory_address = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f'
factory_contract = web3.eth.contract(address=factory_address, abi=factory_abi)


#returns a count of all the trading pairs on uniswap
allPairsLength = factory_contract.functions.allPairsLength().call()
#print(allPairsLength)


for i in range(1, 58494):
    allPairs_address = factory_contract.functions.allPairs(i).call()
    contract = web3.eth.contract(address=allPairs_address, abi=factory_abi)
    symbol = contract.functions.name().call()
    supply = contract.functions.totalSupply().call()
    print(allPairs_address, supply)


Account.enable_unaudited_hdwallet_features()
acct, mnemonic = Account.create_with_mnemonic()

print(acct.address, Web3.toJSON(acct.privateKey))
print(mnemonic)
#print(Web3.toJSON(acct.privateKey))
private_key = Web3.toJSON(acct.privateKey)
print(private_key)

print(Account.from_mnemonic(mnemonic))

account = Account.privateKeyToAccount(private_key[3:-1])
print(account)


account = Account.from_key(private_key)

print(account.address)
# get private key
print(account.privateKey)

# get address
print(account.address)
print(account.privateKey.hex())
"""


from stellar_sdk import Asset, Keypair, Network, Server, TransactionBuilder
from stellar_sdk.exceptions import (BadRequestError, BadResponseError,
                                    NotFoundError)

server = Server(horizon_url="https://horizon-testnet.stellar.org")
source_key = Keypair.from_secret(
    "8efaf003942ea6d0abacf5113a8d8c014d72942c62da1bff2a42662b70220d41"
)
destination_id = "GAHK7EEG2WWHVKDNT4CEQFZGKF2LGDSW2IVM4S5DP42RBW3K6BTODB4A"

# First, check to make sure that the destination account exists.
# You could skip this, but if the account does not exist, you will be charged
# the transaction fee when the transaction fails.
try:
    server.load_account(destination_id)
except NotFoundError:
    # If the account is not found, surface an error message for logging.
    raise Exception("The destination account does not exist!")
print("geting public_key")
# If there was no error, load up-to-date information on your account.
source_account = server.load_account(source_key.public_key)

# Let's fetch base_fee from network
base_fee = server.fetch_base_fee()
print("Start building the transaction")
# Start building the transaction.
transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
    # Because Stellar allows transaction in many currencies, you must specify the asset type.
    # Here we are sending Lumens.
    .append_payment_op(destination=destination_id, asset=Asset.native(), amount="10")
    # A memo allows you to add your own metadata to a transaction. It's
    # optional and does not affect how Stellar treats the transaction.
    .add_text_memo("Test Transaction")
    # Wait a maximum of three minutes for the transaction
    .set_timeout(10).build()
)
print("Sign the transaction to prove you are actually the person sending it.")
# Sign the transaction to prove you are actually the person sending it.
transaction.sign(source_key)

try:
    # And finally, send it off to Stellar!
    response = server.submit_transaction(transaction)
    print(f"Response: {response}")
except (BadRequestError, BadResponseError) as err:
    print(f"Something went wrong!\n{err}")
