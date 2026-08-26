# app/models/database.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, JSON, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class XAccount(Base):
    __tablename__ = "x_accounts"
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    display_name = Column(String(255))
    user_id = Column(String(64))
    followers_count = Column(Integer, default=0)
    tweet_count = Column(Integer, default=0)
    is_verified = Column(Boolean, default=False)
    last_activity = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)

class Tweet(Base):
    __tablename__ = "tweets"
    id = Column(Integer, primary_key=True)
    tweet_id = Column(String(64), unique=True)
    account_id = Column(Integer)
    content = Column(Text)
    created_at = Column(DateTime)
    likes = Column(Integer, default=0)
    retweets = Column(Integer, default=0)
    scraped_at = Column(DateTime, default=datetime.utcnow)

# Database setup
engine = create_engine("sqlite:///x_dashboard.db")
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(engine)