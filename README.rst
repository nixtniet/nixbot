|

**NAME**

    ``NIXBOT`` - Since 4 March 2019.


**SYNOPSIS**

    ``nixbot`` [-h] [-a] [-c] [-d] [-l LEVEL] [-m MODS] [-n] [-s] [-v] [-w] [-u] [--wdr WDR]
    
    | ``nixbot <cmd> [key=val] [key==val]``
    | ``nixbot -cvaw [mods=mod1,mod2]``
    |

**DESCRIPTION**

    ``NIXBOT`` holds evidence that king
    netherlands is doing a nixbot, a
    :ref:`written response <king>` where king
    netherlands confirmed taking note
    of “what i have written”, namely
    :ref:`proof  <evidence>` that medicine
    he uses in treatment laws like zyprexa,
    haldol, abilify and clozapine are not medicine
    but poison.

    Poison that makes impotent, is both
    physical (contracted muscles) and
    mental (make people hallucinate)
    torture and kills members of the
    victim groups: Elderly, Handicapped, Criminals
    and Psychiatric patients.

    ``NIXBOT`` contains :ref:`correspondence
    <writings>` with the International Criminal
    Court, asking for arrest of the king of the
    netherlands, for the nixbot he is committing
    with his new treatment laws.

    Current status is a :ref:`"no basis to proceed"
    <writings>` judgement of the prosecutor which
    requires a :ref:`"basis to prosecute" <reconsider>`
    to have the king actually arrested.


**INSTALL**


    * installation is done with pipx

    | ``$ pipx install nixbot``
    | ``$ pipx ensurepath``
    |
    | <new terminal>
    |
    | ``$ nixbot srv > genocide.service``
    | ``$ sudo mv nixbot.service /etc/systemd/system/``
    | ``$ sudo systemctl enable nixbot --now``
    |
    | joins ``#nixbot`` on localhost
    |


**USAGE**


    * use ``nixbot`` to control the program, default it does nothing

    | ``$ nixbot``
    | ``$``
    |

    * the -h option will show you possible options

    |
    | ``$ nixbot -h``
    |

    .. list-table::
      :align: left

      * - Options
        - Description

      * - -h, --help
        - show this help message and exit
      * - -a, --all
        - load all modules.
      * - -c, --console
        - start console.
      * - -d, --daemon
        - start background daemon.
      * - -i, --ignore IGNORE
        -  modules to ignore.
      * - -l, --level LEVEL
        -  set loglevel.
      * - -m, --mods MODS
        - modules to load.
      * - -n, --index INDEX
        - set index to use.
      * - -r, --read
        - read modules on start.
      * - -s, --service
        - start service.
      * - -v, --verbose
        - enable verbose.
      * - -w, --wait
        - wait for services to start.
      * - -u, --user
        - use local mods directory.
      * - -x, --admin
        - enable admin mode.
      * - --wdr WDR
        - set working directory.
      * - --nochdir
        - set working directory.


    * see list of commands
    
    | ``$ nixbot cmd``
    | ``atr,cfg,cmd,dis,dne,dpl,err,exp,fie,flt,fnd,imp,``
    | ``log,lou,man,mod,nme,now,pth,pwd,rem,req,res,rss,``
    | ``sil,slg,srv,syn,tbl,tdo,thr,tmr,upt,ver,wdr``
    |

    * start console

    | ``$ nixbot -c``
    |

    * start console and run irc and rss clients

    | ``$ nixbot -c mods=irc,rss``
    |

    * list available modules

    | ``$ nixbot mod``
    | ``adm,bsc,cfg,fie,flt,fnd,irc,log,man,mbx,mdl,pth,pwd``
    | ``req,rss,rst,sil,slg,tbl,tdo,thr,tmr,udp,wdr,web,wsd``
    |

    * start daemon

    | ``$ nixbot -d``
    | ``$``
    |

    * start service

    | ``$ nixbot -s``
    | ``<runs until ctrl-c>``
    |


**COMMANDS**

    * here is a list of available commands

    | ``atr`` - show attributes
    | ``cfg`` - irc configuration
    | ``cmd`` - commands
    | ``dis`` - show deaths by disease
    | ``dne`` - flag a todo as done
    | ``dpl`` - sets display items
    | ``eml`` - show emails
    | ``err`` - show errors
    | ``exp`` - export opml (stdout)
    | ``fie`` - show fields of an object
    | ``flt`` - show bots in fleet
    | ``fnd`` - locate objects
    | ``imp`` - import opml
    | ``log`` - log text
    | ``lou`` - enable loud mode
    | ``man`` - create manual page
    | ``mbx`` - import mailbox
    | ``mod`` - show available modules
    | ``nme`` - set name of a feed
    | ``now`` - show nixbot stats of today
    | ``pth`` - show path to website on disk
    | ``pwd`` - sasl nickserv name/pass
    | ``rem`` - removes a rss feed
    | ``req`` - request to the prosecutor
    | ``res`` - restore objects
    | ``rss`` - add a feed
    | ``sil`` - enable silent mode
    | ``syn`` - sync rss feeds
    | ``tbl`` - create table module
    | ``tdo`` - add todo item
    | ``thr`` - show running threads
    | ``tmr`` - timers
    | ``udp`` - send udp packet to udp/irc relay
    | ``upt`` - show uptime
    | ``ver`` - version
    | ``wdr`` - show working directory
    | ``wsd`` - show wisdom
    |

**CONFIGURATION**


    * irc

    | ``$ nixbot cfg irc server=<server>``
    | ``$ nixbot cfg irc hannel=<channel>``
    | ``$ nixbot cfg irc nick=<nick>``
    |

    * sasl

    | ``$ nixbot pwd <nsnick> <nspass>``
    | ``$ nixbot cfg irc password=<frompwd>``
    |

    * rss

    | ``$ nixbot rss <url>``
    | ``$ nixbot dpl <url> <item1,item2>``
    | ``$ nixbot rem <url>``
    | ``$ nixbot nme <url> <name>``
    |

    * opml

    | ``$ nixbot exp``
    | ``$ nixbot imp <filename>``
    |


**PROGRAMMING**

    nixbot has it's user modules in the ~/.genocide/mods directory so for a
    hello world command you would  edit a file in ~/.nixbot/mods/hello.py
    and add the following
    
    ::

        def hello(event):
            event.reply("hello world !!")


    typing the hello command would result into a nice hello world !!
    

    ::

        $ nixbot hello
        hello world !!


    commands run in their own thread and the program borks on exit to enable a
    short debug cycle, output gets flushed on print so exceptions appear in the
    systemd logs. modules can contain your own written python3 code.
    

**SOURCE**

    source is at `https://github.com/bthate/nixbot <https://github.com/bthate/nixbot>`_
    

**FILES**

    | ``~/.nixbot``
    | ``~/.local/bin/nixbot``
    | ``~/.local/share/pipx/venvs/nixbot/*``
    |

**AUTHOR**

    ``Bart Thate`` <``bthate@dds.nl``>
    

**COPYRIGHT**

    ``NIXBOT`` is Public Domain.
