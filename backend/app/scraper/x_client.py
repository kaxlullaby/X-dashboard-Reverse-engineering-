# app/scraper/x_client.py

import json
import time
import random
from curl_cffi import requests
from .auth import XAuthManager
from .endpoints import XEndpoints

class XScraperClient:
    def __init__(self):
        self.auth = XAuthManager()
        self.session = requests.Session(impersonate="chrome120", timeout=30)
        
        # Set cookies langsung
        self.session.cookies.set("auth_token", self.auth.auth_token)
        self.session.cookies.set("ct0", self.auth.ct0)
        
    def post_tweet(self, text: str) -> dict:
        """Post tweet using auth_token"""
        headers = self.auth.get_auth_headers()
        
        payload = {
            "variables": {
                "tweet_text": text,
                "dark_request": False,
                "media": {"media_entities": [], "possibly_sensitive": False},
                "semantic_annotation_ids": []
            },
            "features": {
                "c9s_tweet_anatomy_moderator_badge_enabled": True,
                "tweetypie_unmention_optimization_enabled": True,
                "responsive_web_edit_tweet_api_enabled": True,
                "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
                "view_counts_everywhere_api_enabled": True,
                "long_article_test_highlight": True,
                "long_article_web_read_enabled": True
            }
        }
        
        try:
            response = self.session.post(
                "https://api.twitter.com/graphql/8cFfHnSgIBhQxP9SEWjzbQ/CreateTweet",
                json=payload,
                headers=headers
            )
            
            if response.status_code == 200:
                data = response.json()
                tweet_id = data.get("data", {}).get("create_tweet", {}).get("tweet_results", {}).get("result", {}).get("rest_id", "")
                return {"success": True, "tweet_id": tweet_id}
            else:
                return {"error": f"Status {response.status_code}", "details": response.text}
                
        except Exception as e:
            return {"error": str(e)}
    
    def get_home_timeline(self, count: int = 20) -> list:
        """Get home timeline with auth"""
        headers = self.auth.get_auth_headers()
        
        variables = {
            "count": count,
            "includePromotedContent": True,
            "withCommunity": True,
            "withDownvotePerspective": False,
            "withQuickPromoteEligibilityTweetFields": True,
            "withVoice": True,
            "withV2Timeline": True
        }
        
        features = {
            "rweb_lists_timeline_redesign_enabled": True,
            "responsive_web_graphql_exclude_directive_enabled": True,
            "verified_phone_label_enabled": False,
            "creator_subscriptions_tweet_preview_api_enabled": True,
            "responsive_web_graphql_timeline_navigation_enabled": True,
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
            "c9s_tweet_anatomy_moderator_badge_enabled": True,
            "tweetypie_unmention_optimization_enabled": True,
            "responsive_web_edit_tweet_api_enabled": True,
            "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
            "view_counts_everywhere_api_enabled": True,
            "long_article_test_highlight": True,
            "long_article_web_read_enabled": True
        }
        
        params = {
            "variables": json.dumps(variables),
            "features": json.dumps(features)
        }
        
        try:
            response = self.session.get(
                "https://api.twitter.com/graphql/8Rjf8Jj8dIYKm4p3Fz4F6Q/HomeTimeline",
                params=params,
                headers=headers
            )
            
            if response.status_code == 200:
                return self._parse_tweets(response.json())
            else:
                print(f"[!] Timeline error: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"[!] Timeline error: {e}")
            return []
    
    def get_my_profile(self) -> dict:
        """Get authenticated user profile"""
        headers = self.auth.get_auth_headers()
        
        try:
            response = self.session.get(
                "https://api.twitter.com/1.1/account/verify_credentials.json",
                headers=headers
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Status {response.status_code}"}
                
        except Exception as e:
            return {"error": str(e)}
    
    def get_account_tweets(self, username: str, count: int = 20) -> list:
        # ... kode sama kayak sebelumnya
        pass
    
    def get_followers_count(self, username: str) -> int:
        # ... kode sama kayak sebelumnya
        pass
    
    def _get_user_id(self, username: str) -> str:
        # ... kode sama kayak sebelumnya
        pass
    
    def _parse_tweets(self, data: dict) -> list:
        # ... kode sama kayak sebelumnya
        pass