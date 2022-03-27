from fastapi import FastAPI
from app.db import database
from app.migrations import run_migrations
from app.api import (
    get_root,
    get_postal_codes,
    get_paystats_by_age_gender,
    get_paystats_by_time_gender,
    get_adm1_by_postal_code_prefix,
)


app = FastAPI()


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    await run_migrations(database)


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()


@app.get("/")
async def root():
    return await get_root()


@app.get("/v1/postal_codes/")
async def postal_codes(bounds: str = ""):
    return await get_postal_codes(bounds)


@app.get("/v1/paystats/age-gender/{postal_code_id}")
async def paystats_age_gender(postal_code_id: int):
    return await get_paystats_by_age_gender(postal_code_id)


@app.get("/v1/paystats/time-gender/{postal_code_id}")
async def paystats_time_gender(postal_code_id: int):
    return await get_paystats_by_time_gender(postal_code_id)


@app.get("/v1/adm1/{postal_code_prefix}")
async def adm1_postal_code_prefix(postal_code_prefix: str):
    return await get_adm1_by_postal_code_prefix(postal_code_prefix)
