from shortlib.repository import Repository
import redis
import pickle

# Implmentation of Repository using Redis as a cache and a secondary repo for primary storage

class RedisCacheRepository(Repository):

    def __init__(self, secondaryRepo: Repository) -> None:
        # redis instance 
        self.rs = redis.Redis(decode_responses=True)
        self.secondaryRepo = secondaryRepo

    def save(self , url , value):
        self.secondaryRepo.save(url , value)

    def get(self , url):
        result = self.rs.get(url)
        if result == None:
            new = self.secondaryRepo.get(url)
            self.rs.set(url , pickle.dumps(new))
            self.rs.expire(url , 86_400)
            return new
        return pickle.loads(result)