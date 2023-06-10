from shortlib.repository import Repository
from datetime import date
# Implmentation of Repository for memory (Do not use for production)

class MemoryRepo(Repository):

    def __init__(self, address) -> None:
        super().__init__(address)
        self.store = dict()

    def create(self , url , new , owner_iD , owner_channel , lifetime):
        self.store[new] = (url , new , 0 , owner_iD , owner_channel , lifetime , date.today())

    def read(self, url):
        if url not in self.store:
            raise Exception("No origin with key {url} exists")
        return self.store[url]
    
    def update(self):
        return super().update()
    
    def delete(self, url):
        return super().delete(url)
    
    def click(self , url):
        (original , new , click_count) = self.store[url]
        self.store[url] = (original , new , click_count+1)
