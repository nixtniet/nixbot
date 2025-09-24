# This file is placed in the Public Domain.


"cache"


import json.decoder
import os
import pathlib
import threading


from .methods import deleted, fqn, ident, search
from .objects import Object, update
from .serials import dump, load
from .utility import cdir, fntime


class Cache:

    lock = threading.RLock()
    objs = {}

    @staticmethod
    def add(path, obj):
        Cache.objs[path] = obj

    @staticmethod
    def get(path):
        return Cache.objs.get(path, None)

    @staticmethod
    def update(path, obj):
        if not obj:
            return
        if path in Cache.objs:
            update(Cache.objs[path], obj)
        else:
            Cache.add(path, obj)


def find(clz, selector=None, removed=False, matching=False):
    clz = long(clz)
    if selector is None:
        selector = {}
    for pth in fns(clz):
        obj = Cache.get(pth)
        if not obj:
            obj = Object()
            read(obj, pth)
            Cache.add(pth, obj)
        if not removed and deleted(obj):
            continue
        if selector and not search(obj, selector, matching):
            continue
        yield pth, obj


def fns(clz):
    pth = store(clz)
    for rootdir, dirs, _files in os.walk(pth, topdown=False):
        for dname in dirs:
            ddd = os.path.join(rootdir, dname)
            for fll in os.listdir(ddd):
                yield os.path.join(ddd, fll)


def last(obj, selector=None):
    if selector is None:
        selector = {}
    result = sorted(find(fqn(obj), selector), key=lambda x: fntime(x[0]))
    res = ""
    if result:
        inp = result[-1]
        update(obj, inp[-1])
        res = inp[0]
    return res


def read(obj, path):
    with Cache.lock:
        with open(path, "r", encoding="utf-8") as fpt:
            try:
                update(obj, load(fpt))
            except json.decoder.JSONDecodeError as ex:
                ex.add_note(path)
                raise ex


def write(obj, path=None):
    with Cache.lock:
        if path is None:
            path = getpath(obj)
        cdir(path)
        with open(path, "w", encoding="utf-8") as fpt:
            dump(obj, fpt, indent=4)
        Cache.update(path, obj)
        return path


class Workdir:

    name = __file__.rsplit(os.sep, maxsplit=2)[-2]
    wdr  = ""


def getpath(obj):
    return store(ident(obj))


def long(name):
    split = name.split(".")[-1].lower()
    res = name
    for names in types():
        if split == names.split(".")[-1].lower():
            res = names
            break
    return res


def moddir():
    assert Workdir.wdr
    return os.path.join(Workdir.wdr, "mods")


def pidname(name):
    assert Workdir.wdr
    return os.path.join(Workdir.wdr, f"{name}.pid")


def setwd(name, path=""):
    path = path or os.path.expanduser(f"~/.{name}")
    Workdir.wdr = Workdir.wdr or path
    skel()


def skel():
    result = ""
    if not os.path.exists(store()):
        pth = pathlib.Path(store())
        pth.mkdir(parents=True, exist_ok=True)
        pth = pathlib.Path(moddir())
        pth.mkdir(parents=True, exist_ok=True)
        result =  str(pth)
    return result


def store(pth=""):
    assert Workdir.wdr
    return os.path.join(Workdir.wdr, "store", pth)


def strip(pth, nmr=2):
    return os.path.join(pth.split(os.sep)[-nmr:])


def types():
    skel()
    return os.listdir(store())


def wdr(pth):
    assert Workdir.wdr
    return os.path.join(Workdir.wdr, pth)



def __dir__():
    return (
        'Cache',
        'Workdir',
        'find',
        'getpath',
        'last',
        'long',
        'moddir',
        'pidname',
        'read',
        'setwd',
        'store',
        'strip',
        'types',
        'write'
    )
