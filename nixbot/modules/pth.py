# This file is placed in the Public Domain.


"show path to website"


import os


def pth(event):
    "create and show path to website."
    path = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(path, "network", "index.html")
    if os.path.exists(path):
        event.reply(f"file://{path}")
    else:
        event.reply("no index.html")
