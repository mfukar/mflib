#!/usr/bin/env python
# @file        /Users/mfukar/src/mflib/logger.py
# @author      Michael Foukarakis
# @version     0.1
# @date        Created:     Tue Jan 27, 2015 18:19 EET
#              Last Update: Tue Jan 27, 2015 18:21 EET
#------------------------------------------------------------------------
# Description: <+description+>
#------------------------------------------------------------------------
# History:     <+history+>
# TODO:        <+missing features+>
#------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------
import traceback

class ExceptionLogger():
    def __init__(self):
        pass

def log_traceback(ex):
    tb_lines = [line.rstrip('\n') for line in
                traceback.format_exception(ex.__class__, ex, ex.__traceback__)
               ]

    # tb_lines is now a JSON-serialiable list of lines containing the
    # stack trace, such as:
    # [ 'Traceback (most recent call last):',
    #   '  File "example-for-python3.py",
    #   line 14,
    #   in <module>\n    x = int(\'foo\')',
    #   "ValueError: invalid literal for int() with base 10: 'foo'",
    # ]

    # TODO implement the ExceptionLogger class,
    # and the timestamping:
    exception_logger.log(tb_lines)

try:
    x = int('foo')
except Exception as ex:
    log_traceback(ex)
