import ast
import time
from decimal import Decimal

import pandas as pd
import requests
from fastapi import (APIRouter, BackgroundTasks, Depends, FastAPI, Form,
                     HTTPException, WebSocket, status)
#from pythonpancakes import PancakeSwapAPI
from web3 import EthereumTesterProvider, HTTPProvider, Web3

from app.schemas import BNB_network, Coin_addr, Coin_symbol, USDT_network

#ps = PancakeSwapAPI()
import asyncio

from cryptography.fernet import Fernet

router = APIRouter()

web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/"))


afcash = "0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b"

# print(tokens.items())

# print(tokens)


with open("./networks_id.json", "r") as net_file:
    data_n = net_file.read()
    # print(net_file.read())

# df1 = pd.DataFrame(data_n).astype(str)
Df1 = pd.read_json(data_n)
# print(Df1["USDT"])


# print(Df1['BNB']['Binance_Smart_Chain'])


with open("compiled.json", "r") as file:
    Compiled_code = file.read()
    # print(Compiled_code)


@router.post("/api/v1/bnb_withdraw", tags=["Transaction"])
async def get_network(
    Network: BNB_network,
    account_from: str = Form(...),
    value_to_send: float = Form(...),
    account_to: str = Form(...),
    private_key: str = Form(...),
):
    # using web3py to Transfer usdt tether bep20 from one account to other  account with binance

    with open("usdt_abi.json", "r") as file:
        file.read()

    TokenA = Network.value
    print(len(TokenA))
    if len(TokenA) == 25:
        bsc = Df1["BNB"]["Binance Smart Chain"]
        # result = ast.literal_eval(bsc)
        # print(bsc)
        # return bsc
    elif len(TokenA) == 16:
        bsc = Df1["ETH"]["Ethereum Mainnet"]
        # result = ast.literal_eval(bsc)
        # print(bsc)
        # return bsc
    elif len(TokenA) == 21:
        bsc = Df1["polygon"]["Polygon Mainnet Matic"]
        # #result = ast.literal_eval(bsc)
        # print(bsc)
        # return bsc
    else:
        len(TokenA) == 25
        bsc = Df1["BNB"]["Binance Smart Chain"]
        # result = ast.literal_eval(bsc)
        # print(result)
        # return bsc
    bsc_w3 = eval(bsc)
    # print(bsc_w3)

    # print(bsc_w3.isConnected())
    account_1 = account_from
    account_2 = account_to
    value = value_to_send
    # print("sending567 ...................................................01")
    adr_verify = bsc_w3.isAddress(account_from)
    if not adr_verify:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invaild wallet"
        )

    if not bsc_w3.isAddress(account_2):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not a valid ETH wallet check the wallet and try again",
        )

    int(float(value))
    trans = bsc_w3.eth.get_balance(account_1)
    _bal2_ = bsc_w3.fromWei(trans, "ether")
    if float(value) > _bal2_:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Insufficient ETH Funds"
        )
    # print("sending567 ...................................................11")
    try:
        private_key = private_key
        priv_key = private_key
        nonce = bsc_w3.eth.getTransactionCount(account_1)

        tx = {
            "nonce": nonce,
            "to": bsc_w3.toChecksumAddress(account_2),
            "value": bsc_w3.toWei(value, "ether"),
            "gas": 200000,
            "gasPrice": bsc_w3.toWei("5.5", "gwei"),
        }
        # print("sending567 ...................................................")
        signed_tx = bsc_w3.eth.account.signTransaction(tx, priv_key)
        tx_hash = bsc_w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        new_data = bsc_w3.toHex(tx_hash)
        return {
            "New_transaction": new_data,
        }
    except ValueError:
        # print(e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transaction error, most have BNB for gas fee",
        )


@router.post("/api/v1/usdt_withdraw", tags=["Transaction"])
async def get_network(
    Network: BNB_network,
    account_from: str = Form(...),
    value_to_send: float = Form(...),
    account_to: str = Form(...),
    private_key: str = Form(...),
):
    # using web3py to Transfer usdt tether bep20 from one account to other  account with binance

    with open("usdt_abi.json", "r") as file:
        usdt_erc20 = file.read()

    TokenA = Network.value
    print(len(TokenA))
    if len(TokenA) == 25:
        bsc = Df1["BNB"]["Binance Smart Chain"]
        # result = ast.literal_eval(bsc)
        # print(bsc)
        # return bsc
    elif len(TokenA) == 16:
        bsc = Df1["ETH"]["Ethereum Mainnet"]
        # result = ast.literal_eval(bsc)
        # print(bsc)
        # return bsc
    elif len(TokenA) == 21:
        bsc = Df1["polygon"]["Polygon Mainnet Matic"]
        # #result = ast.literal_eval(bsc)
        # print(bsc)
        # return bsc
    else:
        len(TokenA) == 25
        bsc = Df1["BNB"]["Binance Smart Chain"]
        # result = ast.literal_eval(bsc)
        # print(result)
        # return bsc
    bsc_w3 = eval(bsc)
    # print(bsc_w3)

    # print(bsc_w3.isConnected())
    # print(bsc_w3.isConnected())
    account_1 = account_from
    account_2 = account_to
    value = value_to_send

    if len(private_key) == 44:
        fernet_obj = Fernet(private_key)

        encrypted_message = b"gAAAAABjFWoA9dLKDJ-eJHzveb56ka-3X-vJynPR7l1jXPTsC-CKp0Pslpx-S0_qrtLFDUKmDt3Bsf3T-w_UMXXJUDAv6hA5ZOoEJ3kjDiryL05e3bDOAlpF_aMfzYk3jPyZU1ycaIlw2vs0JCuYkW_aBNi87U5HhWOuymXIRcr2NGiUHA9HDQw="
        decrypted_message = fernet_obj.decrypt(encrypted_message).decode("utf-8")
        # decrypted_message = bytes(decrypted_mess, 'utf-8')
        key = decrypted_message
    else:
        key = private_key
    # if len(decrypted_message) == 66:
    priv_key = key

    contract_addr = bsc_w3.toChecksumAddress(
        "0x55d398326f99059fF775485246999027B3197955"
    )
    account_1 = account_from
    account_2 = account_to
    value = value_to_send

    usdt_bep = bsc_w3.eth.contract(address=contract_addr, abi=usdt_erc20)

    # print("sending567 ...................................................")
    adr_verify = bsc_w3.isAddress(account_1)
    if not adr_verify:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invaild busd_bep20_wallet"
        )
    # print("sending567 isChecksumAddress")
    if not bsc_w3.isAddress(account_2):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not a valid busd_bep20 wallet check the wallet and try again",
        )
    # print("sending567")
    # value_2 = int(float(value))
    trans = usdt_bep.functions.balanceOf(bsc_w3.toChecksumAddress(account_1)).call()
    _bal2_ = bsc_w3.fromWei(trans, "ether")
    # print(_bal2_)
    if float(value) > _bal2_:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Insufficient usdt_bep20 Funds",
        )

    # print("sending890 .....................................")
    nonce = bsc_w3.eth.get_transaction_count(account_1)
    value_to = bsc_w3.toWei(value, "ether")
    try:
        input_balance = usdt_bep.functions.transfer(
            bsc_w3.toChecksumAddress(account_2), value_to
        ).buildTransaction(
            {
                "from": bsc_w3.toChecksumAddress(account_1),
                "nonce": nonce,
                "gas": 250000,
                "gasPrice": bsc_w3.toWei("5.5", "gwei"),
            }
        )

        signed = bsc_w3.eth.account.sign_transaction(
            input_balance, private_key=priv_key
        )
        tx = bsc_w3.eth.send_raw_transaction(signed.rawTransaction)

        return {"hash_tx": bsc_w3.toHex(tx)}
    except ValueError as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transaction error, most have BNB for gas fee",
        )


@router.post("/api/v1/busdt_withdraw", tags=["Transaction"])
async def get_network(
    Network: BNB_network,
    account_from: str = Form(...),
    value_to_send: float = Form(...),
    account_to: str = Form(...),
    private_key: str = Form(...),
):
    # using web3py to Transfer usdt tether bep20 from one account to other  account with binance

    with open("usdt_abi.json", "r") as file:
        usdt_erc20 = file.read()

    TokenA = Network.value
    print(len(TokenA))
    if len(TokenA) == 25:
        bsc = Df1["BNB"]["Binance Smart Chain"]
        # result = ast.literal_eval(bsc)
        # print(bsc)
        # return bsc
    elif len(TokenA) == 16:
        bsc = Df1["ETH"]["Ethereum Mainnet"]
        # result = ast.literal_eval(bsc)
        # print(bsc)
        # return bsc
    elif len(TokenA) == 21:
        bsc = Df1["polygon"]["Polygon Mainnet Matic"]
        # #result = ast.literal_eval(bsc)
        # print(bsc)
        # return bsc
    else:
        len(TokenA) == 25
        bsc = Df1["BNB"]["Binance Smart Chain"]
        # result = ast.literal_eval(bsc)
        # print(result)
        # return bsc
    bsc_w3 = eval(bsc)
    # print(bsc_w3)

    # print(bsc_w3.isConnected())
    account_1 = account_from
    account_2 = account_to
    value = value_to_send

    if len(private_key) == 44:
        fernet_obj = Fernet(private_key)

        encrypted_message = b"gAAAAABjFWoA9dLKDJ-eJHzveb56ka-3X-vJynPR7l1jXPTsC-CKp0Pslpx-S0_qrtLFDUKmDt3Bsf3T-w_UMXXJUDAv6hA5ZOoEJ3kjDiryL05e3bDOAlpF_aMfzYk3jPyZU1ycaIlw2vs0JCuYkW_aBNi87U5HhWOuymXIRcr2NGiUHA9HDQw="
        decrypted_message = fernet_obj.decrypt(encrypted_message).decode("utf-8")
        # decrypted_message = bytes(decrypted_mess, 'utf-8')
        key = decrypted_message
    else:
        key = private_key
    # if len(decrypted_message) == 66:
    priv_key = key

    busd_addr = bsc_w3.toChecksumAddress("0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56")
    account_1 = account_from
    account_2 = account_to
    value = value_to_send

    usdt_bep = bsc_w3.eth.contract(address=busd_addr, abi=usdt_erc20)

    # print("sending567 ...................................................")
    adr_verify = bsc_w3.isAddress(account_1)
    if not adr_verify:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invaild busd_bep20_wallet"
        )
    # print("sending567 isChecksumAddress")
    if not bsc_w3.isAddress(account_2):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not a valid busd_bep20 wallet check the wallet and try again",
        )
    # print("sending567")
    # value_2 = int(float(value))
    trans = usdt_bep.functions.balanceOf(bsc_w3.toChecksumAddress(account_1)).call()
    _bal2_ = bsc_w3.fromWei(trans, "ether")
    # print(_bal2_)
    if float(value) > _bal2_:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Insufficient usdt_bep20 Funds",
        )

    # print("sending890 .....................................")
    nonce = bsc_w3.eth.get_transaction_count(account_1)
    value_to = bsc_w3.toWei(value, "ether")
    try:
        input_balance = usdt_bep.functions.transfer(
            bsc_w3.toChecksumAddress(account_2), value_to
        ).buildTransaction(
            {
                "from": bsc_w3.toChecksumAddress(account_1),
                "nonce": nonce,
                "gas": 250000,
                "gasPrice": bsc_w3.toWei("5.5", "gwei"),
            }
        )

        signed = bsc_w3.eth.account.sign_transaction(
            input_balance, private_key=priv_key
        )
        tx = bsc_w3.eth.send_raw_transaction(signed.rawTransaction)

        return {"hash_tx": bsc_w3.toHex(tx)}
    except ValueError as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transaction error, most have BNB for gas fee",
        )


@router.post("/api/v1/get_swap", tags=["Transaction"])
async def get_swap(
    swap_tokenA: Coin_symbol,
    swap_tokenB: Coin_symbol,
    account_to_swap: float = Form(...),
    account_from: str = Form(...),
    account_to: str = Form(...),
    private_key: str = Form(...),
):
    TokenA = swap_tokenA.value
    TokenB = swap_tokenB.value
    accountToswap = account_to_swap
    my_address = account_from
    privatekey = private_key
    myDict = Compiled_code
    s = str(myDict)
    D2 = ast.literal_eval(s)
    # print(D2.values() )
    try:
        if TokenA == TokenB:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Invaild pair."
            )
        # print(model_name.value, Coun.value)
        keys = TokenA
        D3 = {k: v for k, v in D2.items() if k in keys}
        add = D3.values()
        df = pd.DataFrame(list(add))
        # print(D3 )
        addrr = df["addr"]
        # print(df['addr'])
        addr_A = addrr[0]
        # return addr_A
        key = TokenB
        D3 = {k: v for k, v in D2.items() if k in key}
        add = D3.values()
        df = pd.DataFrame(list(add))
        # print(D3 )
        addrr = df["addr"]
        # print(df['addr'])
        addr_B = addrr[0]
        # return addr_B

        input_address = addr_A  # "0x8ba1940D299d3fd2d64DEB9BA8c552940A8C5d3b"
        output_address = addr_B  # coin_addr
        print(output_address)
        # https://docs.pancakeswap.finance/code/smart-contracts/pancakeswap-exchange/router-v2
        pswap_router_address = "0x10ED43C718714eb63d5aA57B78B54704E256024E"

        url = "https://api.bscscan.com/api"
        apikey = "D5XITX64P3HJAMA4S8QEPBCZ219ED1VGPG"
        input_abi = requests.get(
            f"{url}?apikey={apikey}&module=contract&action=getabi&address={input_address}"
        ).json()["result"]
        pswap_abi = requests.get(
            f"{url}?apikey={apikey}&module=contract&action=getabi&address={pswap_router_address}"
        ).json()["result"]

        input_contract = web3.eth.contract(
            address=Web3.toChecksumAddress(input_address), abi=input_abi
        )
        input_contract.functions.balanceOf(my_address).call()

        input_quantity_wei = accountToswap
        out_2 = Web3.toWei(input_quantity_wei, "ether")
        [input_address, output_address]
        # out = input_contract.functions.getAmountOut(input_quantity_wei, swap_path).call()
        # print(out)

        bnb_balance = web3.eth.get_balance(my_address)
        human_bnb_balance = web3.fromWei(bnb_balance, "ether")
        print(f"BNB balance: {human_bnb_balance}")
        # print('Approve ')
        # Approve input token spend first by PancakeSwap V2 Router
        approve = input_contract.functions.approve(
            pswap_router_address,
            web3.toWei(Decimal(out_2), "ether"),  # 100000
        ).buildTransaction(
            {
                "from": my_address,
                "gasPrice": web3.toWei("5", "gwei"),
                "nonce": web3.eth.get_transaction_count(my_address),
            }
        )

        signed = web3.eth.account.sign_transaction(approve, private_key=privatekey)
        tx = web3.eth.send_raw_transaction(signed.rawTransaction)
        # print(f"Approve tx: {web3.toHex(tx)}. Waiting 10s for approval")
        asyncio.sleep(10)

        pswap_contract = web3.eth.contract(address=pswap_router_address, abi=pswap_abi)
        amountIn = account_to_swap  # (web3.toWei(0.00001, 'ether'))
        amount1 = pswap_contract.functions.getAmountsOut(
            amountIn, [input_address, output_address]
        ).call()
        amountOutMin = amount1[1] * 0.9
        web3.fromWei(amountOutMin, "ether")
        # print('Minimum recieved:', minAmountPrint)
        asyncio.sleep(5)

        swap_amount = accountToswap
        # print(f"Swapping {swap_amount} INPUT to OUTPUT")

        pswap_txn = pswap_contract.functions.swapExactTokensForTokens(
            web3.toWei(Decimal(swap_amount), "ether"),
            0,
            [
                Web3.toChecksumAddress(input_address),
                Web3.toChecksumAddress(output_address),
            ],
            my_address,
            (int(time.time()) + 1000000),
        ).buildTransaction(
            {
                "from": my_address,
                "gas": 250000,
                "gasPrice": web3.toWei("10", "gwei"),
                "nonce": web3.eth.get_transaction_count(my_address),
            }
        )

        signed = web3.eth.account.sign_transaction(pswap_txn, private_key=privatekey)
        tx = web3.eth.send_raw_transaction(signed.rawTransaction)
        # print(f"Swap tx: {web3.toHex(tx)}")
        return {"Swap tx": web3.toHex(tx)}
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transaction error, most have BNB for gas fee",
        )

