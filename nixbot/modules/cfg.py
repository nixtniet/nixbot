# This file is placed in the Public Domain.


"configuration"


from nixbot.objects import Data, Methods, Object
from nixbot.package import Mods
from nixbot.persist import Disk, Locate


def cfg(event):
    if not event.args:
        event.reply(f"cfg <{Mods.has('Config') + ',kernel'}>")
        return
    name = event.args[0]
    print(name, event.sets)
    config = Data()
    if name == "kernel":
        Disk.read(config, "kernel", "config")
        print(config)
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
    if name == "kernel":
        Disk.write(config, "kernel", "config")
    else:
        fnm = Locate.first(config) or Methods.ident(config)
        Disk.write(Methods.skip(config), fnm)
    event.ok()


def krn(event):
    txt = "cfg kernel " + event.rest
    Methods.parse(event, txt)
    cfg(event)
