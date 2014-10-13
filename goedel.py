#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def godel(x,y):
    """
    >>> godel(3, 81)
    3547411905944302159585997044953199142424
    """
    return (2**x)*(3**y)

def degodel_log(z):
    """
    >>> degodel_log(3547411905944302159585997044953199142424)
    (3, 81)
    """
    x,y = 0,0

    ## "galloping" phrase
    lo_y=0
    hi_y=1
    while (z % 3**hi_y == 0):
        lo_y  = hi_y
        hi_y *= 2

    # ok, we know it's somewhere lo_y <= y < hi_y
    while (lo_y < hi_y):
        test_y = int((hi_y + lo_y + 1) / 2)
        if z % 3 ** test_y:
            hi_y = test_y - 1
        else:
            lo_y = test_y

    z /= (3**lo_y)
    # numerical stability issue here
    x = int(math.log(z + 0.01, 2))
    return (x, lo_y)
