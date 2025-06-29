# This file is placed in the Public Domain.


"a clean namespace"


class Object:

    def __contains__(self, key):
        return key in dir(self)

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __str__(self):
        return str(self.__dict__)


"methods"


def construct(obj, *args, **kwargs):
    if args:
        val = args[0]
        if isinstance(val, zip):
            update(obj, dict(val))
        elif isinstance(val, dict):
            update(obj, val)
        elif isinstance(val, Object):
            update(obj, vars(val))
    if kwargs:
        update(obj, kwargs)

def fqn(obj):
    kin = str(type(obj)).split()[-1][1:-2]
    if kin == "type":
        kin = f"{obj.__module__}.{obj.__name__}"
    return kin


def items(obj):
    if isinstance(obj, dict):
        return obj.items()
    return obj.__dict__.items()


def keys(obj):
    if isinstance(obj, dict):
        return obj.keys()
    return obj.__dict__.keys()


def update(obj, data):
    if isinstance(data, dict):
        return obj.__dict__.update(data)
    obj.__dict__.update(vars(data))


def values(obj):
    if isinstance(obj, dict):
        return obj.values()
    return obj.__dict__.values()


"unions"


def cartes(obj, other):
    pass


def complement(obj, other):
    pass


def diff(obj, other):
    pass


def power(obj, other):
    pass


def section(obj, other):
    pass


def union(obj, other):
    pass


"interface"


def __dir__():
    return (
        'Object',
        'cartes',
        'complement',
        'construct',
        'diff',
        'fmt',
        'fqn',
        'items',
        'keys',
        'power',
        'section',
        'update',
        'values',
        'union'
    )
