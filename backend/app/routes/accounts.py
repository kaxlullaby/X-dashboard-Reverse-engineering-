# app/routes/accounts.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from ..models.database import SessionLocal, XAccount

router = APIRouter()

class AccountCreate(BaseModel):
    username: str

@router.get("/")
def get_accounts():
    db = SessionLocal()
    accounts = db.query(XAccount).all()
    db.close()
    return accounts

@router.post("/")
def create_account(account: AccountCreate):
    db = SessionLocal()
    existing = db.query(XAccount).filter(XAccount.username == account.username).first()
    if existing:
        db.close()
        raise HTTPException(status_code=400, detail="Account already exists")
    
    new_account = XAccount(username=account.username)
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    db.close()
    return new_account