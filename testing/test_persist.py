# This file is placed in the Public Domain.


"engine"


import unittest


from nixbot.encoder import dumps, loads
from nixbot.objects import skip
from nixbot.persist import Cache


default = {}


class TestPersist(unittest.TestCase):

    def test_cache(self):
        cache = Cache()
        self.assertEqual(type(cache), Cache)
