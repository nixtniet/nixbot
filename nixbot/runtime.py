# This file is placed in the Public Domain.


"main program"


import os
import sys
import time


from .booting import Boot
from .command import Commands
from .configs import Main
from .handler import Console, Event
from .package import Mods
from .utility import HELP, Utils


from . import modules as MODS


DEFAULT = "irc,mdl,rss,wsd"
TXT = " ".join(sys.argv[1:])
VERSION = 453


class Line(Console):

    def __init__(self):
        super().__init__()
        self.register("command", Commands.command)

    def raw(self, text):
        "write to console."
        print(text.encode('utf-8', 'replace').decode("utf-8"))


class CSL(Line):

    def callback(self, event):
        "wait for callback result."
        if not event.text:
            event.ready()
            return
        super().callback(event)
        event.wait()

    def poll(self):
        "poll for an event."
        evt = Event()
        evt.text = input("> ")
        evt.kind = "command"
        return evt


class Run:

    @classmethod
    def banner(cls):
        "hello."
        tme = time.ctime(time.time()).replace("  ", " ")
        print("%s %s since %s %s (%s)" % (
            Main.name.upper(),
            Main.version,
            tme,
            Main.level.upper() or "INFO",
            Utils.md5sum(Mods.path("tbl") or "")[:7]
        ))
        sys.stdout.flush()
        return Main.version

    @staticmethod
    def check(opts):
        for word in TXT.split():
            if not word.startswith("-"):
                continue
            for char in opts:
                if char in word:
                    return True
        return False

    @staticmethod
    def cmd(text):
        "parse text for command and run it."
        cli = Line()
        cli.start()
        for txt in text.split(" ! "):
            evt = Event()
            evt.orig = repr(cli)
            evt.text = txt
            evt.kind = "command"
            Commands.command(evt)
            evt.wait()
        return evt


class Scripts:

    @staticmethod
    def background():
        "background script."
        Boot.daemon(Main.verbose, Main.nochdir)
        Boot.privileges()
        Main.boot = True
        Boot.boot(TXT, MODS)
        Boot.scan()
        Boot.pidfile(Main.name)
        Boot.init()
        Boot.forever()

    @staticmethod
    def console():
        "console script."
        import readline
        readline.redisplay()
        Boot.boot(TXT, MODS)
        if Main.verbose:
            Run.banner()
        Boot.scan()
        Boot.init(default=False)
        csl = CSL()
        csl.start()
        Boot.forever()

    @staticmethod
    def control():
        "cli script."
        if len(sys.argv) == 1:
            return
        Main.all = True
        Boot.boot(TXT, MODS)
        Boot.scan()
        Run.cmd(TXT)

    @staticmethod
    def service():
        "service script."
        Boot.privileges()
        Main.boot = True
        Boot.boot(TXT, MODS)
        Boot.scan()
        Run.banner()
        Boot.pidfile(Main.name)
        Boot.init()
        Boot.forever()


check = Run.check


def main():
    "main"
    Main.default = DEFAULT
    Main.version = VERSION
    Main.wdr = os.path.expanduser(f"~/.{Main.name}")
    if check('a'): Main.all = True
    if check('b'): Main.boot = True
    if check('h'): print(HELP % (Main.name, Main.name))
    if check('n'): Main.noignore = True
    if check('r'): Main.read = True
    if check("u"): Main.user = True
    if check("v"): Main.verbose = True
    if check("w"): Main.wait = True
    if check("d"): Scripts.background()
    elif check("c"): Boot.wrap(Scripts.console)
    elif check("s"): Boot.wrap(Scripts.service)
    else: Boot.wrap(Scripts.control)
    Boot.shutdown()


if __name__ == "__main__":
    main()
