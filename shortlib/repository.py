from common.repository import Repository

# abstract class for storage repository responsible for storing URLS and their short versions
# shortlib repository
class ShortRepository(Repository):

    def __init__(self , address) -> None:
        self.address = address

    def create(self , url , new , owner_ID , owner_channel , lifetime):
        pass
    

    def read(self , url):
        pass

    def click(self , url , IP , user_agent , ):
        pass

    def read_and_click(self , url , IP , user_agent):
        self.click(url , IP , user_agent)
        return self.read(url)

    def update(self):
        return super().update()

    def delete(self , url):
        pass

    def __del__(self):
        pass