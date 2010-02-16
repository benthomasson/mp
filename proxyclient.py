#!/usr/bin/env python

from multiprocessing.managers import BaseManager

from proxies import ThingyProxy
import time
import gc
from IPython.Shell import IPShellEmbed

ipshell = IPShellEmbed()



class ThingyManager(BaseManager): pass

ThingyManager.register('Thingy',proxytype=ThingyProxy)

while True:
    try:
        manager = ThingyManager(address=('127.0.0.1',8001), authkey='abracadabra')
        manager.connect()
        while True:
            thingy = manager.Thingy()
            print thingy.name
            time.sleep(1)
    except Exception, e:
        print str(e), e.__class__
    manager = None
    thingy = None
    gc.collect()
    time.sleep(1)
