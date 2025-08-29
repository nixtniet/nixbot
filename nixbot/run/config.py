# This file is placed in the Public Domain.


"runtime"


class Main:

    debug   = False
    gets    = {}
    init    = ""
    level   = "warn"
    md5     = False
    name    = __package__.split(".", maxsplit=1)[0].lower()
    opts    = {}
    sets    = {}
    verbose = False
    version = 130


def __dir__():
    return (
        'Main',
    )
