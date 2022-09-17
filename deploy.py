from web3 import Web3

web3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
abi = '[{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"description","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint80","name":"_roundId","type":"uint80"}],"name":"getRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'
addr = '0x0567F2323251f0Aab15c8dFb1967E4e8A7D42aeE'
contract = web3.eth.contract(address=addr, abi=abi)



# Set up contract instance
# Set up while loop for prices feed
def get_exl_Price(crypto_ltc):
    contract = web3.eth.contract(address=addr, abi=abi)
    latestData = contract.functions.latestRoundData().call()
    prices = latestData[1]/ 10**6
    return prices/ 10**5

def main_exl():
  
  last_price = -1
  
  while True:
    
    crypto = 'bitcoin'
    price = get_exl_Price(crypto)
  
    if price != last_price:
      #print('BTC_ETH: ',price)
      last_price = price
    return last_price
      

  
print(main_exl())
