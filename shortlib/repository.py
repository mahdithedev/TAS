from common.repository import Repository

# abstract class for storage repository responsible for storing URLS and their short versions
# shortlib repository
class ShortRepository(Repository):

    def __init__(self , address) -> None:
        self.address = address

    def create(self , url , new , owner_iD , owner_channel , lifetime):
        pass

    def read(self , url):
        pass

    def click(self):
        pass

    def update(self):
        return super().update()

    def delete(self , url):
        pass

    def __del__(self):
        pass