# abstract class for storage repository responsible for storing URLS and their short versions

class Repository():

    def __init__(self , address) -> None:
        self.address = address

    def save(self , url , value):
        pass

    def click(self):
        pass

    def get(self , url):
        pass

    def delete(self , url):
        pass

    def __del__(self):
        pass