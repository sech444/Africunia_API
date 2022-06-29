from email.headerregistry import Address
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

ps = PancakeSwapAPI()


afcash = "0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b"

tokens =  ps.tokens()

#print(tokens)

data =tokens["data"] 

with open("compiled.json", "r") as file:
    swap_Afcash_file = file.read()
    print(swap_Afcash_file)

#data2 = dict(data)
#print(data2)
# Display all elements each repeated by their number of count
ordered_dict = OrderedDict(data)
print(data["0x2aDc3468fc4149932DD16d0244B7228aA8EEAd5c"]['name'])
 
#data3 = {}
# JSON file
f = open ('compiled_code.json', "r")
  
# Reading from file
data = json.loads(f.read())
  
# Iterating through the json
# list
for i in data["0x2aDc3468fc4149932DD16d0244B7228aA8EEAd5c"]['symbol']:
    print(i)
  
# Closing file
f.close()

with open('compiled_code.json', 'w') as outfile:
    json.dump(data, outfile)
    #compiled_code = outfile.read()
    #print(compiled_code)
    
with open("compiled_code.json", "r") as file:
    Compiled_code = file.read()
    #print(Compiled_code)df = pd.DataFrame(numpy.random.randn(5,3),columns=list('ABC'))df = pd.DataFrame(numpy.random.randn(5,3),columns=list('ABC'))
#DataFrame.to_numpy
 

df = pd.DataFrame(data)#.to_numpy()
fieldnames = ['symbol', 'address']
l2 = df.head(91)
#print(l2)
for v in l2 :
    print(v)
#with open('compiled.json', 'w') as outfile:
#    json.dump(l2, outfile)
#print(df)
#sym = df[1]['symbol']
#for vals in df.head():
    #print(vals)

pdObj = pd.read_json('compiled_code.json', orient='index')

pdObj.to_csv('pancake.csv', index=True )



"""
for vals in data.head():
    print(vals)

with open('pancake.csv', newline='') as f:
    reader = csv.reader(f)
    data = [tuple(row) for row in reader]

x = data.count("bnb")


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