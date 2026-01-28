# This file is put into the Public Domain.


"in case setup.py installed bin ain't owrking no more place the runtime script here"


from .objects import Default


class Config(Default):

    pass


Cfg = Config()


def __dir__():
    return (
        'Cfg',
        'Config'
    )
