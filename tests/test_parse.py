# This file is placed in the Public Domain.


"parse"


import unittest


from nixbot.objects import Object
from nixbot.modules import parse


class TestParse(unittest.TestCase):

    def test_parse(self):
        obj = Object()
        result = parse(obj, "cmd")
        self.assertEqual(result, None)
