from shortlib.repository import Repository

# Implmentation of Repository for memory (Do not use for production)

class MemoryRepo(Repository):

    def __init__(self, address) -> None:
        super().__init__(address)
        self.store = dict()

    def create(self, url, value):
        self.store[value] = (url , value , 0)

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
