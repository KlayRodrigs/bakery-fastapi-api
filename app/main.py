from fastapi import FastAPI
from core.database import create_tables
from router import api_router
import uvicorn

app = FastAPI(title='BakeryApi')

app.include_router(api_router)


@app.on_event("startup")
async def on_startup():
    create_tables()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8021)
