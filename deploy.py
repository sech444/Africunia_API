from ast import Try
from cmath import e
from fastapi import FastAPI, WebSocket, BackgroundTasks, APIRouter, Depends, status, HTTPException, Form
import json
from typing import List, Optional
import requests
import binance
from web3 import Web3
from coinpaprika import client as Coinpaprika
from bs4 import BeautifulSoup as BS





def afcash(crypto_dash):
    url = "https://coincodex.com/crypto/africunia-bank/"
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
    try:
    # getting the request from url 
        import re
        data = requests.get(url,headers=headers) 
        # converting the text 
        soup = BS(data.text, 'html.parser')
        
    
        # finding metha info for the current price
        ans = soup.find('div', {"class" :"coin-info-box-content"}).text
        listans = [float(s) for s in re.findall(r'[\d]*[.][\d]+', ans)]
        #print(listans)
        print(float(listans[0]))
        return float(listans[0])
    except:
        return  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"price update soon")



afcash('crypto_dash')

