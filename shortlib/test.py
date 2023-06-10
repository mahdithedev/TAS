import unittest

from shortlib.memory import MemoryRepo
from shortlib.postgres import PostgresRepo
from shortlib.filerepo import FileRepo
from shortlib.redis import RedisCacheRepository

class TestClass(unittest.TestCase):

    def test_memoryrepo():
        pass