#!/usr/bin/env python3
# @file        /Users/mfukar/src/mflib/plotter.py
# @author      Michael Foukarakis
# @version     <+version+>
# @date        Created:     Sun Jul 05, 2015 17:02 EEST
#              Last Update: Fri Apr 01, 2022 19:21 W. Europe Daylight Time
#------------------------------------------------------------------------
# Description: Various plotting & visualisation routines
#------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------
from math import floor

def plot_counter(collection, width=100):
    """Plot a histogram of a collections.Counter in text:
    """
    longest_key = max(len(key) for key in collection)
    graph_width = width - longest_key - 2
    widest = collection.most_common(1)[0][1]
    scale = graph_width / floor(widest)
    for k, v in collection.most_common():
        print('{}: {} {}'.format(k, (1 + int(v * scale)) * '=', v))
