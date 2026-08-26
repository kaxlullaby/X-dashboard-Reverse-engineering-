# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import accounts, tweets, websocket

app = FastAPI(title="X Dashboard", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(accounts.router, prefix="/api/accounts", tags=["accounts"])
app.include_router(tweets.router, prefix="/api/tweets", tags=["tweets"])
app.include_router(websocket.router, prefix="/ws", tags=["websocket"])

@app.get("/")
def root():
    return {"message": "X Dashboard API", "status": "running"}

@app.on_event("startup")
def startup():
    print("[+] X Dashboard started successfully!")