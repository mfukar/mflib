#!/usr/bin/env python
# @file        /Users/mfukar/src/mflib/selfdict.py
# @author      Michael Foukarakis
# @version     0.1
# @date        Created:     Tue Oct 14, 2014 13:51 EEST
#              Last Update: Tue Oct 14, 2014 13:53 EEST
#------------------------------------------------------------------------
# Description: A defaultdict in which the key is also the value.
#------------------------------------------------------------------------
# History:     First implementation.
# TODO:        Come up with a decent name for it.
#------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------
from collections import defaultdict

class selfdict(defaultdict):
    """A defaultdict in which the key is also the value. This has the following good
    properties:
        * You can index its values using one of their properties as the key. To index
          objects based on their .name, you implement the __hash__ method to hash .name
          members.
        * If the key is not present, the default factory will be called with the key as
          the only argument.
    """
    def __missing__(self, key):
        self[key] = self.default_factory(key)
        return self[key]
