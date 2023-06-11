from shortlib.repository import ShortRepository
from datetime import date
import time
# Implmentation of Repository for memory (Do not use for production)

class MemoryRepo(ShortRepository):

    def __init__(self, address) -> None:
        super().__init__(address)
        self.store = dict()
        self.click_store = dict()

    def create(self , url , new , owner_iD , owner_channel , lifetime):
        self.store[new] = (url , new , owner_iD , owner_channel , lifetime , date.today())

    def read(self, url):
        if url not in self.store:
            raise Exception("No origin with key {url} exists")
        return self.store[url]
    
    def update(self):
        return super().update()
    
    def delete(self, url):
        return super().delete(url)
    
    def click(self, url, IP, user_agent):
        if self.click_store[url+IP]:
            return False
        self.click_store[url+IP] = (user_agent , time.time())
        return True