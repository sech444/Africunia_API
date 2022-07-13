from py_crypto_hd_wallet import HdWalletBip44Coins, HdWalletBipChanges, HdWalletBipFactory, HdWalletSubstrateWordsNum
from fastapi import  APIRouter, Depends, status, HTTPException, Form
import json
from typing import List, Optional
import requests
from hexbytes import HexBytes



router = APIRouter()



@router.post("/api/v1/create_ exl_afcash_wallet",tags=["Coin_Wallets"])
def  EXL_wallet():
    Account.enable_unaudited_hdwallet_features()
    acct, mnemonic = Account.create_with_mnemonic()
    
    return{"mnemonic": mnemonic,
           "address" : acct.address,
            "account_key": acct.key.hex()}



@router.post("/api/v1/create_btc_wallet",tags=["Coin_Wallets"])
def btc_wallet(wallet_name: str = Form(...)):
    # Create factory
    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BITCOIN)
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom(wallet_name.upper(), HdWalletSubstrateWordsNum.WORDS_NUM_12,)

    # Generate with default parameters
    hd_wallet.Generate(addr_num=1,subaddr_off=1)
    # Specify parameters (it'll generate addresses from index 10 to 15)
    #hd_wallet.Generate()
    wallet_data = hd_wallet.ToDict()
    # After generated, you can check if the wallet is watch-only with the IsWatchOnly method
    is_wo = hd_wallet.IsWatchOnly()
    return{"wallet_name": wallet_data["wallet_name"],
           "coin_name": wallet_data["coin_name"],
           "mnemonic": wallet_data["mnemonic"],
            "master_key": wallet_data["master_key"],
           "address":wallet_data["address"],
            "seed": wallet_data["seed_bytes"],
            "account_key": wallet_data["account_key"],
            "purpose_key" : wallet_data["purpose_key"],
            "coin_key"  : wallet_data["coin_key"]
            }
    
    
@router.post("/api/v1/create_tron_wallet",tags=["Coin_Wallets"])
def TRON_wallet(wallet_name: str = Form(...)):
    # Create factory
    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.TRON)
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom(wallet_name.upper(), HdWalletSubstrateWordsNum.WORDS_NUM_12,)
    # Generate with default parameters
    hd_wallet.Generate(addr_num=1)
    # Specify parameters (it'll generate addresses from index 10 to 15)
    #hd_wallet.Generate()
    wallet_data = hd_wallet.ToDict()
    # After generated, you can check if the wallet is watch-only with the IsWatchOnly method
    is_wo = hd_wallet.IsWatchOnly()
    return{"wallet_name": wallet_data["wallet_name"],
           "coin_name": wallet_data["coin_name"],
           "mnemonic": wallet_data["mnemonic"],
            "master_key": wallet_data["master_key"],
           "address":wallet_data["address"],
            "seed": wallet_data["seed_bytes"],
            "account_key": wallet_data["account_key"],
            "purpose_key" : wallet_data["purpose_key"],
            "coin_key"  : wallet_data["coin_key"]
            }
    


@router.post("/api/v1/create_usdt_erc20_wallet",tags=["Coin_Wallets"])
def USDT_ERC20_wallet(wallet_name: str = Form(...)):
    # Create factory
    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.ETHEREUM)
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom(wallet_name.upper(), HdWalletSubstrateWordsNum.WORDS_NUM_12,)

    # Generate with default parameters
    hd_wallet.Generate(addr_num=1)
    # Specify parameters (it'll generate addresses from index 10 to 15)
    #hd_wallet.Generate()
    wallet_data = hd_wallet.ToDict()
    # After generated, you can check if the wallet is watch-only with the IsWatchOnly method
    is_wo = hd_wallet.IsWatchOnly()
    return{"wallet_name": wallet_data["wallet_name"],
           "coin_name": wallet_data["coin_name"],
           "mnemonic": wallet_data["mnemonic"],
            "master_key": wallet_data["master_key"],
           "address":wallet_data["address"],
            "seed": wallet_data["seed_bytes"],
            "account_key": wallet_data["account_key"],
            "purpose_key" : wallet_data["purpose_key"],
            "coin_key"  : wallet_data["coin_key"]
            }



@router.post("/api/v1/create_usdt_bep20_wallet",tags=["Coin_Wallets"])
def USDT_BEP20_wallet(wallet_name: str = Form(...)):
    # Create factory
    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BINANCE_SMART_CHAIN)
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom(wallet_name.upper(), HdWalletSubstrateWordsNum.WORDS_NUM_12,)

    # Generate with default parameters
    hd_wallet.Generate(addr_num=1)
    # Specify parameters (it'll generate addresses from index 10 to 15)
    #hd_wallet.Generate()
    wallet_data = hd_wallet.ToDict()
    # After generated, you can check if the wallet is watch-only with the IsWatchOnly method
    is_wo = hd_wallet.IsWatchOnly()
    return{"wallet_name": wallet_data["wallet_name"],
           "coin_name": wallet_data["coin_name"],
           "mnemonic": wallet_data["mnemonic"],
            "master_key": wallet_data["master_key"],
           "address":wallet_data["address"],
            "seed": wallet_data["seed_bytes"],
            "account_key": wallet_data["account_key"],
            "purpose_key" : wallet_data["purpose_key"],
            "coin_key"  : wallet_data["coin_key"]
            }



    
@router.post("/api/v1/create_litecoin_wallet",tags=["Coin_Wallets"])
def LITECOIN_wallet(wallet_name: str = Form(...)):
    # Create factory
    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.LITECOIN)
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom(wallet_name.upper(), HdWalletSubstrateWordsNum.WORDS_NUM_12,)

    # Generate with default parameters
    hd_wallet.Generate(addr_num=1)
    # Specify parameters (it'll generate addresses from index 10 to 15)
    #hd_wallet.Generate()
    wallet_data = hd_wallet.ToDict()
    # After generated, you can check if the wallet is watch-only with the IsWatchOnly method
    is_wo = hd_wallet.IsWatchOnly()
    return{"wallet_name": wallet_data["wallet_name"],
           "coin_name": wallet_data["coin_name"],
           "mnemonic": wallet_data["mnemonic"],
            "master_key": wallet_data["master_key"],
           "address":wallet_data["address"],
            "seed": wallet_data["seed_bytes"],
            "account_key": wallet_data["account_key"],
            "purpose_key" : wallet_data["purpose_key"],
            "coin_key"  : wallet_data["coin_key"]
            }
    
@router.post("/api/v1/create_stellar_wallet",tags=["Coin_Wallets"])
def STELLAR_wallet(wallet_name: str = Form(...)):
    # Create factory
    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.STELLAR)
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom(wallet_name.upper(), HdWalletSubstrateWordsNum.WORDS_NUM_12,)

    # Generate with default parameters
    hd_wallet.Generate(addr_num=1)
    # Specify parameters (it'll generate addresses from index 10 to 15)
    #hd_wallet.Generate()
    wallet_data = hd_wallet.ToDict()
    # After generated, you can check if the wallet is watch-only with the IsWatchOnly method
    is_wo = hd_wallet.IsWatchOnly()
    return{"wallet_name": wallet_data["wallet_name"],
           "coin_name": wallet_data["coin_name"],
           "mnemonic": wallet_data["mnemonic"],
            "master_key": wallet_data["master_key"],
           "address":wallet_data["address"],
            "seed": wallet_data["seed_bytes"],
            "account_key": wallet_data["account_key"],
            "purpose_key" : wallet_data["purpose_key"],
            "coin_key"  : wallet_data["coin_key"]
            }
@router.post("/api/v1/create_ripple_wallet",tags=["Coin_Wallets"])
def RIPPLE_wallet(wallet_name: str = Form(...)):
    # Create factory
    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.RIPPLE)
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom(wallet_name.upper(), HdWalletSubstrateWordsNum.WORDS_NUM_12,)

    # Generate with default parameters
    hd_wallet.Generate(addr_num=1)
    # Specify parameters (it'll generate addresses from index 10 to 15)
    #hd_wallet.Generate()
    wallet_data = hd_wallet.ToDict()
    # After generated, you can check if the wallet is watch-only with the IsWatchOnly method
    is_wo = hd_wallet.IsWatchOnly()
    return{"wallet_name": wallet_data["wallet_name"],
           "coin_name": wallet_data["coin_name"],
           "mnemonic": wallet_data["mnemonic"],
            "master_key": wallet_data["master_key"],
           "address":wallet_data["address"],
            "seed": wallet_data["seed_bytes"],
            "account_key": wallet_data["account_key"],
            "purpose_key" : wallet_data["purpose_key"],
            "coin_key"  : wallet_data["coin_key"]
            }
    
@router.post("/api/v1/create_dash_wallet",tags=["Coin_Wallets"])
def DASH_wallet(wallet_name: str = Form(...)):
    # Create factory
    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.DASH)
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom(wallet_name, HdWalletSubstrateWordsNum.WORDS_NUM_12,)

    # Generate with default parameters
    hd_wallet.Generate(addr_num=1)
    # Specify parameters (it'll generate addresses from index 10 to 15)
    #hd_wallet.Generate()
    wallet_data = hd_wallet.ToDict()
    # After generated, you can check if the wallet is watch-only with the IsWatchOnly method
    is_wo = hd_wallet.IsWatchOnly()
    return{"wallet_name": wallet_data["wallet_name"],
           "coin_name": wallet_data["coin_name"],
           "mnemonic": wallet_data["mnemonic"],
            "master_key": wallet_data["master_key"],
           "address":wallet_data["address"],
            "seed": wallet_data["seed_bytes"],
            "account_key": wallet_data["account_key"],
            "purpose_key" : wallet_data["purpose_key"],
            "coin_key"  : wallet_data["coin_key"]
            }
    
@router.post("/api/v1/create_btc_cash_wallet",tags=["Coin_Wallets"])
def BITCOIN_CASH_wallet(wallet_name: str = Form(...)):
    # Create factory
    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BITCOIN_CASH)
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom(wallet_name.upper(), HdWalletSubstrateWordsNum.WORDS_NUM_12,)

    # Generate with default parameters
    hd_wallet.Generate(addr_num=1)
    # Specify parameters (it'll generate addresses from index 10 to 15)
    #hd_wallet.Generate()
    wallet_data = hd_wallet.ToDict()
    # After generated, you can check if the wallet is watch-only with the IsWatchOnly method
    is_wo = hd_wallet.IsWatchOnly()
    return{"wallet_name": wallet_data["wallet_name"],
           "coin_name": wallet_data["coin_name"],
           "mnemonic": wallet_data["mnemonic"],
            "master_key": wallet_data["master_key"],
           "address":wallet_data["address"],
            "seed": wallet_data["seed_bytes"],
            "account_key": wallet_data["account_key"],
            "purpose_key" : wallet_data["purpose_key"],
            "coin_key"  : wallet_data["coin_key"]
            }
    
@router.post("/api/v1/create_binance_smart_chain_wallet",tags=["Coin_Wallets"])
def BINANCE_SMART_CHAIN_wallet(wallet_name: str = Form(...)):
    # Create factory
    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BINANCE_SMART_CHAIN)
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom(wallet_name.upper(), HdWalletSubstrateWordsNum.WORDS_NUM_12,)

    # Generate with default parameters
    hd_wallet.Generate(addr_num=1,subaddr_off=0)
    # Specify parameters (it'll generate addresses from index 10 to 15)
    #hd_wallet.Generate()
    wallet_data = hd_wallet.ToDict()
    # After generated, you can check if the wallet is watch-only with the IsWatchOnly method
    is_wo = hd_wallet.IsWatchOnly()
    return{"wallet_name": wallet_data["wallet_name"],
           "coin_name": wallet_data["coin_name"],
           "mnemonic": wallet_data["mnemonic"],
            "master_key": wallet_data["master_key"],
           "address":wallet_data["address"],
            "seed": wallet_data["seed_bytes"],
            "account_key": wallet_data["account_key"],
            "purpose_key" : wallet_data["purpose_key"],
            "coin_key"  : wallet_data["coin_key"]
            }
