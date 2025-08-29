# This file is placed in the Public Domain.


"functions"


import unittest


from nixbot.objects import Object, edit, fmt


class TestFunctions(unittest.TestCase):

    def test_edit(self):
        obj = Object()
        edit(obj, {"a": "b"})
        self.assertEqual(obj.a, "b")
