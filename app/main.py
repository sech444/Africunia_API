from fastapi import (APIRouter, BackgroundTasks, Depends, FastAPI, Form,
                     HTTPException, Response, WebSocket, status)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer

from app.routers import Oracle_feeds, coin_prices, coin_wallets, send_tx, smart_swap, swap, web_hook, new_event
from . import models
from . routers.new_event import main

app = FastAPI(title="AFRICUNIABNAK API")

origins = ["http://www.africuniabank.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/coin_price", response_model=models.Item, tags=["Coin_Price"], deprecated=True
)
def coins(Coin_Price: models.Item):
    return


@app.get(
    "/coin_wallets",
    response_model=models.Wallets,
    tags=["Coin_Wallets"],
    deprecated=True,
)
def coins(Coin_Price: models.Wallets):
    
    return


@app.get("/Web_hook", response_model=models.Web_Hook, tags=["WebHook"], deprecated=True)
def coins(Coin_Price: models.Web_Hook):
    return


@app.get(
    "/Transaction",
    response_model=models.Web_Hook,
    tags=["Transaction"],
    deprecated=True,
)
def coins(Coin_Price: models.Web_Hook):
    return


app.include_router(coin_prices.router)
app.include_router(coin_wallets.router)
app.include_router(send_tx.router)
app.include_router(web_hook.router)
app.include_router(swap.router)
app.include_router(smart_swap.router)
app.include_router(Oracle_feeds.router)
app.include_router(new_event.router)


