# This file is placed in the Public Domain.


"configuration"


from nixbot.objects import Data, Methods, Object
from nixbot.package import Mods
from nixbot.persist import Disk, Locate


def cfg(event):
    if not event.args:
        mods = f"cfg <{Mods.has('Config') + ',main'}>"
        if mods.startswith(","):
            mods = mods[1:]
        event.reply(mods)
        return
    name = event.args[0]
    config = Data()
    if name == "main":
        Disk.read(config, "main", "config")
    else:
        mod = Mods.get(name)
        if not mod:
            event.reply(f"no {name} module found.")
            return
        config = getattr(mod, "Config", None)
        if not config:
            event.reply("no configuration found.")
            return
    if not event.sets:
        event.reply(
            Methods.fmt(
                config,
                Object.keys(config),
                skip=["word",]
            )
        )
        return
    Methods.edit(config, event.sets)
    if name == "main":
        Disk.write(config, "main", "config")
    else:
        fnm = Locate.first(config) or Methods.ident(config)
        Disk.write(Methods.skip(config), fnm)
    event.ok()


def krn(event):
    txt = "cfg main " + event.rest
    Methods.parse(event, txt)
    cfg(event)
