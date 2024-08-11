from fastapi import FastAPI
from router import api_router

app = FastAPI(title='BakeryApi')
app.include_router(api_router)
