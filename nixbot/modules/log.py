# This file is placed in the Public Domain.


"log text"


import time


from nixbot.objects import Data
from nixbot.persist import Disk
from nixbot.utility import Time


class Log(Data):

    def __init__(self):
        super().__init__()
        self.txt = ''


def log(event):
    if not event.rest:
        event.reply("log <txt>")
        return
    obj = Log()
    obj.txt = event.rest
    Disk.write(obj)
    event.reply("ok")
