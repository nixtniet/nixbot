# This file is placed in the Public Domain.


"event handler"


import logging
import os
import queue
import threading


from .threads import Thread


class Handler:

    def __init__(self):
        self.idone = threading.Event()
        self.iqueue = queue.Queue()
        self.istopped = threading.Event()

    def handle(self, event):
        "handle event."
        raise NotImplementedError

    def poller(self):
        "polling loop."
        while not self.istopped.is_set():
            self.poll()
            event = self.iqueue.get()
            if event is None:
                event.ready()
                self.iqueue.task_done()
                break
            event.orig = repr(self)
            try:
                self.handle(event)
            except (KeyboardInterrupt, EOFError):
                _thread.interrupt_main()
            except Exception as ex:
                logging.exception(ex)
                logging.debug(str(event))
                os._exit(0)
            self.iqueue.task_done()
        self.idone.set()

    def poll(self):
        "return event."

    def put(self, event):
        "put event on queue."
        self.iqueue.put(event)

    def start(self, daemon=True):
        "start polling loop."
        self.idone.clear()
        self.istopped.clear()
        Thread.launch(self.poller, daemon=daemon)

    def stop(self):
        "stop polling loop."
        self.istopped.set()

    def wait(self):
        "wait for handler to finish."
        self.iqueue.join()


def __dir__():
    return (
        'Handler',
    )
