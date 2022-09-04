from fastapi import FastAPI, WebSocket, BackgroundTasks, APIRouter, Depends, status, HTTPException, Form, Response
from .routers import coin_prices, coin_wallets, send_tx, web_hook, swap, smart_swap, Oracle_feeds
from . import models
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer

app = FastAPI()

origins = ["http://www.africuniabank.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/coin_price", response_model=models.Item, tags=["Coin_Price"], deprecated=True)
def coins(Coin_Price: models.Item):
    return


@app.get("/coin_wallets", response_model=models.Wallets, tags=["Coin_Wallets"], deprecated=True)
def coins(Coin_Price: models.Wallets):
    return


@app.get("/Web_hook", response_model=models.Web_Hook, tags=["WebHook"], deprecated=True)
def coins(Coin_Price: models.Web_Hook):
    return


@app.get("/Transaction", response_model=models.Web_Hook, tags=["Transaction"], deprecated=True)
def coins(Coin_Price: models.Web_Hook):
    return


app.include_router(coin_prices.router)
app.include_router(coin_wallets.router)
app.include_router(send_tx.router)
app.include_router(web_hook.router)
app.include_router(swap.router)
app.include_router(smart_swap.router)
app.include_router(Oracle_feeds.router)


