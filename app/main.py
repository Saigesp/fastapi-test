from fastapi import FastAPI
from app.db import database
from app.migrations import check_migrations


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello 3"}


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()

    await check_migrations(database)


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
