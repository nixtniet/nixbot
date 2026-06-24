# This file is placed in the Public Domain.


"if it repeats it's important"


import threading
import time


from .objects import Base
from .persist import Disk, Locate
from .threads import Thread


class Repeater:

    fnm = ""
    running = threading.Event()
    stopped = threading.Event()
    todo = Base()

    @classmethod
    def add(cls, sleep, func, *args, **kwargs):
        "add a repeater."
        if not cls.running.is_set():
            cls.start()
        todotime = str(time.time() + sleep)
        cls.todo[todotime] = (sleep, func, args, kwargs)

    @classmethod
    def loop(cls):
        "repeater loop."
        while not cls.stopped.is_set():
            time.sleep(1.0)
            next = []
            now = time.time()
            for todotime in cls.todo:
                if now > float(todotime):
                    sleep, func, args, kwargs = getattr(cls.todo, todotime)
                    Thread.launch(func, *args, **kwargs)
                    next.append(todotime)
            for todotime in next:
                    sleep, func, args, kwargs = getattr(cls.todo, todotime)
                    cls.add(sleep, func, *args, **kwargs)
                    del cls.todo[todotime]

    @classmethod
    def start(cls):
        "start repeater loop."
        cls.running.set()
        cls.stopped.clear()
        Thread.launch(cls.loop)

    @classmethod
    def stop(cls):
        "stop repeater loop."
        cls.stopped.set()                


def __dir__():
    return (
        'Repeater',
    )
