#!/usr/bin/env python
# @file        util.py
# @author      Michael Foukarakis
# @version     0.1
# @date        Created:     Tue Feb 14, 2012 13:19 GTB Standard Time
#              Last Update: Sun Apr 14, 2013 19:39 GTB Daylight Time
#------------------------------------------------------------------------
# Description: Library with useful utility functions, decorators, etc.
#------------------------------------------------------------------------
# History:     0.1 - Rolling window over an iterator
# TODO:        <+missing features+>
#------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------
import itertools, collections

def rolling_window(iterator, length, step = 1):
    streams = itertools.tee(iterator, length)
    return zip(*[itertools.islice(s, i, None, step) for s,i in zip(streams, itertools.count())])

def rolling_average(iterator, length):
    deck = collections.deque(itertools.islice(iterator, 0, length))
    rolling_sum = sum(deck)
    yield rolling_sum / length
    for elem in iterator:
        rolling_sum -= deck.popleft()
        rolling_sum += elem
        deck.append(elem)
        yield rolling_sum / length

if __name__ == '__main__':
    res = set(moving(range(10), 3))
    exp = {(0,1,2), (1,2,3), (2,3,4), (3,4,5), (4,5,6), (5,6,7), (6,7,8), (7,8,9)}

    if exp.intersection(res) == res:
        print('[+] Self-test passed.')
    else:
        print('[-] Self-test failed!')
