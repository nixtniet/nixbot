# This file is been placed in the Public Domain.


"available commands"


from ..cmnd import Commands, Main


def cmd(event):
    event.reply(",".join(sorted(Commands.names)))
