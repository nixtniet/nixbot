# This file is placed in the Public Domain.


"text logging"


from nixbot.defines import Object
from nixbot.defines import Disk


class Log(Object):

    "log item"

    def __init__(self):
        super().__init__()
        self.txt = ''


def log(msg):
    "log text."
    if len(msg.args) == 0:
        msg.iface("<txt>")
        return
    obj = Log()
    obj.txt = msg.rest
    Disk.write(obj)
    msg.ok()
