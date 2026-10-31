# This file is placed in the Public Domain.


"disk"


import unittest


from nixbot.defines import Disk


class TestStorage(unittest.TestCase):

    "disk read/write"

    def test_construct(self):
        "create a disk."
        disk = Disk()
        self.assertTrue(disk)
