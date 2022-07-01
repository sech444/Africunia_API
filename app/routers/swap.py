from fastapi import FastAPI, WebSocket, BackgroundTasks, APIRouter, Depends, status, HTTPException, Form
from enum import Enum
import time
from webbrowser import get
import requests
from decimal import Decimal
from web3 import Web3
import json
import pandas as pd
from app.schemas import Coin_addr, Coin_symbol
from pythonpancakes import PancakeSwapAPI
import ast
ps = PancakeSwapAPI()
import csv
import asyncio


router = APIRouter()

web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/"))

#input_address = "0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b"
#output_address =  "0x55d398326f99059fF775485246999027B3197955"

#privatekey = input("PRIVATE KEY: ")
#my_address = input("YOUR WALLET: ")

afcash = "0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b"

#print(tokens.items())

#print(tokens)


'''   
with open("compiled_code.json", "w") as file:
    swap_Afcash_file = file.read()
    #print(swap_Afcash_file)
    
    

df = pd.DataFrame(list(data.items()))

sub = df.iloc[0]
sym = df[1]
print(sub)
#print(sym)'''

with open("compiled.json", "r") as file:
    Compiled_code = file.read()
    #print(Compiled_code)


@router.post("/api/v1/get_swap", tags=["Transaction"])
async def get_swap(swap_tokenA: Coin_symbol, swap_tokenB: Coin_symbol,account_to_swap:float = Form(...),account_from:str =Form(...),account_to:str = Form(...), private_key: str=Form(...)):
    TokenA = swap_tokenA.value
    TokenB  = swap_tokenB.value
    accountToswap = account_to_swap
    my_address = account_from
    privatekey = private_key
    myDict = Compiled_code
    s=str(myDict)
    D2=ast.literal_eval(s)
    #print(D2.values() ) 
    try:
        if TokenA == TokenB :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail=f"Invaild pair." )
        #print(model_name.value, Coun.value)
        keys = TokenA 
        D3 = {k: v for k, v in D2.items() if k in keys} 
        add = D3.values()  
        df = pd.DataFrame(list(add))
        #print(D3 )
        addrr = df["addr"]
        #print(df['addr'])
        addr_A = addrr[0]
            #return addr_A
        key = TokenB 
        D3 = {k: v for k, v in D2.items() if k in key} 
        add = D3.values()  
        df = pd.DataFrame(list(add))
        #print(D3 )
        addrr = df["addr"]
        #print(df['addr'])
        addr_B = addrr[0]
        #return addr_B
    
        input_address = addr_A #"0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b"
        output_address = addr_B #coin_addr
        #print(output_address)
        # https://docs.pancakeswap.finance/code/smart-contracts/pancakeswap-exchange/router-v2
        pswap_router_address = "0x10ED43C718714eb63d5aA57B78B54704E256024E"

        url = "https://api.bscscan.com/api"
        apikey = "D5XITX64P3HJAMA4S8QEPBCZ219ED1VGPG"
        input_abi = requests.get(f"{url}?apikey={apikey}&module=contract&action=getabi&address={input_address}").json()["result"]
        pswap_abi = requests.get(f"{url}?apikey={apikey}&module=contract&action=getabi&address={pswap_router_address}").json()["result"]

        input_contract = web3.eth.contract(address=Web3.toChecksumAddress(input_address), abi=input_abi)
        input_balance = input_contract.functions.balanceOf(my_address).call()

        input_quantity_wei = accountToswap
        out_2 = Web3.toWei(input_quantity_wei, 'ether')
        swap_path = [input_address, output_address]
        #out = input_contract.functions.getAmountOut(input_quantity_wei, swap_path).call()
        #print(out)

        human_input_balance = web3.fromWei(input_balance, 'ether')
        #print(f"Input balance: {human_input_balance}")

        bnb_balance = web3.eth.get_balance(my_address)
        human_bnb_balance = web3.fromWei(bnb_balance, 'ether')
        #print(f"BNB balance: {human_bnb_balance}")

        # Approve input token spend first by PancakeSwap V2 Router
        approve = input_contract.functions.approve(
                        pswap_router_address, 
                        web3.toWei(Decimal('10000'), 'ether'),
                    ).buildTransaction({
                        'from': my_address,
                        'gasPrice': web3.toWei('5', 'gwei'),
                        'nonce': web3.eth.get_transaction_count(my_address),
                    })

        signed = web3.eth.account.sign_transaction(approve, private_key=privatekey)
        tx = web3.eth.send_raw_transaction(signed.rawTransaction)
        print(f"Approve tx: {web3.toHex(tx)}. Waiting 10s for approval")
        asyncio.sleep(10)

        pswap_contract = web3.eth.contract(address=pswap_router_address, abi=pswap_abi)
        amountIn = (web3.toWei(0.00001, 'ether'))
        amount1 = pswap_contract.functions.getAmountsOut( amountIn,[input_address, output_address] ).call()
        amountOutMin = amount1[1] * 0.9
        minAmountPrint = web3.fromWei(amountOutMin, 'ether')
        print('Minimum recieved:', minAmountPrint)
        asyncio.sleep(5)

        swap_amount = accountToswap
        print(f"Swapping {swap_amount} INPUT to OUTPUT")

        pswap_txn = pswap_contract.functions.swapExactTokensForTokens(
                web3.toWei(Decimal(swap_amount), 'ether'),
                0,
                [Web3.toChecksumAddress(input_address), Web3.toChecksumAddress(output_address)],
                my_address,
                (int(time.time()) + 1000000)
            ).buildTransaction({
                'from': my_address,
                'gas': 250000,
                'gasPrice': web3.toWei('10', 'gwei'),
                'nonce': web3.eth.get_transaction_count(my_address),
            })
            
        signed = web3.eth.account.sign_transaction(pswap_txn, private_key=privatekey)
        tx = web3.eth.send_raw_transaction(signed.rawTransaction)
        #print(f"Swap tx: {web3.toHex(tx)}")
        return {"Swap tx": web3.toHex(tx)}      
    except ValueError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail=f"Transaction error, most have BNB for gas fee")
