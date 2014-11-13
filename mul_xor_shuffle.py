#!/usr/bin/env python
# @file        mul_xor_shuffle.py
# @author      Michael Foukarakis
# @version     0.1
# @date        Created:     Fri Jan 06, 2012 15:55 GTB Standard Time
#              Last Update: Thu Oct 23, 2014 15:31 SAST
#------------------------------------------------------------------------
# Description: A simple obfuscation scheme, just to throw people off or
#              discourage easy tampering of values.
#------------------------------------------------------------------------
# History:     None yet
# TODO:        Nothing yet.
#------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------
mask = 0x1a02f3f12876ce55

def _binstr(n, l = 16):
    tmp = n<0 and binarystr((2<<l)+n) or n and _binstr(n>>1).lstrip('0') + str(n&1) or '00'
    if len(tmp) % 2:
        tmp = '0' + tmp
    return tmp

def _modmul(x):
    m = 2**64
    a = 2**63 - 1
    return (a * x) % m

def perfect_shuffle(seq):
    """Perfectly shuffles the supplied sequence SEQ.
    Throws AssertionError if list has odd length.
    """
    l = len(seq)

    if l % 2:
        raise AssertionError

    h = l//2

    return [item for pair in zip(seq[:h], seq[h:]) for item in pair]

def perfect_unshuffle(seq):
    """Perfectly unshuffles the supplied sequence SEQ, if previously perfectly shuffled.
    """
    return seq[::2] + seq[1::2]

def mul_xor_shuffle(item):
    return perfect_shuffle(list(_binstr(_modmul(item) ^ mask)))

if __name__ == '__main__':
    """ mul-xor-shuffle """
    for i in range(1000000):
        obfuscated_i = perfect_shuffle(list(_binstr(_modmul(i) ^ mask)))
        unobfuscat_i = _modmul(int(''.join(perfect_unshuffle(obfuscated_i)), 2) ^ mask)
        if i != unobfuscat_i:
            print('[-] Oh shit: [%u] gave [%u]' % (i, unobfuscat_i))
