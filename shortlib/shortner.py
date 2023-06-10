import random
from shortlib.repository import Repository
from shortlib.memory import MemoryRepo
from shortlib.postgres import PostgresRepo
from shortlib.redis import RedisCacheRepository

# generate a random 8 character string
# we can safely use this function if we have less than 1 million urls stored but after that
# the chance of collison is 0.01
def random_id():

    rid = ""

    for i in range(8):

        is_uppercase = random.randint(0 , 1)

        if is_uppercase:
            character_code = random.randint(0 , 25) + 65  
        else:
            character_code = random.randint(0 , 25) + 97

        rid += chr(character_code)

    return rid

class Shortner():
    
    def __init__(self , repository: Repository , base) -> None:
        self.repository = repository
        # the final url will be base + new
        self.base = base

    def shorten(self , url):
        new_url = random_id()
        self.repository.save(url , new_url)
        return new_url
    
    def get(self , url):
        return self.repository.read(url)
    
    def click(self , url):
        return self.repository.click(url)