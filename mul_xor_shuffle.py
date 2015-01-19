#!/usr/bin/env python
# @file        mul_xor_shuffle.py
# @author      Michael Foukarakis
# @version     0.1
# @date        Created:     Fri Jan 06, 2012 15:55 GTB Standard Time
#              Last Update: Mon Jan 19, 2015 11:22 EET
#------------------------------------------------------------------------
# Description: A simple obfuscation scheme, just to throw people off or
#              discourage easy tampering of values.
#              Inspired from hbfs.wordpress.com/2011/11/08/mild-obfuscation
#------------------------------------------------------------------------
# History:     None yet
# TODO:        Nothing yet.
#------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------

class PerfectShuffledNumber():
    def __init__(self, value=0, mask=None):
        self.mask = mask if mask is not None else 0x1a02f3f12876ce55
        self.sign = -1 if value < 0 else 1
        bitstring = bin(self._modmul(abs(value)) ^ self.mask) [2:]
        if len(bitstring) % 2:
            bitstring = '0' + bitstring
        self.obfuscated_value = perfect_shuffle(bitstring)

    def __str__(self):
        return 'mask: {} sign: {} value: {}'.format(self.mask, self.sign, '0b'+''.join(self.obfuscated_value))

    def _modmul(self, x):
        m = 2**64
        a = 2**63 - 1
        return (a * x) % m

    def value(self):
        return self.sign * self._modmul(int(''.join((perfect_unshuffle(self.obfuscated_value))), 2) ^ self.mask)

def perfect_shuffle(seq):
    """Returns a list which contains the perfectly shuffled, supplied sequence SEQ.
    Throws AssertionError if list has odd length.
    """
    l = len(seq)

    if l % 2:
        raise AssertionError

    h = l // 2

    return [item for pair in zip(seq[:h], seq[h:]) for item in pair]

def perfect_unshuffle(seq):
    """Returns a list containing the perfectly unshuffled supplied sequence SEQ, if previously perfectly shuffled.
    """
    return seq[::2] + seq[1::2]
