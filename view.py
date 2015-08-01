#!/usr/bin/env python
# @file        /Users/mfukar/src/mflib/view.py
# @author      Michael Foukarakis
# @version     0.1
# @date        Created:     Sat Aug 01, 2015 09:44 EEST
#              Last Update: Sat Aug 01, 2015 09:45 EEST
#------------------------------------------------------------------------
# Description: Various ways to view & manipulate sequences
#------------------------------------------------------------------------
# History:     <+history+>
# TODO:        <+missing features+>
#------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------
def rotate(seq, offset):
    return seq[offset:] + seq[:offset]
