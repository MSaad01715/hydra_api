from fastapi import FastAPI
from core.database import engine, Base
from api.dependencies import xa_router
import os
import asyncio
import asyncpg
import socket

app = FastAPI(title="Hydra Api")

print('Current working directory: '+os.getcwd())

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get('/')
def hello():
    return {"api": { 'endpoint': 'http://127.0.0.1:8000/','status': "connected"} }


app.include_router(xa_router)