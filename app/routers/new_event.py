# import the following dependencies
import asyncio
import json
from web3.middleware import geth_poa_middleware
from web3 import HTTPProvider, Web3
import web3
import requests
import pandas as pd
from sse_starlette.sse import EventSourceResponse
# Currently this method is not exposed over official web3 API,
import requests
from fastapi import (APIRouter, BackgroundTasks, Depends, FastAPI, Form,
                     HTTPException, WebSocket, status, Request)

router = APIRouter()
# add your blockchain connection information
# infura_url = "https://rpc.exlscan.com"
# web3 = Web3(Web3.HTTPProvider(infura_url))
w3 = web3.Web3(web3.HTTPProvider('https://rpc.exlscan.com'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract_addr = w3.toChecksumAddress(
    "0x561748A6B1D8b328788dc49C03e0605cc2030953")

ABI = """[{"type":"constructor","stateMutability":"nonpayable","inputs":[]},{"type":"event","name":"Approval","inputs":[{"type":"address","name":"_owner","internalType":"address","indexed":true},{"type":"address","name":"_spender","internalType":"address","indexed":true},{"type":"uint256","name":"_value","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"Burn","inputs":[{"type":"address","name":"from","internalType":"address","indexed":true},{"type":"uint256","name":"value","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"Transfer","inputs":[{"type":"address","name":"from","internalType":"address","indexed":true},{"type":"address","name":"to","internalType":"address","indexed":true},{"type":"uint256","name":"value","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"allowance","inputs":[{"type":"address","name":"","internalType":"address"},{"type":"address","name":"","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"success","internalType":"bool"}],"name":"approve","inputs":[{"type":"address","name":"_spender","internalType":"address"},{"type":"uint256","name":"_value","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"balanceOf","inputs":[{"type":"address","name":"","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"success","internalType":"bool"}],"name":"burn","inputs":[{"type":"uint256","name":"_value","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"success","internalType":"bool"}],"name":"burnFrom","inputs":[{"type":"address","name":"_from","internalType":"address"},{"type":"uint256","name":"_value","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint8","name":"","internalType":"uint8"}],"name":"decimals","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"string","name":"","internalType":"string"}],"name":"name","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"string","name":"","internalType":"string"}],"name":"symbol","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"totalSupply","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"success","internalType":"bool"}],"name":"transfer","inputs":[{"type":"address","name":"_to","internalType":"address"},{"type":"uint256","name":"_value","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"success","internalType":"bool"}],"name":"transferFrom","inputs":[{"type":"address","name":"_from","internalType":"address"},{"type":"address","name":"_to","internalType":"address"},{"type":"uint256","name":"_value","internalType":"uint256"}]}]
    """
address = contract_addr
contract_abi = ABI

contract = w3.eth.contract(address, abi=contract_abi)
accounts = w3.eth.accounts

# python object to be appended
# function to add to JSON


def write_json(new_data, filename='./wallet_id.json'):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["wallet_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)


@router.post("/api/v1/reg_afcash_wallet")
def register_wallet(wallet_id: str = Form(...)):
    try:
        # python object to be appended
        y = wallet_id
        write_json(y)
        return {"wallet_id": 'register'}
    except ValueError as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"faild to register",
        )


patients_df = pd.read_json('./wallet_id.json')
by_t = patients_df.head()
# print(by_t)
# Loop along dictionary keys
# printing keys and values

# print(i, value)
def main():
    event_filter = contract.events.Transfer.createFilter(fromBlock="latest")
    # event_filter = contract.events.Deposit.createFilter(fromBlock='latest')
    loop = asyncio.get_event_loop()
    #live = loop.run_until_complete(asyncio.gather(log_loop(event_filter, 2)))
    #await asyncio.sleep(poll_interval)
    try:
        loop.run_until_complete(asyncio.gather(log_loop(event_filter, 2)))
    finally:
        pass
    #return live

def handle_event(event):
    print(w3.eth.get_block("latest")["number"])
    for i in patients_df:
        value = patients_df[i]
    temp = json.loads(w3.toJSON(event))
    print(temp)
    try:
        if (value == temp["args"]["to"]).any():
            print(temp["args"]["to"])
            print(temp["args"]['value'] / 10**18)
            to = temp["args"]["to"]
            value = temp["args"]['value'] / 10**18
            data = {'to': to, 'value': value}
            webhook_url = "https://webhook.site/10aece72-e5a1-4073-a10a-4b91de6771fe"
            r = requests.post(webhook_url, data=json.dumps(data))
            #return r 
    except ValueError as e:
        print(e)
        main()

async def log_loop(event_filter, poll_interval):
    while True:
        for Transfer in event_filter.get_new_entries():
            print("I'm here")
            handle_event(Transfer)
        await asyncio.sleep(poll_interval)





#app = FastAPI()


STREAM_DELAY = 5# second
RETRY_TIMEOUT = 15000  # milisecond

@router.get('/stream')
async def message_stream(request: Request):
    def new_messages():
        # Add logic here to check for new messages
        main()
        yield main()
    async def event_generator():
        # while True:
        #     # If client closes connection, stop sending events
        #     if await request.is_disconnected():
        #         pass#break 
            
                # Checks for new messages and return them to client if any
        if new_messages():
            yield {
                    "event": main(),
                    "id": "message_id",
                    "retry": RETRY_TIMEOUT,
                    "data": "message_content"
                    }

            await asyncio.sleep(STREAM_DELAY)

    return EventSourceResponse(event_generator())


