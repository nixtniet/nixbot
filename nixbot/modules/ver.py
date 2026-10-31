# This file is placed in the Public Domain.


"show version"


from nixbot.defines import MD5
from nixbot.defines import Main


def ver(msg):
    "show verson."
    msg.reply(f"{Main.name.upper()} {MD5.core()}")
