from fastapi import FastAPI
from core.database import engine, Base
from api.dependencies import xa_router

app = FastAPI(title="Hydra Api")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get('/')
def hello():
    return {"Hello", "World"}


app.include_router(xa_router)