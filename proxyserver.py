#!/usr/bin/env python

from multiprocessing.managers import BaseManager

from proxies import ThingyProxy
import time
from IPython.Shell import IPShellEmbed
import gc

ipshell = IPShellEmbed()


class ThingyManager(BaseManager): pass

class Thingy(object):

    name = 'ed'

aThingy = Thingy()
aThingy.name = 'al'

bThingy = Thingy()
bThingy.name = 'ben'

thingies = {}
thingies[aThingy.name] = aThingy
thingies[bThingy.name] = bThingy

def getThingy(name=None):
    if not name:
        return aThingy
    else:
        return thingies[name]

while True:
    try:
        ThingyManager.register('Thingy',getThingy,proxytype=ThingyProxy)
        manager = ThingyManager(address=('127.0.0.1',8001), authkey='abracadabra')
        server = manager.get_server()
        print 'Starting'
        server.serve_forever()
    except Exception, e:
        print str(e), e.__class__
        manager = None
        server = None
        gc.collect()
        time.sleep(5)

