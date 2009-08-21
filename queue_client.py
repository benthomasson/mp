#!/usr/bin/env python

import sys

from multiprocessing.managers import BaseManager
class QueueManager(BaseManager): pass
QueueManager.register('get_queue')
m = QueueManager(address=('127.0.0.1', int(sys.argv[1])), authkey='abracadabra')
m.connect()
queue = m.get_queue()
queue.put('hello')

