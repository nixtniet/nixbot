# This file is placed in the Public Domain.


"version"


from ..cmnd import Main


def ver(event):
    event.reply(f"{Main.name.upper()} {Main.version}")
