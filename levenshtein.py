#!/usr/bin/env python
# @file        levenshtein.py
# @author      Michael Foukarakis
# @version     0.1
# @date        Created:     Thu Oct 16, 2014 10:57 EEST
#              Last Update: Thu Oct 16, 2014 11:01 EEST
#------------------------------------------------------------------------
# Description: Levenshtein string distance implementation
#------------------------------------------------------------------------
# History:     <+history+>
# TODO:        <+missing features+>
#------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------

def levenshtein(s1, s2):
    """Returns the Levenshtein distance of S1 and S2.
    >>> levenshtein('aabcadcdbaba', 'aabacbaaadb')
    6
    """
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
    if not s1:
        return len(s2)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]
