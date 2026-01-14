# This file is placed in the Public Domain.


"configuration"


from nixt.objects import Default
from nixt.utility import pkgname


class Config(Default):

    name = pkgname(Default)


Cfg = Config()


def __dir__():
    return (
        'Cfg',
    )
