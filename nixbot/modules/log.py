# This file is placed in the Public Domain.


"log text"


from nixbot.objects import Data
from nixbot.persist import Disk


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
