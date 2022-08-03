from brownie import BridgeBase, network, config, accounts
from scripts.helper_scripts import get_account

print(BridgeBase)
def BridgeBase_test():
   #account = get_account()
    account = accounts[0]
    print(account)
  
    # pass the address of Afcash bridge contract
    # otherwise , deploy mocks
    '''if network.show_active() != "development":
        Afcash_bridge = config["network"][network.show_active()]["Afcash"]'''
    data = BridgeBase.deploy({'from': account})
    print('deploy ............................')
    bata2 = data.accounts()
    print(data)
    return 
  
def main():
    BridgeBase_test()