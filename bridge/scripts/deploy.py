from brownie import BridgeBase, TokenExl, config, accounts
from scripts.helper_scripts import get_account

print(BridgeBase)


def BridgeBase_test():
    account = get_account()
    # account = accounts[0]
    print(account)
    data = TokenExl.deploy({"from": account})  # , publish_source=True)
    print("deploy ............................")
    data2 = data.address
    print(data2)
    return


def main():
    BridgeBase_test()
