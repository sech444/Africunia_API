from fastapi import FastAPI, WebSocket, BackgroundTasks, APIRouter, Depends, status, HTTPException, Form
import json
from web3 import Web3
from time import sleep
import requests
from bs4 import BeautifulSoup as BS
from requests.adapters import HTTPAdapter
#from requests.packages.urllib3.util.retry import Retry
# w3 = Web3(Web3.HTTPProvider('https://rpc.exlscan.com/'))


# router = APIRouter()

# contract_addr ='0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b'
# dbAddress = w3.toChecksumAddress(contract_addr).lower()
# #print(dbAddress )
# with open("pancake.json", "r") as file:
#     Compiled_code = file.read()
#     #print(Compiled_code)

# Afcash = w3.eth.contract(address= contract_addr, abi=Compiled_code)

#print(Afcash.functions.name().call())

'''alice = input('addr to reciver: ')#'0x9875adb3f2ab35cb2328c9974292e5711eced73b' 0xB1E6c654Cd79265865b07611CAB04E80d245e92e
Address = w3.toChecksumAddress(alice)
bals = Afcash.functions.balanceOf(Address).call()
#bals2 = w3.eth.get_balance(Address)
bals_ = w3.fromWei(bals, 'ether'),
#print(bals2)
print(bals_)'''



'''acct_from = input("acct_from: ")
value_to_send = input("value: ")
my_private_key = input("private_key: ")
tx_hash = Afcash.functions.transferFrom(acct_from, alice, value_to_send).call()
'''

# 2. Sign a transaction





# working with Contract, you need :
# Contract Address
# Contarct ABI
#AfcashSwap = w3.eth.contract(address=tx_receipt.contractAddress, abi = abi)

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


from web3 import Web3
from fastapi import FastAPI, WebSocket, BackgroundTasks, APIRouter, Depends, status, HTTPException, Form


w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/2b4e6cbc9f444bed94a86178238f8cad'))

with open("./fund_abi.json", 'r') as f_file:
    data_n = f_file.read()
    # print(data_n)
addr = w3.isChecksumAddress("0x4Ff26e42af59Bda47ac8D7BB15CEa3c6CaBafC7E")
value = 0.001
private_key="0x2284e003c9e2328abcdbae2bade56f9c862ad8c43a0fd045a21478d41e9dc942"
foun_me_address =w3.isChecksumAddress('0x49e8fd12fba447798ad5259c7bbabc0c8f9f9eec')
abi = data_n
# print(abi)
Afcash = w3.eth.contract(address=foun_me_address, abi=abi)

def get_exl20_afcash():
    """A valid access token is required to access this route"""

    #result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # 👇 new code
    #if result.get("status"):
        #response.status_code = status.HTTP_400_BAD_REQUEST
        #return result
    

   
    #print("sending234")
    # adr_verify = w3.isAddress(account_1)
    # if not adr_verify:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"Invaild exl20_afcash wallet")

    # if not Web3.isChecksumAddress(account_2):
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"Not a valid exl20_afcash wallet check the wallet and try again")
    #print("sending567")
    #value_2 = int(float(value))
    # trans = Afcash.functions.balanceOf(account_1).call()
    # _bal2_ = w3.fromWei(trans, 'ether')
    # if float(value) > _bal2_:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"Insufficient exl20_afcash Funds")
    print("sending890")
    #value_to = w3.toWei(value, 'ether')
    try:
        input_balance = Afcash.functions.fund().buildTransaction(
            {
                        'from': w3.isChecksumAddress("0x4Ff26e42af59Bda47ac8D7BB15CEa3c6CaBafC7E"),
                        'to' : w3.isChecksumAddress("0x49e8fd12fba447798ad5259c7bbabc0c8f9f9eec"),
                        'value': w3.toWei(value, 'ether'),
                        'gasPrice': w3.toWei('55', 'gwei'),
                        'gas' : 2500000,
                        'nonce': w3.eth.get_transaction_count("0x4Ff26e42af59Bda47ac8D7BB15CEa3c6CaBafC7E"),
                    }
        ) 
        print("signing")
        print(private_key)
        signed = w3.eth.account.sign_transaction(
            input_balance, private_key=private_key)
        tx = w3.eth.send_raw_transaction(signed.rawTransaction)
        #print(tx)
        #print(f"Swap tx: {w3.toHex(tx)}")
        return {"hash_tx": w3.toHex(tx)}
    except ValueError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Transaction error, most have exl20 for gas fee")
        
        
get_exl20_afcash()