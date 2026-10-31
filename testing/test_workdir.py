# This file is placed in the Public Domain.


"working directory"


import unittest


from nixbot.defines import Workdir


class TestWorkdir(unittest.TestCase):

    "directory to put data in."

    def test_construct(self):
        "create a workdir"
        wdr = Workdir()
        self.assertTrue(type(wdr), Workdir)

    def test_wdr(self):
        "verify wdr is set."
        self.assertEqual(Workdir.wdr, ".test")
