from shortlib.repository import Repository

# Implmentation of Repository for memory (Do not use for production)

class MemoryRepo(Repository):

    def __init__(self, address) -> None:
        super().__init__(address)
        self.store = dict()

    def save(self, url, value):
        self.store[value] = (url , value , 0)

    def get(self, url):
        return self.store[url]
    
    def delete(self, url):
        return super().delete(url)
    
    def click(self , url):
        (original , new , click_count) = self.store[url]
        self.store[url] = (original , new , click_count+1)
