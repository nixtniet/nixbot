**NAME**

::

nixbot - NIXBOT



**SYNOPSIS**

::

    nixbot [-c|-d|-h|-s] [-a] [-v] [-w] [-l level] [-m m1,m2] [-p path]
    nixbot [cmd] [key=val] [key==val]


**DESCRIPTION**


::

    NIXBOT has all you need to program a unix cli program, such as disk
    perisistence for configuration files, event handler to handle the
    client/server connection, bork on exit for have an early exit, etc.

    NIXBOT contains python3 code to program objects in a functional way.
    it provides an "clean namespace" Object class that only has dunder
    objects, so the namespace is not cluttered with method names. This
    makes storing and reading to/from json possible.

    NIXBOT is a python3 IRC bot, it can connect to IRC, fetch and
    display RSS feeds, take todo notes, keep a shopping list and log
    text. You can run it under systemd for 24/7 presence in a IRC channel.

    NIXBOT is Public Domain.


**INSTALL**


* installation is done with pipx::

    $ pipx install nixbot
    $ pipx ensurepath

    <new terminal>

    $ nixbot srv > nixbot.service
    $ sudo mv nixbot.service /etc/systemd/system/
    $ sudo systemctl enable nixbot --now

    joins ``#nixbot`` on localhost


**USAGE**


* use ``nixbot`` to control the program, default it does nothing::

    $ nixbot
    $

* the -h option will show you possible options::


    $ nixbot -h

    usage: nixbot [-c|-d|-h|-s] [-a] [-v] [-w] [-l level] [-m m1,m2] [-p path]
           nixbot [cmd] [key=val] [key==val]

    NIXT

    options:
      -h, --help         show this help message and exit
      -c, --console      run as console.
      -d, --daemon       run as background daemon.
      -s, --service      run as service.

      -a, --all          load all modules.
      -v, --verbose      enable verbose.
      -w, --wait         wait for services to start.

      -l, --level level  set loglevel.
      -m, --mods m1,m2   modules to load.
      -p, --path path    path to working directory.

      --admin            enable admin mode
      --user             use local mods directory.

      use "nixbot cmd" for a list of commands.


* see list of commands::

    $ nixbot cmd
    cfg,cmd,dne,dpl,err,exp,imp,log,mod,mre,nme,
    pwd,rem,req,res,rss,srv,syn,tdo,thr,upt

* start console::

    $ nixbot -c
    
* start console and run irc and rss clients::

    $ nixbot -c mods=irc,rss

* list available modules::

    $ nixbot mod
    err,flt,fnd,irc,llm,log,mbx,mdl,mod,req,rss,
    rst,slg,tdo,thr,tmr,udp,upt

* start daemon::

    $ nixbot -d
    $

* start service::

    $ nixbot -s
    <runs until ctrl-c>


**COMMANDS**


* here is a list of available commands::

    atr - show attributes
    cfg - irc configuration
    cmd - commands
    dis - show deaths by disease
    dne - flag a todo as done
    dpl - sets display items
    eml - show emails
    err - show errors
    exp - export opml (stdout)
    fie - show fields of an object
    flt - show bots in fleet
    fnd - locate objects
    imp - import opml
    log - log text
    lou - enable loud mode
    man - create manual page
    mbx - import mailbox
    mod - show available modules
    nme - set name of a feed
    now - show genocide stats of today
    pth - show path to website on disk
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    req - request to the prosecutor
    res - restore objects
    rss - add a feed
    sil - enable silent mode
    srv - create service file
    syn - sync rss feeds
    tbl - create table module
    tdo - add todo item
    thr - show running threads
    tmr - timers
    udp - send udp packet to udp/irc relay
    upt - show uptime
    ver - version
    wdr - show working directory
    wsd - show wisdom


**CONFIGURATION**


* irc::

    $ nixbot cfg irc server=<server>
    $ nixbot cfg irc hannel=<channel>
    $ nixbot cfg irc nick=<nick>

* sasl::

    $ nixbot pwd <nsnick> <nspass>
    $ nixbot cfg irc password=<frompwd>


* rss::

    $ nixbot rss <url>
    $ nixbot dpl <url> <item1,item2>
    $ nixbot rem <url>
    $ nixbot nme <url> <name>

* opml::

    $ nixbot exp
    $ nixbot imp <filename>


**PROGRAMMING**

^ nixbot support modules::

    nixbot has it's user modules in the ~/.nixbot/mods directory for a hello world
    command you would edit a file in ~/.nixbot/mods/hello.py and add the following

        def hello(event):
            event.reply("hello world !!")

    typing the hello command would result into a nice hello world !!

        $ nixbot hello
        hello world !!


    commands run in their own thread and the program borks on exit to enable a
    short debug cycle, output gets flushed on print so exceptions appear in the
    systemd logs. modules can contain your own written python3 code.


**FILES**

* pipx install into three placed::

    ~/.nixbot
    ~/.local/bin/nixbot
   `~/.local/share/pipx/venvs/nixbot/*


**AUTHOR**

* email address::

    Nixt Niet <nixtniet@gmail.com>


**COPYRIGHT**

* no copyroght/license::

    NIXBOT is Public Domain.


