from fastapi import FastAPI
from core.database import create_tables
from router import api_router

app = FastAPI(title='BakeryApi')
app.include_router(api_router)

@app.on_event("startup")
async def on_startup():
    create_tables() 