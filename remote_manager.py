#!/usr/bin/env python

from multiprocessing.managers import SyncManager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    manager = SyncManager(address=('127.0.0.1', 0), authkey='abc')
    server = manager.get_server()

    manager.start()

    d = manager.dict()
    l = manager.list(range(10))

    print server.address
    server.serve_forever()

