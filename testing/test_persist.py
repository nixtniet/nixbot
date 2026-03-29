# This file is placed in the Public Domain.


"persist tests"


import os
import sys
import unittest


sys.path.insert(0, ".")


from nixbot.configs import Main
from nixbot.objects import Data
from nixbot.persist import Disk, Workdir


Workdir.wdr = '.test'


class TestPersist(unittest.TestCase):

    def test_save(self):
        obj = Data()
        opath = Disk.write(obj)
        self.assertTrue(os.path.exists(os.path.join(
                                                    Main.wdr,
                                                    "store",
                                                    opath
                                                   )))
