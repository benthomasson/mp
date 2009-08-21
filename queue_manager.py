#!/usr/bin/env python
from multiprocessing.managers import BaseManager
import Queue
queue = Queue.Queue()
class QueueManager(BaseManager): pass
QueueManager.register('get_queue', callable=lambda:queue)
m = QueueManager(address=('127.0.0.1', 0), authkey='abracadabra')
s = m.get_server()
print s.address
s.serve_forever()

