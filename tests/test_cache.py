# This file is placed in the Public Domain.


"cache"


import unittest


from nixbot.persist import Cache


class TestCache(unittest.TestCase):

    def test_construct(self):
        cache = Cache()
        self.assertEqual(type(cache), Cache)
