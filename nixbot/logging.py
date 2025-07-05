# This file is placed in the Public Domain.


"logging"


import sys
import logging as logger


LEVELS = {'debug': logger.DEBUG,
          'info': logger.INFO,
          'warning': logger.WARNING,
          'warn': logger.WARNING,
          'error': logger.ERROR,
          'critical': logger.CRITICAL
         }


def level(loglevel="debug"):
    if loglevel != "none":
        format_short = "%(message)-80s"
        datefmt = '%H:%M:%S'
        logger.basicConfig(stream=sys.stderr, datefmt=datefmt, format=format_short)
        logger.getLogger().setLevel(LEVELS.get(loglevel))


def rlog(loglevel, txt, ignore=None):
    if ignore is None:
        ignore = []
    for ign in ignore:
        if ign in str(txt):
            return
    logger.log(LEVELS.get(loglevel), txt)


"interface"


def __dir__():
    return (
        'level',
        'rlog'
    )
