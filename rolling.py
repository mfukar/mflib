#!/usr/bin/env python
# @file        rolling.py
# @author      Michael Foukarakis
# @version     0.1
# @date        Created:     Tue Feb 14, 2012 13:19 GTB Standard Time
#              Last Update: Thu Nov 13, 2014 20:19 SAST
#------------------------------------------------------------------------
# Description: Rolling window generator over an iterator.
#------------------------------------------------------------------------
# History:     0.1 - First implementation
# TODO:        <+missing features+>
#------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------
from itertools import tee, islice, count

def rolling_window(iterator, length, step = 1):
    """Returns an iterator of length LENGTH over ITERATOR, which advances by STEP after
    each call.
    >>> set(rolling_window(range(10), 3)) == {(0,1,2), (1,2,3), (2,3,4), (3,4,5), (4,5,6), (5,6,7), (6,7,8), (7,8,9)}
    True
    """
    streams = tee(iterator, length)
    return zip(*[islice(s, i, None, step) for s,i in zip(streams, count())])

def rolling_average(sequence, length):
    for win in rolling_window(sequence, length):
        yield sum(win) / length
