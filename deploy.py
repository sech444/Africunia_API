from web3 import Web3
from fastapi import FastAPI, WebSocket, BackgroundTasks, APIRouter, Depends, status, HTTPException, Form

w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/2b4e6cbc9f444bed94a86178238f8cad'))

with open("./fund_abi.json", 'r') as f_file:
    data_n = f_file.read()
    # print(data_n)
addr = w3.isChecksumAddress("0x4Ff26e42af59Bda47ac8D7BB15CEa3c6CaBafC7E")
value = int(0.001)
private_key="0xf862f00a6b3e060bef0ecf1240f36f02a89f3ce88cb5f7f6083260366b78e13d"
foun_me_address =w3.isChecksumAddress('0x49e8fd12fba447798ad5259c7bbabc0c8f9f9eec')
abi = data_n
# print(abi)
Afcash = w3.eth.contract(address=foun_me_address, abi=abi)
nonce =w3.eth.get_transaction_count("0x4Ff26e42af59Bda47ac8D7BB15CEa3c6CaBafC7E"),
def get_exl20_afcash():
    """A valid access token is required to access this route"""

    #result = VerifyToken(token.credentials).verify()  # 👈 updated code

    # 👇 new code
    #if result.get("status"):
        #response.status_code = status.HTTP_400_BAD_REQUEST
        #return result
    
    #account_1 =w3.isChecksumAddress("0x49e8fd12fba447798ad5259c7bbabc0c8f9f9eec")
   
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
                        'from':addr,
                        'value': w3.toWei(value, 'ether'),
                        
                    }
        ) 
        print("signing")
        #print(private_key)
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
