#!/usr/bin/env python
# @file        mflib/logger.py
# @author      Michael Foukarakis
# @version     0.1
# @date        Created:     Tue Jan 27, 2015 18:19 EET
#              Last Update: Mon Oct 30, 2017 10:54 CET
#------------------------------------------------------------------------
# Description: Useful constructs for logging
#------------------------------------------------------------------------
# History:     <+history+>
# TODO:        <+missing features+>
#------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------
import sys

class duplicate_stdout():
    """Context manager for temporarily duplicating stdout to a file. Like tee, but limited in scope.
    # How to duplicate help() to 'help.txt':
    with duplicate_stdout('help.txt', 'w'):
        help(ord)

    Not reusable, and not reentrant.
    """
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.stdout = sys.stdout

    def __enter__(self):
        self.fh = open(self.path, self.mode)
        return self

    def __exit__(self, *args):
        sys.stdout = self.stdout
        self.fh.flush()
        self.fh.close()

    def write(self, buffer):
        self.fh.write(buffer)
        self.stdout.write(buffer)

    def flush(self):
        self.fh.flush()

class duplicate_stderr():
    """Context manager for temporarily duplicating stderr to a file. Like tee, but limited in scope.

    # How to duplicate sys.stderr.write to 'help.txt':
    with duplicate_stderr('help.txt', 'w'):
        sys.stderr.write(help(ord))

    Not reusable, and not reentrant.
    """
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.stderr = sys.stderr

    def __enter__(self):
        self.fh = open(self.path, self.mode)
        return self

    def __exit__(self, *args):
        sys.stderr = self.stderr
        self.fh.flush()
        self.fh.close()

    def write(self, buffer):
        self.fh.write(buffer)
        self.stderr.write(buffer)

    def flush(self):
        self.fh.flush()
