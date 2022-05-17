from fastapi import FastAPI, WebSocket, BackgroundTasks, APIRouter, Depends, status, HTTPException, Form
from .routers import coin_prices, coin_wallets, send_tx, web_hook
from . import models
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()



@app.get("/coin_price", response_model=models.Item, tags=["Coin_Price"], deprecated=True)
def coins(Coin_Price: models.Item):
    return 



@app.get("/coin_wallets", response_model=models.Wallets, tags=["Coin_Wallets"], deprecated=True)
def coins(Coin_Price: models.Wallets):
    return 


@app.get("/Web_hook", response_model=models.Web_Hook, tags=["WebHook"], deprecated=True)
def coins(Coin_Price: models.Web_Hook):
    return

    
app.include_router(coin_prices.router)
app.include_router(coin_wallets.router)
app.include_router(send_tx.router)
app.include_router(web_hook.router)
    
