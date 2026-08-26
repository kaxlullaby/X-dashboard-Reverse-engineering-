# app/routes/tweets.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..scraper.x_client import XScraperClient

router = APIRouter()

class TweetPost(BaseModel):
    text: str

@router.get("/{username}")
def get_tweets(username: str, count: int = 20):
    client = XScraperClient()
    tweets = client.get_account_tweets(username, count)
    return {"username": username, "tweets": tweets}

@router.post("/post")
def post_tweet(tweet: TweetPost):
    """Post a tweet using auth_token"""
    client = XScraperClient()
    result = client.post_tweet(tweet.text)
    
    if result.get("success"):
        return {"success": True, "tweet_id": result.get("tweet_id")}
    else:
        raise HTTPException(status_code=500, detail=result.get("error"))

@router.get("/timeline")
def get_timeline(count: int = 20):
    """Get home timeline using auth_token"""
    client = XScraperClient()
    tweets = client.get_home_timeline(count)
    return {"tweets": tweets}

@router.get("/profile")
def get_profile():
    """Get authenticated user profile"""
    client = XScraperClient()
    profile = client.get_my_profile()
    return profile