# This file is placed in the Public Domain.


"find"


import unittest


from nixt.object import Object

from nixbot.disk  import write
from nixbot.paths import Workdir, getpath, ident
from nixbot.find  import find


class TestFind(unittest.TestCase):

    def setUp(self):
        Workdir.wdr = ".test"

    def test_find(self):
        obj = Object()
        write(obj, getpath(obj))
        result = list(find("nixt.object.Object"))
        self.assertNotEqual(len(result), 0)
