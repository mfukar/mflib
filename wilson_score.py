#!/usr/bin/env python
# @file        wilson_score.py
# @author      Michael Foukarakis
# @version     0.1
# @date        Created:     Fri Sep 01, 2017 10:19 EEST
#              Last Update: Fri Sep 01, 2017 16:40 EEST
#------------------------------------------------------------------------
# Description: Wilson score interval
#------------------------------------------------------------------------
# History:     <+history+>
# TODO:        <+missing features+>
#------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------
from scipy.stats import norm
from math import sqrt

def ci_lower_bound(positive, n, confidence):
    """Returns the lower-bound Wilson score for a given confidence interval.
    positive (int): Number of positive events
    n (int): Total number of trials
    confidence (float): The percentage of confidence that the 'true' value of
                        positive events is within this confidence interval"""
    if n == 0:
        return 0
    z = norm.ppf(1 - (1 - confidence) / 2.0)
    phat = 1.0 * pos / n
    return (phat + z*z / (2 * n) - z * sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)) / (1 + z*z / n)

