# app/scraper/auth.py

import time
import uuid
from curl_cffi import requests
from typing import Optional

class XAuthManager:
    def __init__(self):
        self.guest_token = None
        self.auth_token = None
        self.ct0 = None
        self.last_refresh = 0
        
        # SET TOKEN DARI LO
        self.auth_token = "1da4deb3509f865cd9ea74ec939576374131aa72d096897ff39b6b600fd87ce4940880b991b449555ad5deed0963b868403bdfba5e778cb3a956988c1b3d51795d4ad9bab0729c090a7b4ae124e2c4e9"
        self.ct0 = "cb2578c8f4428911347ca375b5a9268036181509"
        
    def get_guest_token(self):
        if self.guest_token and time.time() - self.last_refresh < 3600:
            return self.guest_token
            
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0",
            "Accept": "*/*",
            "Content-Type": "application/json",
            "x-csrf-token": self.ct0,
            "x-twitter-client-language": "en",
            "x-twitter-active-user": "yes",
            "x-client-transaction-id": self._generate_transaction_id()
        }
        
        try:
            session = requests.Session(impersonate="chrome120")
            # Set cookies dulu
            session.cookies.set("auth_token", self.auth_token)
            session.cookies.set("ct0", self.ct0)
            
            session.get("https://twitter.com/", headers=headers)
            
            response = session.post(
                "https://api.twitter.com/1.1/guest/activate.json",
                headers=headers
            )
            
            if response.status_code == 200:
                data = response.json()
                self.guest_token = data.get("guest_token")
                self.last_refresh = time.time()
                return self.guest_token
                
        except Exception as e:
            print(f"[!] Guest token error: {e}")
            
        return "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
    
    def get_auth_headers(self) -> dict:
        """Get headers with auth_token for logged-in requests"""
        return {
            "Authorization": f"Bearer {self.auth_token}",
            "x-csrf-token": self.ct0,
            "x-guest-token": self.get_guest_token(),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0",
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.9",
            "Origin": "https://twitter.com",
            "Referer": "https://twitter.com/home",
            "Sec-Ch-Ua": '"Not_A Brand";v="99", "Google Chrome";v="120", "Chromium";v="120"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "X-Client-Transaction-Id": self._generate_transaction_id()
        }
    
    def _generate_transaction_id(self) -> str:
        return str(uuid.uuid4())