# This file is placed in the Public Domain.


"in the beginning"


import logging
import os
import pathlib
import threading
import time
import _thread


from ..library import Client, Clients, Task, Thread
from ..persist import Workdir
from ..utility import Logging, Utils


from .configs import Main
from .package import Mods


class Boot:

    @classmethod
    def configure(cls):
        "configure program."
        Workdir.wdr = Workdir.wdr or Workdir.home(Main.name)
        Workdir.skel()
        Mods.dir("modules", Workdir.moddir())
        Mods.dir(f"{Main.name}.modules", Mods.moddir())
        Logging.size(len(Main.name))
        Logging.level(Main.sets.level or "warning")
        if cls.check("user"):
            Mods.dir("mods", "mods")
        if cls.check("all"):
            Main.sets.mods = ",".join(Mods.list())
        Mods.table()

    @classmethod
    def check(cls, options):
        for option in Utils.spl(options):
            if option in Utils.spl(Main.opts):
                return True
        return False

    @classmethod
    def forever(cls):
        "run forever until ctrl-c."
        while True:
            try:
                time.sleep(0.1)
            except (KeyboardInterrupt, EOFError):
                break

    @classmethod
    def init(cls, blank=False):
        "call init of modules that have an init function."
        thrs = []
        if not Main.sets.mods and blank:
            names = ""
        else:
            names = Main.sets.mods or Main.sets.default
        for name in Utils.spl(names):
            mod = Mods.get(name)
            if not mod or "init" not in dir(mod):
                continue
            thrs.append(Thread.launch(mod.init))
        if thrs and cls.check("wait"):
            for thr in thrs:
                try:
                    thr.join()
                except (KeyboardInterrupt, EOFError):
                    return False
        return True

    @classmethod
    def null(cls, io):
        "route to dev/null."
        with open('/dev/null', 'r', encoding="utf-8") as sis:
            os.dup2(sis.fileno(), io.fileno())

    @classmethod
    def pid(cls):
        "write pidfile."
        filename = Workdir.pid()
        if os.path.exists(filename):
            os.unlink(filename)
        path2 = pathlib.Path(filename)
        path2.parent.mkdir(parents=True, exist_ok=True)
        with open(filename, "w", encoding="utf-8") as fds:
            fds.write(str(os.getpid()))

    @classmethod
    def privileges(cls):
        "drop privileges."
        import getpass
        import pwd
        pwnam2 = pwd.getpwnam(getpass.getuser())
        os.setgid(pwnam2.pw_gid)
        os.setuid(pwnam2.pw_uid)

    @classmethod
    def shutdown(cls):
        "call stop on clients."
        Clients.shutdown()
        while True:
            if len(threading.enumerate()) == 1:
                break
            time.sleep(0.1)

    @classmethod
    def wrapped(cls, func, *args):
        "wrap function in a try/except, silence ctrl-c/ctrl-d."
        try:
            func(*args)
        except (KeyboardInterrupt, EOFError):
            Client.block.set()
            Task.block.set()
            _thread.interrupt_main()
        except Exception as ex:
            logging.exception(ex)
            _thread.interrupt_main()


def __dir__():
    return (
        'Boot',
    )
