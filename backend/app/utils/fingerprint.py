# app/utils/fingerprint.py
import uuid
import random

class FingerprintGenerator:
    def __init__(self):
        self.browser_profiles = ["chrome110", "chrome120", "chrome123"]
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/120.0.0.0",
        ]
        
    def get_browser_profile(self) -> str:
        return random.choice(self.browser_profiles)
    
    def get_user_agent(self) -> str:
        return random.choice(self.user_agents)
    
    def get_client_uuid(self) -> str:
        return str(uuid.uuid4())