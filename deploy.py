from email.headerregistry import Address
from importlib.machinery import DEBUG_BYTECODE_SUFFIXES
import json
from lib2to3.pygram import Symbols
from locale import D_FMT
from multiprocessing.sharedctypes import Value
from operator import index
from os import uname
from solcx import compile_standard, install_solc
from web3 import Web3
from collections import OrderedDict
import time
from decimal import Decimal
import pandas as pd
from pythonpancakes import PancakeSwapAPI
import csv
#import itertools
import requests as r
ps = PancakeSwapAPI()


""""

#print(json.dumps(data, indent=4))
#print(data2["symbol"])    
    #print(name)

#with open("./contracts/AfcashSwap.sol", "r") as file:
    #swap_Afcash_file = file.read()
    #print(swap_Afcash_file)

# Compile Our Solidity
install_solc("0.6.6")
compiled_sol = compile_standard(
    {"language": "Solidity",
     "sources": {"AfcashSwap.sol": {"content": swap_Afcash_file}},
     "settings": {
         "outputSelection": {
             "*": {"*": ["abi", "metadata", "evm.byecode", "evm.bytecode.sourceMap"]}
         }
     },
     },
    solc_version="0.6.6",
)

# print(compiled_sol)
# get bytecode76]
    coin_addr79 = df[0][77]
    coin_addr80 = df[0][78]
    coin_addr81 = df[0][79]
    coin_addr82 = df[0][80]
    coin_addr83 = df[0][81]
    coin_addr84 = df[0][82]
    coin_addr85 = df[0][83]
    coin_addr86 = df[0][84]
    coin_addr87 = df[0][85]
    coin_addr88 = df[0][86]
    coin_addr89 = df[0][87]
    coin_addr90 = df[0][89]
    coin_addr91= df[0][90]




#print(df[0][0])
class Coin_symbol(str, Enum):
    coin_smbol00 = "AFCASH"
    coin_smbol0 = df[1][0]['symbol']
    coin_smbol1 = df[1][1]['symbol']
    coin_smbol2 = df[1][2]['symbol']
    coin_smbol3 = df[1][3]['symbol']
    coin_smbol4 = df[1][4]['symbol']
    coin_smbol5 = df[1][5]['symbol']
    coin_smbol6 = df[1][6]['symbol']
    coin_smbol7 = df[1][7]['symbol']
    coin_smbol8 = df[1][8]['symbol']
    coin_smbol9 = df[1][9]['symbol']
    coin_smbol10 = df[1][10]['symbol']
    coin_smbol11 = df[1][11]['symbol']
    coin_smbol12 = df[1][12]['symbol']
    coin_smbol13 = df[1][13]['symbol']
    coin_smbol14 = df[1][14]['symbol']
    coin_smbol15 = df[1][15]['symbol']
    coin_smbol16 = df[1][16]['symbol']
    coin_smbol17 = df[1][17]['symbol']
    coin_smbol18 = df[1][18]['symbol']
    coin_smbol19 = df[1][19]['symbol']
    coin_smbol20 = df[1][20]['symbol']
    coin_smbol21 = df[1][21]['symbol']
    coin_smbol22 = df[1][22]['symbol']
    coin_smbol23 = df[1][23]['symbol']
    coin_smbol24 = df[1][24]['symbol']
    coin_smbol25 = df[1][25]['symbol']
    coin_smbol26 = df[1][26]['symbol']
    coin_smbol27 = df[1][27]['symbol']
    coin_smbol28 = df[1][28]['symbol']
    coin_smbol29 = df[1][29]['symbol']
    coin_smbol30 = df[1][30]['symbol']
    coin_smbol31 = df[1][31]['symbol']
    coin_smbol32 = df[1][32]['symbol']
    coin_smbol33 = df[1][33]['symbol']
    coin_smbol34 = df[1][34]['symbol']
    coin_smbol35 = df[1][35]['symbol']
    coin_smbol36 = df[1][36]['symbol']
    coin_smbol37 = df[1][37]['symbol']
    coin_smbol38 = df[1][38]['symbol']
    coin_smbol39 = df[1][39]['symbol']
    coin_smbol40 = df[1][40]['symbol']
    coin_smbol41 = df[1][41]['symbol']
    coin_smbol42 = df[1][42]['symbol']
    coin_smbol43 = df[1][43]['symbol']
    coin_smbol44 = df[1][44]['symbol']
    coin_smbol45 = df[1][45]['symbol']
    coin_smbol46 = df[1][46]['symbol']
    coin_smbol47 = df[1][47]['symbol']
    coin_smbol48 = df[1][48]['symbol']
    coin_smbol49 = df[1]
bytecode = compiled_sol["contracts"]["AfcashSwap.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

abi = compiled_sol["contracts"]["AfcashSwap.sol"]["SimpleStorage"]["abi"]
#print(abi)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

w3 = Web3(Web3.HTTPProvider("HTTP://0.0.0.0:7545"))
chain_id = 1337
my_address = "0x8f18A038d1177E8Eb6A5F5804a60101e1B910bac"
my_private_key = "0x2e72b9f6f4c507233d3f7cb1d18feaa35e704a8a1d16447cf514227954f2992c"

# Create the contract in python 
AfcashSwap = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get the latestest transaction
nonce = w3.eth.getTransactionCount(my_address)
print(nonce)
print(nonce)

# 1. Build a transaction


transaction = AfcashSwap.constructor().buildTransaction( {
    "gasPrice": w3.eth.gas_price, 
    "chainId": chain_id, 
    "from": my_address, 
    "nonce": nonce, 
})

# 2. Sign a transaction


signed_tx = w3.eth.account.signTransaction(transaction, my_private_key)

# 3. send a transaction
tx_hash =  w3.eth.send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(tx_receipt)
new_data = (w3.toHex(tx_hash))
print(new_data )


# working with Contract, you need :
# Contract Address
# Contarct ABI
AfcashSwap = w3.eth.contract(address=tx_receipt.contractAddress, abi = abi)

# Intitial value of favorite number
print(AfcashSwap.functions.retrieve().call())

store_transaction = AfcashSwap.functions.store(15).buildTransaction(
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

bsc = "https://bsc-dataseed.binance.org/"
bsc_w3 = Web3(Web3.HTTPProvider(bsc))


with open("./pancake.json", "r") as file:
    pancake_abi_file = file.read()
    #print(pancake_abi_file )

pancake_factory = "0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73"

contract_addr = bsc_w3.toChecksumAddress(
    "0x10ED43C718714eb63d5aA57B78B54704E256024E")

usdt_addr = "0x55d398326f99059fF775485246999027B3197955"

Pancake_abi = pancake_abi_file

Afcash_addr = bsc_w3.toChecksumAddress(
    "0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b")
wBNB_token = bsc_w3.toChecksumAddress(
    "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c")
#value = input(" Value: ")
# function balanceOf(address account) external view returns (uint256)
AfcashSwap = bsc_w3.eth.contract(address=wBNB_token, abi=Pancake_abi)


def Swap():
    sender_address = bsc_w3.toChecksumAddress(input("sender_address: "))
    value = input(" Value: ")
    my_private_key = input(" private_key")
    # AfcashSwap.functions.balanceOf(sender_address).call()
    balance = bsc_w3.eth.get_balance(sender_address)
    balance_2 = bsc_w3.toWei(balance, 'ether')
    print(balance_2)
    nonce = bsc_w3.eth.get_transaction_count(sender_address)
    start = time.time()
    tx_swap = AfcashSwap.functions.swapExactETHForTokens(
        0,
        [weth_token,
         Afcash_addr],
        sender_address,
        (int(time.time()) + 10000)
    ).buildTransaction(
        {
            "from": sender_address,
            'value': bsc_w3.toWei(value, 'ether'),
            "gas": 250000,
            "gasPrice": bsc_w3.toWei('5', 'gwei'),
            "nonce": nonce,
        }
    )
    signed_store_tx = bsc_w3.eth.account.signTransaction(
        tx_swap, my_private_key)
    store_tx_hash = bsc_w3.eth.send_raw_transaction(
        signed_store_tx.rawTransaction)
    store_tx_receipt = bsc_w3.eth.wait_for_transaction_receipt(store_tx_hash)
    print(store_tx_receipt)
    print("........................new...........")
    new_data2 = (bsc_w3.toHex(store_tx_hash))
    print(new_data2)with open("./contracts/AfcashSwap.sol", "r") as file:
    s#wap_Afcash_file = file.read()
    # print(swap_Afcash_file)

# Compile Our Solidity
install_solc("0.6.6")
compiled_sol = compile_standard(
    {"language": "Solidity",
     "sources": {"AfcashSwap.sol": {"content": swap_Afcash_file}},
     "settings": {
         "outputSelection": {
             "*": {"*": ["abi", "metadata", "evm.byecode", "evm.bytecode.sourceMap"]}
         }
     },
     },
    solc_version="0.6.6",
)

# print(compiled_sol)
# get bytecode
bytecode = compiled_sol["contracts"]["AfcashSwap.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

abi = compiled_sol["contracts"]["AfcashSwap.sol"]["SimpleStorage"]["abi"]
#print(abi)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

w3 = Web3(Web3.HTTPProvider("HTTP://0.0.0.0:7545"))
chain_id = 1337
my_address = "0x8f18A038d1177E8Eb6A5F5804a60101e1B910bac"
my_private_key = "0x2e72b9f6f4c507233d3f7cb1d18feaa35e704a8a1d16447cf514227954f2992c"

# Create the contract in python 
AfcashSwap = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get the latestest transaction
nonce = w3.eth.getTransactionCount(my_address)
print(nonce)
print(nonce)

# 1. Build a transaction


transaction = AfcashSwap.constructor().buildTransaction( {
    "gasPrice": w3.eth.gas_price, 
    "chainId": chain_id, 
    "from": my_address, 
    "nonce": nonce, 
})

# 2. Sign a transaction


signed_tx = w3.eth.account.signTransaction(transaction, my_private_key)

# 3. send a transaction
tx_hash =  w3.eth.send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(tx_receipt)
new_data = (w3.toHex(tx_hash))
print(new_data )


# working with Contract, you need :
# Contract Address
# Contarct ABI
AfcashSwap = w3.eth.contract(address=tx_receipt.contractAddress, abi = abi)

# Intitial value of favorite number
print(AfcashSwap.functions.retrieve().call())

store_transaction = AfcashSwap.functions.store(15).buildTransaction(
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

bsc = "https://bsc-dataseed.binance.org/"
bsc_w3 = Web3(Web3.HTTPProvider(bsc))


with open("./pancake.json", "r") as file:
    pancake_abi_file = file.read()
    #print(pancake_abi_file )

pancake_factory = "0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73"

contract_addr = bsc_w3.toChecksumAddress(
    "0x10ED43C718714eb63d5aA57B78B54704E256024E")

usdt_addr = "0x55d398326f99059fF775485246999027B3197955"

Pancake_abi = pancake_abi_file

Afcash_addr = bsc_w3.toChecksumAddress(
    "0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b")
wBNB_token = bsc_w3.toChecksumAddress(
    "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c")
#value = input(" Value: ")
# function balanceOf(address account) external view returns (uint256)
AfcashSwap = bsc_w3.eth.contract(address=wBNB_token, abi=Pancake_abi)

def Swap():
    sender_address = bsc_w3.toChecksumAddress(input("sender_address: "))
    value = input(" Value: ")
    my_private_key = input(" private_key")
    # AfcashSwap.functions.balanceOf(sender_address).call()
    balance = bsc_w3.eth.get_balance(sender_address)
    balance_2 = bsc_w3.toWei(balance, 'ether')
    print(balance_2)
    nonce = bsc_w3.eth.get_transaction_count(sender_address)
    start = time.time()
    tx_swap = AfcashSwap.functions.swapExactETHForTokens(
        0,
        [weth_token,
         Afcash_addr],
        sender_address,
        (int(time.time()) + 10000)
    ).buildTransaction(
        {
            "from": sender_address,
            'value': bsc_w3.toWei(value, 'ether'),
            "gas": 250000,
            "gasPrice": bsc_w3.toWei('5', 'gwei'),
            "nonce": nonce,
        }
    )
    signed_store_tx = bsc_w3.eth.account.signTransaction(
        tx_swap, my_private_key)
    store_tx_hash = bsc_w3.eth.send_raw_transaction(
        signed_store_tx.rawTransaction)
    store_tx_receipt = bsc_w3.eth.wait_for_transaction_receipt(store_tx_hash)
    print(store_tx_receipt)
    print("........................new...........")
    new_data2 = (bsc_w3.toHex(store_tx_hash))
    print(new_data2)


#Swap()


sender_address = bsc_w3.toChecksumAddress(input("sender_address: "))
balance = bsc_w3.eth.get_balance(sender_address)
balance_2 = bsc_w3.toWei(balance, 'ether')
print(balance_2)

input_quantity_wei = balance_2
out_2 = Web3.toWei(input_quantity_wei, 'ether')
swap_path = [Afcash_addr, weth_token]
out = AfcashSwap.functions.getAmountsOut(input_quantity_wei, swap_path).call()

# print(out)
# 0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b
# private_key: 7dbec09e214cab2b4f77636cd082c65f85442d0ea65a59c28aa177158c4fe0c0
#
sender_address: 0xC9A61631F31E2FAaE0f79328A8e30F582C0F6F7d

# 0x162fe933c42fc0521f6b5fe99927e05f1e38d930326f87a794c432a9af8754e4

function swapExactTokensForTokens(
  uint amountIn,
  uint amountOutMin,
  address[] calldata path,
  address to,
  uint deadline
) external returns (uint[] memory amounts);

receive = AfcashSwap.functions.getAmountsOut( [0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b, 0x55d398326f99059fF775485246999027B3197955], 20).call()
minReceived = receive[1] * (9/10)                                                       
receiveReadable = bsc_w3.fromWei(minReceived,'ether')                       
print("Minimum tokens to recieve:", str(receiveReadable))

def PancakeSwap():
    sender_address = "0xC9A61631F31E2FAaE0f79328A8e30F582C0F6F7d"
    #address = bsc_w3.toChecksumAddress(input("sender_address: "))
    value = input(" Value: ")
    my_private_key = input(" private_key")
    path = [Afcash_addr, usdt_addr]
    #AfcashSwap.functions.balanceOf(sender_address).call()
    balance = bsc_w3.eth.get_balance(sender_address)
    balance_2 = bsc_w3.toWei(balance, 'ether')
    print(balance_2)
    nonce = bsc_w3.eth.get_transaction_count(sender_address)
    start = time.time()
    tx_Swap = AfcashSwap.functions.swapExactTokensForTokens(0, 0,
        path,
        balance_2,
        int(time.time()) + 10000
    ).buildTransaction(
        {
            "from": balance,
            'value': bsc_w3.toWei(value, 'ether'),
            "gas": 250000,
            "gasPrice": bsc_w3.toWei('5', 'gwei'),
            "nonce": bsc_w3.eth.get_transaction_count(balance),
        }
    )
    signed_store_tx = bsc_w3.eth.account.signTransaction(
        tx_Swap, my_private_key)
    store_tx_hash = bsc_w3.eth.send_raw_transaction(
        signed_store_tx.rawTransaction)
    store_tx_receipt = bsc_w3.eth.wait_for_transaction_receipt(store_tx_hash)
    print(store_tx_receipt)
    print("........................new...........")
    new_data2 = (bsc_w3.toHex(store_tx_hash))
    print(new_data2)


PancakeSwap()



#Calculate minimum amount of tokens to receive

receive = contract.functions.getAmountsOut(amount, [tokenToSpend, tokenToBuy]).call()
minReceived = receive[1] * (9/10)                                                       
receiveReadable = web3.fromWei(minReceived,'ether')                       
print("Minimum tokens to recieve:", str(receiveReadable))

#Trade execution:

pancakeswap2_txn = contract.functions.swapExactTokensForTokens(minReceived, [tokenToSpend,tokenToBuy], sender_address, (int(time.time()) + 1000000)).buildTransaction({   
            'from': sender_address,
            'value': web3.toWei(amount,'ether'), 
            'gasPrice': web3.toWei('5','gwei'),
            'nonce': nonce,
            })
            
            
with open("./contracts/AfcashSwap.sol", "r") as file:
    swap_Afcash_file = file.read()
    # print(swap_Afcash_file)

# Compile Our Solidity
install_solc("0.6.6")
compiled_sol = compile_standard(
    {"language": "Solidity",
     "sources": {"AfcashSwap.sol": {"content": swap_Afcash_file}},
     "settings": {
         "outputSelection": {
             "*": {"*": ["abi", "metadata", "evm.byecode", "evm.bytecode.sourceMap"]}
         }
     },
     },
    solc_version="0.6.6",
)

# print(compiled_sol)
# get bytecode
bytecode = compiled_sol["contracts"]["AfcashSwap.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

abi = compiled_sol["contracts"]["AfcashSwap.sol"]["SimpleStorage"]["abi"]
#print(abi)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

w3 = Web3(Web3.HTTPProvider("HTTP://0.0.0.0:7545"))
chain_id = 1337
my_address = "0x8f18A038d1177E8Eb6A5F5804a60101e1B910bac"
my_private_key = "0x2e72b9f6f4c507233d3f7cb1d18feaa35e704a8a1d16447cf514227954f2992c"

# Create the contract in python 
AfcashSwap = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get the latestest transaction
nonce = w3.eth.getTransactionCount(my_address)
print(nonce)
print(nonce)

# 1. Build a transaction


transaction = AfcashSwap.constructor().buildTransaction( {
    "gasPrice": w3.eth.gas_price, 
    "chainId": chain_id, 
    "from": my_address, 
    "nonce": nonce, 
})

# 2. Sign a transaction


signed_tx = w3.eth.account.signTransaction(transaction, my_private_key)

# 3. send a transaction
tx_hash =  w3.eth.send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(tx_receipt)
new_data = (w3.toHex(tx_hash))
print(new_data )


# working with Contract, you need :
# Contract Address
# Contarct ABI
AfcashSwap = w3.eth.contract(address=tx_receipt.contractAddress, abi = abi)

# Intitial value of favorite number
print(AfcashSwap.functions.retrieve().call())

store_transaction = AfcashSwap.functions.store(15).buildTransaction(
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

bsc = "https://bsc-dataseed.binance.org/"
bsc_w3 = Web3(Web3.HTTPProvider(bsc))


with open("./pancake.json", "r") as file:
    pancake_abi_file = file.read()
    #print(pancake_abi_file )

pancake_factory = "0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73"

contract_addr = bsc_w3.toChecksumAddress(
    "0x10ED43C718714eb63d5aA57B78B54704E256024E")

usdt_addr = "0x55d398326f99059fF775485246999027B3197955"

Pancake_abi = pancake_abi_file

Afcash_addr = bsc_w3.toChecksumAddress(
    "0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b")
wBNB_token = bsc_w3.toChecksumAddress(
    "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c")
#value = input(" Value: ")
# function balanceOf(address account) external view returns (uint256)
AfcashSwap = bsc_w3.eth.contract(address=wBNB_token, abi=Pancake_abi)

def Swap():
    sender_address = bsc_w3.toChecksumAddress(input("sender_address: "))
    value = input(" Value: ")
    my_private_key = input(" private_key")
    # AfcashSwap.functions.balanceOf(sender_address).call()
    balance = bsc_w3.eth.get_balance(sender_address)
    balance_2 = bsc_w3.toWei(balance, 'ether')
    print(balance_2)
    nonce = bsc_w3.eth.get_transaction_count(sender_address)
    start = time.time()
    tx_swap = AfcashSwap.functions.swapExactETHForTokens(
        0,
        [weth_token,
         Afcash_addr],
        sender_address,
        (int(time.time()) + 10000)
    ).buildTransaction(
        {
            "from": sender_address,
            'value': bsc_w3.toWei(value, 'ether'),
            "gas": 250000,
            "gasPrice": bsc_w3.toWei('5', 'gwei'),
            "nonce": nonce,
        }
    )
    signed_store_tx = bsc_w3.eth.account.signTransaction(
        tx_swap, my_private_key)
    store_tx_hash = bsc_w3.eth.send_raw_transaction(
        signed_store_tx.rawTransaction)
    store_tx_receipt = bsc_w3.eth.wait_for_transaction_receipt(store_tx_hash)
    print(store_tx_receipt)
    print("........................new...........")
    new_data2 = (bsc_w3.toHex(store_tx_hash))
    print(new_data2)


#Swap()


sender_address = bsc_w3.toChecksumAddress(input("sender_address: "))
balance = bsc_w3.eth.get_balance(sender_address)
balance_2 = bsc_w3.toWei(balance, 'ether')
print(balance_2)

input_quantity_wei = balance_2
out_2 = Web3.toWei(input_quantity_wei, 'ether')
swap_path = [Afcash_addr, weth_token]
out = AfcashSwap.functions.getAmountsOut(input_quantity_wei, swap_path).call()

# print(out)
# 0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b
# private_key: 7dbec09e214cab2b4f77636cd082c65f85442d0ea65a59c28aa177158c4fe0c0
#
sender_address: 0xC9A61631F31E2FAaE0f79328A8e30F582C0F6F7d

# 0x162fe933c42fc0521f6b5fe99927e05f1e38d930326f87a794c432a9af8754e4

function swapExactTokensForTokens(
  uint amountIn,
  uint amountOutMin,
  address[] calldata path,
  address to,
  uint deadline
) external returns (uint[] memory amounts);


receive = AfcashSwap.functions.getAmountsOut( [0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b, 0x55d398326f99059fF775485246999027B3197955], 20).call()
minReceived = receive[1] * (9/10)                                                       
receiveReadable = bsc_w3.fromWei(minReceived,'ether')                       
print("Minimum tokens to recieve:", str(receiveReadable))

def PancakeSwap():
    sender_address = "0xC9A61631F31E2FAaE0f79328A8e30F582C0F6F7d"
    #address = bsc_w3.toChecksumAddress(input("sender_address: "))
    value = input(" Value: ")
    my_private_key = input(" private_key")
    path = [Afcash_addr, usdt_addr]
    #AfcashSwap.functions.balanceOf(sender_address).call()
    balance = bsc_w3.eth.get_balance(sender_address)
    balance_2 = bsc_w3.toWei(balance, 'ether')
    print(balance_2)
    nonce = bsc_w3.eth.get_transaction_count(sender_address)
    start = time.time()
    tx_Swap = AfcashSwap.functions.swapExactTokensForTokens(0, 0,
        path,
        balance_2,
        int(time.time()) + 10000
    ).buildTransaction(
        {
            "from": balance,
            'value': bsc_w3.toWei(value, 'ether'),
            "gas": 250000,
            "gasPrice": bsc_w3.toWei('5', 'gwei'),
            "nonce": bsc_w3.eth.get_transaction_count(balance),
        }
    )
    signed_store_tx = bsc_w3.eth.account.signTransaction(
        tx_Swap, my_private_key)
    store_tx_hash = bsc_w3.eth.send_raw_transaction(
        signed_store_tx.rawTransaction)
    store_tx_receipt = bsc_w3.eth.wait_for_transaction_receipt(store_tx_hash)
    print(store_tx_receipt)
    print("........................new...........")
    new_data2 = (bsc_w3.toHex(store_tx_hash))
    print(new_data2)


PancakeSwap()



#Calculate minimum amount of tokens to receive

receive = contract.functions.getAmountsOut(amount, [tokenToSpend, tokenToBuy]).call()
minReceived = receive[1] * (9/10)                                                       
receiveReadable = web3.fromWei(minReceived,'ether')                       
print("Minimum tokens to 


receive = AfcashSwap.functions.getAmountsOut( [0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b, 0x55d398326f99059fF775485246999027B3197955], 20).call()
minReceived = receive[1] * (9/10)                          


receive = AfcashSwap.functions.getAmountsOut( [0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b, 0x55d398326f99059fF775485246999027B3197955], 20).call()
minReceived = receive[1] * (9/10)                          :", str(receiveReadable))

#Trade execution:

pancakeswap2_txn = contract.functions.swapExactTokensForTokens(minReceived, [tokenToSpend,tokenToBuy], sender_address, (int(time.time()) + 1000000)).buildTransaction({   
            'from': sender_address,
            'value': web3.toWei(amount,'ether'), 
            'gasPrice': web3.toWei('5','gwei'),
            'nonce': nonce,
            })
            
            



#Swap()


sender_address = bsc_w3.toChecksumAddress(input("sender_address: "))
balance = bsc_w3.eth.get_balance(sender_address)
balance_2 = bsc_w3.toWei(balance, 'ether')
print(balance_2)

input_quantity_wei = balance_2
out_2 = Web3.toWei(input_quantity_wei, 'ether')
swap_path = [Afcash_addr, weth_token]
out = AfcashSwap.functions.getAmountsOut(input_quantity_wei, swap_path).call()

# print(out)
# 0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b
# private_key: 7dbec09e214cab2b4f77636cd082c65f85442d0ea65a59c28aa177158c4fe0c0
#
sender_address: 0xC9A61631F31E2FAaE0f79328A8e30F582C0F6F7d

# 0x162fe933c42fc0521f6b5fe99927e05f1e38d930326f87a794c432a9af8754e4

function swapExactTokensForTokens(
  uint amountIn,
  uint amountOutMin,
  address[] calldata path,
  address to,
  uint deadline
) external returns (uint[] memory amounts);


receive = AfcashSwap.functions.getAmountsOut( [0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b, 0x55d398326f99059fF775485246999027B3197955], 20).call()
minReceived = receive[1] * (9/10)                                                       
receiveReadable = bsc_w3.fromWei(minReceived,'ether')                       
print("Minimum tokens to recieve:", str(receiveReadable))

def PancakeSwap():
    sender_address = "0xC9A61631F31E2FAaE0f79328A8e30F582C0F6F7d"
    #address = bsc_w3.toChecksumAddress(input("sender_address: "))
    value = input(" Value: ")
    my_private_key = input(" private_key")
    path = [Afcash_addr, usdt_addr]
    #AfcashSwap.functions.balanceOf(sender_address).call()
    balance = bsc_w3.eth.get_balance(sender_address)
    balance_2 = bsc_w3.toWei(balance, 'ether')
    print(balance_2)
    nonce = bsc_w3.eth.get_transaction_count(sender_address)
    start = time.time()
    tx_Swap = AfcashSwap.functions.swapExactTokensForTokens(0, 0,
        path,
        balance_2,
        int(time.time()) + 10000
    ).buildTransaction(
        {
            "from": balance,
            'value': bsc_w3.toWei(value, 'ether'),
            "gas": 250000,
            "gasPrice": bsc_w3.toWei('5', 'gwei'),
            "nonce": bsc_w3.eth.get_transaction_count(balance),
        }
    )
    signed_store_tx = bsc_w3.eth.account.signTransaction(
        tx_Swap, my_private_key)
    store_tx_hash = bsc_w3.eth.send_raw_transaction(
        signed_store_tx.rawTransaction)
    store_tx_receipt = bsc_w3.eth.wait_for_transaction_receipt(store_tx_hash)
    print(store_tx_receipt)
    print("........................new...........")
    new_data2 = (bsc_w3.toHex(store_tx_hash))
    print(new_data2)


PancakeSwap()



#Calculate minimum amount of tokens to receive

receive = contract.functions.getAmountsOut(amount, [tokenToSpend, tokenToBuy]).call()
minReceived = receive[1] * (9/10)                                                       
receiveReadable = web3.fromWei(minReceived,'ether')                       
print("Minimum tokens to recieve:", str(receiveReadable))

#Trade execution:

pancakeswap2_txn = contract.functions.swapExactTokensForTokens(minReceived, [tokenToSpend,tokenToBuy], sender_address, (int(time.time()) + 1000000)).buildTransaction({   
            'from': sender_address,
            'value': web3.toWei(amount,'ether'), 
            'gasPrice': web3.toWei('5','gwei'),
            'nonce': nonce,
            })"""