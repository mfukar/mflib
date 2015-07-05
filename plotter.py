#!/usr/bin/env python
# @file        /Users/mfukar/src/mflib/plotter.py
# @author      Michael Foukarakis
# @version     <+version+>
# @date        Created:     Sun Jul 05, 2015 17:02 EEST
#              Last Update: Sun Jul 05, 2015 17:04 EEST
#------------------------------------------------------------------------
# Description: Various plotting & visualisation routines
#------------------------------------------------------------------------
# History:     <+history+>
# TODO:        <+missing features+>
#------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------

def plot_counter(collection, width=120):
    """Plot a histogram of a collections.Counter in text:
    """
    longest_key = max( len(key for key in collection))
    graph_width = width - longest_key - 2
    widest = collection.most_common(1)[0][1]
    scale = graph_width / floor(widest)
    for k, v in sorted(collection.items()):
        print('{}: {}'.format(k, int(v * scale) * '='))
