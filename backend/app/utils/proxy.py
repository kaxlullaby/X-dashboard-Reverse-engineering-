# app/utils/proxy.py
import random
from typing import List, Optional, Dict

class ProxyManager:
    def __init__(self, proxy_list: Optional[List[str]] = None):
        self.proxies = proxy_list or []
        self.current_index = 0
        
    def get_next_proxy(self) -> Optional[Dict[str, str]]:
        if not self.proxies:
            return None
        proxy = self.proxies[self.current_index % len(self.proxies)]
        self.current_index += 1
        return {"http": proxy, "https": proxy}
    
    def add_proxy(self, proxy: str):
        self.proxies.append(proxy)