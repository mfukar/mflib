#!/usr/bin/env python
# @file        goedel.py
# @author      Michael Foukarakis
# @version     0.1
# @date        Created:     Thu Oct 16, 2014 10:57 EEST
#              Last Update: Thu Nov 13, 2014 09:25 SAST
#------------------------------------------------------------------------
# Description: Implementation of a simple pairing function using Gödel numbering. Code
# taken from hbfs.wordpress.com/2011/09/27/pairing-functions/
#------------------------------------------------------------------------
# History:     <+history+>
# TODO:        <+missing features+>
#------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------
from math import log

def godel(x,y):
    """
    >>> godel(3, 81)
    3547411905944302159585997044953199142424
    >>> godel(51, 29)
    154541870963391800995410345984
    """
    return (2**x)*(3**y)

def degodel_log(z):
    """
    >>> degodel_log(3547411905944302159585997044953199142424)
    (3, 81)
    """
    x, y = 0, 0

    ## "Galloping" phase:
    lo_y, hi_y = 0, 1
    while z % 3**hi_y == 0:
        lo_y  = hi_y
        hi_y *= 2

    # OK, we know it's somewhere lo_y <= y < hi_y:
    while lo_y < hi_y:
        test_y = int((hi_y + lo_y + 1) / 2)
        if z % 3 ** test_y:
            hi_y = test_y - 1
        else:
            lo_y = test_y

    z /= 3**lo_y
    # Numerical stability issue here:
    x = int(log(z + 0.01, 2))
    return (x, lo_y)

if __name__ == '__main__':
    import doctest
    fail, total = doctest.testmod()
