# import the following dependencies
import json
from web3 import Web3
import asyncio

# add your blockchain connection information
infura_url = 'https://goerli.infura.io/v3/2b4e6cbc9f444bed94a86178238f8cad'
web3 = Web3(Web3.HTTPProvider(infura_url))



contract_addr=web3.toChecksumAddress('0x49e8fd12fba447798ad5259c7bbabc0c8f9f9eec')

with open("./fund_abi.json", "r") as file:
    usdt_erc20 = file.read()
    
contract_address = contract_addr
contract_abi = usdt_erc20 

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def handle_event(event):
    print(web3.eth.get_block('latest')['number'])

    temp = json.loads(Web3.toJSON(event))
    print(temp)

async def log_loop(event_filter, poll_interval):
    while True:
        for PairCreated in event_filter.get_new_entries():
            print("I'm here")
            handle_event(PairCreated)
        await asyncio.sleep(poll_interval)


def main():
    event_filter = contract.events.Sent.createFilter(fromBlock='latest')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop(event_filter, 2)))
    finally:
        loop.close()

if __name__ == "__main__":
    main()