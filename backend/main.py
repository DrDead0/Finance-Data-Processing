from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import ASCENDING
from db import client, db
from api import router as api_router
from config import get_settings

settings = get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    db.users.create_index("email", unique=True)
    db.financial_records.create_index([("date", ASCENDING)])
    db.financial_records.create_index([("category", ASCENDING)])
    db.financial_records.create_index([("type", ASCENDING)])
    db.financial_records.create_index([("created_by", ASCENDING)])
    yield
    client.close()

app = FastAPI(
    title="Finance Dashboard API",
    description="Finance Data Processing and Access Control System",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_origin_regex=settings.ALLOWED_ORIGIN_REGEX,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

@app.get("/health", tags=["Infrastructure"])
def health_check():
    return {"status": "ok"}
