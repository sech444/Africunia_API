# import the following dependencies
import asyncio
import json
from web3.middleware import geth_poa_middleware
from web3 import HTTPProvider, Web3
import web3
import requests
import pandas as pd
from sse_starlette.sse import EventSourceResponse
# Currently this method is not exposed over official web3 API,
import requests
from fastapi import (APIRouter, BackgroundTasks, Depends, FastAPI, Form,
                     HTTPException, WebSocket, status, Request)
import asyncio
import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()


STREAM_DELAY = 1  # second
RETRY_TIMEOUT = 15000  # milisecond

@app.get('/stream')
async def message_stream(request: Request):
    def new_messages():
        # Add logic here to check for new messages
        yield 'Hello World'
    async def event_generator():
        while True:
            # If client closes connection, stop sending events
            if await request.is_disconnected():
                break

            # Checks for new messages and return them to client if any
            if new_messages():
                yield {
                        "event": "new_message",
                        "id": "message_id",
                        "retry": RETRY_TIMEOUT,
                        "data": "message_content"
                }

            await asyncio.sleep(STREAM_DELAY)

    return EventSourceResponse(event_generator())