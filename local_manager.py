#!/usr/bin/env python

from multiprocessing.managers import SyncManager
import sys

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    manager = SyncManager(address=('127.0.0.1', int(sys.argv[1])), authkey='abc')

    manager.connect()

    print manager.list()

    print 'Done'


