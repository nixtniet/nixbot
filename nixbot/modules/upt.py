# This file is placed in the Public Domain.


"show uptime"


import time


from nixbot.defines import Time


def upt(msg):
    "show uptiome."
    msg.reply(Time.elapsed(time.time()-Time.starttime))
