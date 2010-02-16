#!/usr/bin/env python

from multiprocessing.managers import BaseManager

from proxies import ThingyProxy
import time
import gc
from IPython.Shell import IPShellEmbed
import traceback

ipshell = IPShellEmbed()



class ThingyManager(BaseManager): pass

ThingyManager.register('Thingy',proxytype=ThingyProxy)

while True:
    try:
        print 'Creating local manager'
        manager = ThingyManager(address=('127.0.0.1',8001), authkey='abracadabra')
        print 'Connecting manager'
        manager.connect()
        print 'Getting Thingy'
        thingy = manager.Thingy()
        while True:
            print thingy.name
            time.sleep(1)
            print '.'
    except Exception, e:
        print str(e), e.__class__
        print traceback.format_exc()
    print 'Forgetting manager'
    manager = None
    print 'Forgetting thingy'
    thingy = None
    print 'Collecting garbage'
    gc.collect()
    print 'Sleeping'
    time.sleep(1)
