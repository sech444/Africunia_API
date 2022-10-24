from typing import Union
from pydantic import BaseModel


class Item(BaseModel):
    description: Union[str, None] = None


class Wallets(BaseModel):
    description: Union[str, None] = None


class Send_tx(BaseModel):
    description: Union[str, None] = None


class Web_Hook(BaseModel):
    description: Union[str, None] = None


class Smart_swap(BaseModel):
    description: Union[str, None] = None
